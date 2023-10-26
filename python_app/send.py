import requests
import os
from requests.auth import HTTPBasicAuth

# WordPressの認証情報
username =os.getenv("WORDPRESS_USERNAME")
app_pass = os.getenv("WORDPRESS_APP_PASS")
auth = HTTPBasicAuth(username, app_pass)

# 画像をWordPressにアップロード
with open('./img/local_image.jpg', 'rb') as file:
    media_response = requests.post(
        'http://localhost:8000/wp-json/wp/v2/media',
        files={'file': ('image.jpg', file)},
        auth=auth
    )

# レスポンスをチェック
if media_response.status_code == 201:
    media_id = media_response.json()['id']
    media_url = media_response.json()['source_url']
else:
    print('Failed to upload the image.')
    exit()

# 新しいページのデータ
page_data = {
    "title": "Published by OpenIntepreter",
    "content": f'<img src="{media_url}" alt="Image" /> Viva OpenIntepreter!',
    "status": "publish"
}

# POSTリクエストを送信してページを追加
page_response = requests.post('http://localhost:8000/wp-json/wp/v2/pages', json=page_data, auth=auth)

# レスポンスをチェック
if page_response.status_code == 201:
    print('Page created: ', page_response.json()['link'])
else:
    print('Failed to post the page.')