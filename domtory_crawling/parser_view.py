from bs4 import BeautifulSoup
import requests
import pymysql

def scrape_page(page):
    # Construct the URL for the specific page
    url = f"http://cbhs2.kr/0000007?where=&keyword=&page={page}"

    # Get the content of the page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the links to the posts on the page
    posts = soup.select(".Board_LISTC .mr_TITLE a")

    # Create new links for each post on the page
    new_links = []
    for post in posts:
        link = post.attrs.get('onclick', '')
        post_id_start = link.find("goRead('") + len("goRead('")
        post_id_end = link.find("')", post_id_start)
        post_id = link[post_id_start:post_id_end]
        new_url = f"http://cbhs2.kr/0000007?postId={post_id}&mode=READ&where=&keyword=&page={page}"
        new_links.append(new_url)

    # List to store post data
    post_data_list = []

    # Iterate through each post link and scrape data
    for new_link in new_links:
        response = requests.get(new_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        post_data = {}

        # Extract post_id
        post_id_element = soup.select_one('#postId')
        if post_id_element:
            post_data['post_id'] = post_id_element.get('value')

        # Extract title
        title_element = soup.select_one(".v_TITLE")
        if title_element:
            post_data['title'] = title_element.get_text(strip=True)

        # Extract date
        date = soup.select_one(".TrRoll td[colspan='2']")
        if date:
            post_data['date'] = date.select_one(".v_DBDATE").get_text(strip=True)

        post_data['notice_url'] = new_link
            

        # Append post_data to the list
        post_data_list.append(post_data)

    return post_data_list

def crawling_notice(conn):
    # Set the starting page
    with conn.cursor() as cursor:
        all_posts_data = []

        # Scrape all pages
        posts_data = scrape_page(0)

        all_posts_data.extend(posts_data)

        # Reverse the order of the posts data list
        reversed_posts_data = reversed(all_posts_data)
        cursor.execute("SELECT post_id FROM domtory.notice_noticelist")
        exist_notices_id_set = set(row['post_id'] for row in cursor.fetchall())
        
        for post in reversed_posts_data:
            if post['post_id'] not in exist_notices_id_set:
                cursor.execute("INSERT INTO domtory.notice_noticelist (post_id, title, date, notice_url) VALUES (%s, %s, %s, %s)", (post['post_id'], post['title'], post['date'], post['notice_url']))
        conn.commit()