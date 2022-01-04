import os
import boto3
import requests

os.environ.setdefault('AWS_DEFAULT','itvgithub')

s3_client = boto3.client('s3')

# s3_objects = s3_client.list_objects(
#     Bucket='itv-github-pt'
# )
#
# print(s3_objects['Contents'][0])

file='2021-01-01-0.json.gz'
res = requests.get(f'https://data.gharchive.org/{file}')

upload_res = s3_client.put_object(
    Bucket='itv-github-pt',
    Key='2021-01-01-0.json.gz',
    Body=res.content
)

print(upload_res)