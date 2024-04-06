import requests
from make_blocks import make_blocks

def lambda_handler(event, context):
    url = ''
    data = {
        "db_name": "디비이름",
        "name": "회의이름",
        "part": "참여 파트 ex)백엔드",
        "day": "금요일",
        "time": "18:00",
        "type": "비대면",
        "blocks": make_blocks()
    }
    response = requests.post(url, json=data)
    return {
        'statusCode': response.status_code,
        'body': response.json()
    }