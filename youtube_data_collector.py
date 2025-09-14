import pandas as pd
from googleapiclient.discovery import build
import os

def get_channel_videos(api_key, channel_id):
    """
    Fetches the 50 most recent video details for a given YouTube channel.
    """
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get the playlist ID for the channel's uploads
    request = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    )
    response = request.execute()
    
    if 'items' not in response or not response['items']:
        print(f"Could not find channel with ID: {channel_id}")
        return []
        
    playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    # Get the most recent 50 videos from the uploads playlist
    while True:
        request = youtube.playlistItems().list(
            part='snippet,contentDetails',
            playlistId=playlist_id,
            maxResults=50, # Max allowed per page
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            video_id = item['contentDetails']['videoId']
            video_title = item['snippet']['title']
            published_date = item['snippet']['publishedAt']
            
            # A separate API call is needed to get stats for each video
            stats_request = youtube.videos().list(
                part='statistics,snippet',
                id=video_id
            )
            stats_response = stats_request.execute()

            if 'items' in stats_response and stats_response['items']:
                video_stats = stats_response['items'][0]['statistics']
                video_snippet = stats_response['items'][0]['snippet']
                
                video_details = {
                    'channel_id': channel_id,
                    'channel_title': video_snippet.get('channelTitle', ''),
                    'video_id': video_id,
                    'title': video_title,
                    'published_at': published_date,
                    'description': video_snippet.get('description', ''),
                    'tags': ','.join(video_snippet.get('tags', [])), # Join tags into a single string
                    'view_count': int(video_stats.get('viewCount', 0)),
                    'like_count': int(video_stats.get('likeCount', 0)),
                    'comment_count': int(video_stats.get('commentCount', 0)),
                }
                videos.append(video_details)

        # Since we only want the most recent 50, we break after the first page
        break
        
    return videos

if __name__ == '__main__':
    # --- IMPORTANT ---
    # 1. Replace "YOUR_API_KEY" with the key you generated in Step 1.
    # 2. Make sure you have the channel IDs for the channels you want to analyze.
    API_KEY = "AIzaSyDKB2goSLOWNxv7vRZ-NKMYKmpM1jbFB44" 

    # List of Channel IDs for "Personal Finance for Millennials in India"
    CHANNEL_IDS = [
        'UCN_b9a2Rk_cUR_5_q5a_a7g', # Ankur Warikoo
        'UCe3qdG0A_gr-sEdat5y2twQ', # CA Rachana Phadke Ranade
        'UCbAdpE-0D_4t32G_p8_T6LA', # Pranjal Kamra
        'UCg4_a0Q-G_5uC-JbA9I1_3w', # Labour Law Advisor
        'UCV3wGu3Vv3z42c0L_e_kchw', # Asset Yogi
        # Add the rest of the 15 channel IDs here...
    ]

    all_videos_data = []
    print("Starting data collection...")

    for channel_id in CHANNEL_IDS:
        print(f"Fetching videos for channel ID: {channel_id}")
        try:
            channel_videos = get_channel_videos(API_KEY, channel_id)
            if channel_videos:
                all_videos_data.extend(channel_videos)
                print(f"Successfully fetched {len(channel_videos)} videos.")
            else:
                print(f"No videos found or error fetching for channel ID: {channel_id}")
        except Exception as e:
            print(f"An error occurred for channel ID {channel_id}: {e}")

    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(all_videos_data)

    # Save the DataFrame to a CSV file
    output_filename = 'youtube_finance_videos_raw.csv'
    df.to_csv(output_filename, index=False, encoding='utf-8')

    print(f"\nData collection complete. {len(df)} videos saved to {output_filename}")
