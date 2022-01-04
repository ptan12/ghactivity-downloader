import json
from download1 import download_file

def lambda_handler(event, context):
    download_res = download_file('2021-01-01-0.json.gz')

    return {
        'statusCode': download_res.status_code,
        'body': json.dumps('Download status code')
    }
