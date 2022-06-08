# cook your dish here

"""
Find songs that have more than 3 million streams


Spotify
Easy
General Practice
ID 9990
1
0
Find songs that have more than 3 million streams.
Output the track name, artist, and the corresponding streams.
Sort records based on streams in descending order.

"""

# Import your libraries
import pandas as pd

# Start writing code
df=spotify_worldwide_daily_song_ranking

df=df.loc[df['streams']>3000000,['trackname','artist','streams']]
df.sort_values('streams',ascending=False)