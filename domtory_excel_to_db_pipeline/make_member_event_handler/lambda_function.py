import pymysql
import boto3
import os

pymysql.install_as_MySQLdb()

def lambda_handler(event, context):
    conn = pymysql.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        port=3306,
        db=os.environ.get('DB_NAME'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
    )
    event_data = event
    with conn.cursor() as cursor:
        # 기존 회원들의 username을 set에 담기
        cursor.execute("SELECT username FROM domtory.member")
        existing_usernames = set(row['username'] for row in cursor.fetchall())
    
        # 새로운 회원 데이터를 추가
        for data in event_data:
            member_id, dormitory_code, name, phone_number, birthday = data
            # 기존 회원 username에서 일치하는 회원 정보가 없는 경우에만 추가
            if dormitory_code not in existing_usernames:
                cursor.execute("INSERT INTO domtory.member (username, password, name, phone_number, birthday, status) VALUES (%s, %s, %s, %s, %s, 'ACTIVE')", (dormitory_code, birthday, name, phone_number, birthday))
                cursor.execute("INSERT INTO domtory.notification_detail (breakfast, lunch, dinner, lightning_post, comment, reply, member_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", (1, 1, 1, 1, 1, 1, member_id))
        conn.commit()
        
    return {
        'statusCode': 200
    }
