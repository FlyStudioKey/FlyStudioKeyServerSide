from django.shortcuts import HttpResponse
from qcloud_cos import CosConfig, CosClientError, CosServiceError
from qcloud_cos import CosS3Client
import os

secret_id = os.environ['COS_SECRET_ID']
secret_key = os.environ['COS_SECRET_KEY']
region = 'ap-beijing'

token = None
scheme = 'https'

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)


def download(file):
    for i in range(0, 10):
        try:
            response = client.download_file(
                Bucket=os.environ['Bucket'],
                Key=file,
                DestFilePath=file)
            break
        except CosClientError or CosServiceError as e:
            print(e)


def upload(file):
    for i in range(0, 10):
        try:
            response = client.upload_file(
                Bucket=os.environ['Bucket'],
                Key=file,
                LocalFilePath=file)
            break
        except CosClientError or CosServiceError as e:
            print(e)


# Create your views here.
def get(request):
    pass
