import praw
import boto3
import json
import time

# Reddit API Configuration

user_agent = 'script:reddit_data_collector:v1.0 (by u/Icy_Order_22)'

reddit = praw.Reddit(
    client_id='xh7iSGmMZsnVEy7SbCtdbw',
    client_secret='llVI86neqfdVqU2i3oT0mvVcM2Otzw',
    user_agent=user_agent
)

# Kinesis Data Firehose Configuration
firehose_client = boto3.client('firehose',aws_access_key_id='AKIA3FLD2VGR5N5MRHOJ',
                                aws_secret_access_key='DAz670zHo+gmkvEPhU7PZcCISRILOrQkIzpABqfU',
                                region_name='us-east-1')
delivery_stream_name = 'PUT-S3-6o341'  # Replace with your stream name

# Data Collection Parameters
subreddit_name = 'StockMarket'
max_posts = 100
sleep_time = 1  # Seconds to sleep between batches

def fetch_and_send_posts():
    subreddit = reddit.subreddit(subreddit_name)

    for post in subreddit.hot(limit=max_posts):
        post_data = {
            'id': post.id,
            'title': post.title,
            'author': post.author.name if post.author else None,
            'created_utc': post.created_utc,
            'score': post.score,
            'num_comments': post.num_comments,
            'upvote_ratio': post.upvote_ratio,
            'url': post.url,
            'selftext': post.selftext
        }

        # Send to Kinesis Data Firehose
        firehose_client.put_record(
            DeliveryStreamName=delivery_stream_name,
            Record={'Data': json.dumps(post_data).encode('utf-8')}
        )

# Main Loop
i=0
while True:
    fetch_and_send_posts()
    i+=1
    print(i)
    time.sleep(sleep_time)  # Sleep to avoid rate limiting
