import pymysql
import pandas as pd
import logging
import os

pymysql.install_as_MySQLdb()

def make_personal_data(data):
    conn = pymysql.connect(
            host=os.environ.get('DB_HOST'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            port=3306,
            db=os.environ.get('DB_NAME'),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
        )
    with conn.cursor() as cursor:
        cursor.execute('TRUNCATE TABLE domtory.dormitory_personal_info')
        
        event_data = []
        for index, row in data.iterrows():
            try:
                id = int(row['No'])
                dormitory_code = row['학사번호']
                room_number = row['사실']
                name = row['성명']
                phone_number = row['휴대폰']
                birthday = int(row['생년월일'])
                sql = """
                INSERT INTO domtory.dormitory_personal_info (id, dormitory_code, room_number, name, phone_number, birthday)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (id, dormitory_code, room_number, name, phone_number, birthday))
                event_data.append((id, dormitory_code, name, phone_number, birthday))
            except Exception as e:
                logging.error(f'DB 저장 오류 발생: {e}')
        conn.commit()
                
    return event_data