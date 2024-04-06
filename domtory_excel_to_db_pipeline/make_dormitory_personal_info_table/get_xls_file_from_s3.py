import json
from io import BytesIO
import boto3
from urllib.parse import unquote
import os

def get_xls_file_from_s3(event):
    s3 = boto3.client('s3')

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = unquote(event['Records'][0]['s3']['object']['key'])
    
    _, file_extension = os.path.splitext(file_key)
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    return BytesIO(obj['Body'].read()), file_extension