import os
import requests

username =os.getenv("WORDPRESS_USERNAME")
app_pass=os.getenv("WORDPRESS_APP_PASS")

# WordPressのエンドポイントと認証情報
url = 'http://localhost:8000/wp-json/wp/v2/pages'
auth = (username, app_pass)

# 追加するページのデータ
data = {
    "title": "New Page",
    "content": "This is the content of the new page.",
    "status": "publish"
}

# POSTリクエストを送信してページを追加
response = requests.post(url, json=data, auth=auth)

# レスポンスをチェック
if response.status_code == 201:
    print(f'Page created: {response.json()["link"]}')
else:
    print(f'Failed to create page: {response.status_code} - {response.text}')
