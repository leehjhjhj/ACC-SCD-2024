from make_light_logo import process_logo
from s3 import S3Connect
import io

def lambda_handler(event, context):
    for record in event['Records']:
        s3_key = record['body']
        s3 = S3Connect()
        try:
            original_logo = s3.get_s3_image_object(s3_key)
            original_format = original_logo.format
            
            new_logo = process_logo(original_logo, original_format)
            out_img = io.BytesIO()
            new_logo.save(out_img, format=original_format, quality=70)
            out_img.seek(0)
            s3.put_s3_image_object(out_img, s3_key)
        except Exception as e:
            print("오류:{}, S3키:{}".format(e, s3_key))
    return {
        'statusCode': 200
    }