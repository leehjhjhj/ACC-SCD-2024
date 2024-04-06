from db_connection import return_connection
from crawling import crawling_menu
from parser_view import crawling_notice
from crawling import crawling_menu

def lambda_handler():
    conn = return_connection()
    crawling_menu(conn)
    crawling_notice(conn)
    return {
        'statusCode': 200
    }