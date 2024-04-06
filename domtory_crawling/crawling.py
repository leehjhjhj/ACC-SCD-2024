import requests
from bs4 import BeautifulSoup

def crawling_menu(conn):
    with conn.cursor() as cursor:
        try:
            url = 'http://cbhs2.kr/meal?searchWeek=0'

            # 웹페이지에서 HTML 내용을 가져온다
            response = requests.get(url)
        except Exception as e:
            print("request error:", e)
        response.encoding = 'utf-8'
        html = response.text
        # BeautifulSoup 객체를 생성하여 HTML을 파싱.
        soup = BeautifulSoup(html, 'html.parser')
        
        # 모든 식단 찾기
        meal_plans = soup.find_all('div', class_='fplan_plan')
        
        # 각 식단 계획에 대해 요일과 식사 시간대별 메뉴 추출
        for plan in meal_plans:
            date_detail = plan.find('a', class_='btn_type1 fplan_date_sun').text.strip()
            date_code = date_detail[:8].replace('.', '')

            cursor.execute("SELECT * FROM domtory.menu_menu WHERE date_code = %s", (date_code,))
            if cursor.fetchone():
                continue
            cursor.execute(
                        "INSERT INTO domtory.menu_menu (date_code, date_detail) VALUES (%s, %s)",
                        (date_code, date_detail)
            )
            conn.commit()
            try:
                # 해당 일의 식단 정보를 저장할 딕셔너리 생성
                meal_info = {
                    'breakfast': '',
                    'lunch': '',
                    'dinner': ''
                }
                # 조식, 중식, 석식 메뉴 추출
                meals = plan.find_all(['h3', 'p'], recursive=False)
                current_meal = None
                for item in meals:
                    if item.name == 'h3':
                        if '조식' in item.text:
                            current_meal = 'breakfast'
                        elif '중식' in item.text:
                            current_meal = 'lunch'
                        elif '석식' in item.text:
                            current_meal = 'dinner'
                    elif item.name == 'p' and current_meal:
                        meal_info[current_meal] = item.text.strip()

                breakfast_data = meal_info.pop('breakfast').split(',')
                lunch_data = meal_info.pop('lunch').split(',')
                dinner_data = meal_info.pop('dinner').split(',')
        
                for breakfast in breakfast_data:
                    cursor.execute(
                        "INSERT INTO domtory.menu_breakfast (name, menu_id) VALUES (%s, %s)",
                        (breakfast.strip(), date_code)
                    )
        
                for lunch in lunch_data:
                    cursor.execute(
                        "INSERT INTO domtory.menu_lunch (name, menu_id) VALUES (%s, %s)",
                        (lunch.strip(), date_code)
                    )
        
                for dinner in dinner_data:
                    cursor.execute(
                        "INSERT INTO domtory.menu_dinner (name, menu_id) VALUES (%s, %s)",
                        (dinner.strip(), date_code)
                    )
                conn.commit()
            except Exception as e:
                print("저장 오류:", e)