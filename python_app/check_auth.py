import os
import requests
from requests.auth import HTTPBasicAuth

# 認証情報
username = "oi_test"
app_pass=os.getenv("WORDPRESS_APP_PASS")
# エンドポイントURL
url = 'http://localhost:8000/wp-json/wp/v2/users/me'

# GETリクエストを送信してユーザー情報を取得
response = requests.get(url, auth=HTTPBasicAuth(username, app_pass))

# レスポンスをチェック
if response.status_code == 200:
    user_info = response.json()
    # ユーザーが投稿を作成する権限を持っているかどうかを確認
    print(user_info)
else:
    print('failed to post ')