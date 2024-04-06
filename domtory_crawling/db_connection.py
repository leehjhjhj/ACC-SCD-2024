import pymysql
import os

def return_connection():
    conn = pymysql.connect(
        host='',
        user='',
        password='',
        port=3306,
        db='',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
    )
    return conn