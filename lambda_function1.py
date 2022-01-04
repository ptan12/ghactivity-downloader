import os
from download1 import download_file
from upload1 import upload_s3


def lambda_handler(event, context):
    file = '2021-01-29-2.json.gz'
    download_res = download_file(file)
    bucket = os.environ.get('BUCKET_NAME')
    file_prefix = os.environ.get('FILE_PREFIX')
    environ = os.environ.get('ENVIRON')
    if environ == 'DEV':
        print(f'Running in {environ} environment')
        os.environ.setdefault('AWS_PROFILE', 'itvgithub')
    upload_res = upload_s3(
        download_res.content,
        bucket,
        f'{file_prefix}/{file}'
    )
    return upload_res