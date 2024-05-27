# cook your dish here

"""

"""
# import boto3

# glue_client = boto3.client('glue',aws_access_key_id='AKIA3FLD2VGR5N5MRHOJ',
#                                 aws_secret_access_key='DAz670zHo+gmkvEPhU7PZcCISRILOrQkIzpABqfU',
#                                 region_name='us-east-1')
# response = glue_client.get_table(
#     DatabaseName='reddit-database',
#     Name='maturing_twitter_s3'
# )
# print(response)  # This will print the table definition


import boto3

sts_client = boto3.client('sts')
role_arn = 'arn:aws:iam::767397898659:role/DataEngineerETLRole'   
role_session_name = 's3Access'

# Assume Role
response = sts_client.assume_role(
    RoleArn=role_arn,
    RoleSessionName=role_session_name
)

# Get Temporary Credentials
temp_credentials = response['Credentials']

# Create Boto3 Clients
s3 = boto3.client(
    's3',
    aws_access_key_id=temp_credentials['AccessKeyId'],
    aws_secret_access_key=temp_credentials['SecretAccessKey'],
    aws_session_token=temp_credentials['SessionToken']
)

# ... Now you can use the s3 client to access S3 ...

print(s3)