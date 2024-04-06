from make_table import make_personal_data
from get_xls_file_from_s3 import get_xls_file_from_s3
import pandas as pd
import boto3
import json

def send_event_data_to_make_member_event_lambda_function(event_data):
    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
        FunctionName='make_member_event',
        InvocationType='Event',
        Payload=json.dumps(event_data)
    )

def lambda_handler(event, context):
    xls_file, file_extension = get_xls_file_from_s3(event)
    
    data = None
    if file_extension == '.xlsx':
        data = pd.read_excel(xls_file, engine='openpyxl')
    elif file_extension == '.xls':
        data = pd.read_excel(xls_file, engine='xlrd')

    data = data.dropna()
    event_data = make_personal_data(data)
    send_event_data_to_make_member_event_lambda_function(event_data)
    return {
        'statusCode': 200,
    }