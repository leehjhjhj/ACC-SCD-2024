from PIL import Image
import boto3
import io
import os

class S3Connect:
    def __init__(self):
        self._s3_conn = boto3.client('s3')
        self._bucket_name = os.environ.get('BUCKET_NAME')
        
    def get_s3_image_object(self, key):
        response = self._s3_conn.get_object(Bucket=self._bucket_name, Key=key)
        image_data = response['Body'].read()
        image = Image.open(io.BytesIO(image_data))
        return image
        
    def put_s3_image_object(self, image_data, key):
        self._s3_conn.put_object(Body=image_data, Bucket=self._bucket_name, Key=key)