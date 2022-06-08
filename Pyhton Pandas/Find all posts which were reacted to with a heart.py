# cook your dish here

"""
Find all posts which were reacted to with a heart


Meta/Facebook
Easy
General Practice
ID 10087
9
8
Find all posts which were reacted to with a heart.


"""

# Import your libraries
import pandas as pd

# Start writing code
facebook_reactions.head()
# Double quote output data frame.
heart=facebook_reactions[facebook_reactions['reaction']=='heart'][['post_id']]
result=pd.merge(heart,facebook_posts,on='post_id',how='inner').drop_duplicates(subset='post_id')


# Import your libraries
import pandas as pd

# Start writing code
df=pd.merge(facebook_reactions[['reaction','post_id']],facebook_posts,on='post_id',how='inner')
df1=df[df['reaction']=='heart']
df1.drop_duplicates()


# Import your libraries
import pandas as pd

# Start writing code
index = facebook_reactions[facebook_reactions['reaction']=='heart']['post_id'].unique()
facebook_posts[facebook_posts['post_id'] == index[0]]