import json
import urllib.request
import boto3
import os

class DatabaseAccess:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table("")
        
    def put_data(self, input_data):
        self.table.put_item(
            Item =  input_data
        )
def lambda_handler(event, context):
    name = event['name']
    db = DatabaseAccess()
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {"role": "system", "content": "한국이름 세글자를 받으면 상냥한 말투로 2024년 운세 한 줄과 피해야할 것을 한 줄로 말해."},
            {'role': 'user', 'content': f'{name}'}
        ]
    }

    api_keys = [os.environ.get('OPENAPI_KEY1')]

    for api_key in api_keys:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

        request = urllib.request.Request(
            'https://api.openai.com/v1/chat/completions',
            data=json.dumps(data).encode('utf-8'),
            headers=headers,
            method='POST'
        )

        try:
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))

            fortune = result['choices'][0]['message']['content'].strip()
            db.put_data({"name": name, "detail": fortune})
            return {
                'statusCode': 200,
                'headers': { 'Content-Type': 'application/json' },
                'body': fortune
            }
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"429 Error occurred, switching API key to the next one.")
                continue
