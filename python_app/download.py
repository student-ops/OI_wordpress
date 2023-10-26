import requests

# 画像のURL
img_url = 'https://example.com/image.jpg'

# 画像をダウンロード
response = requests.get(img_url)

# レスポンスをチェックし、画像を保存
if response.status_code == 200:
    with open('./img/image.jpg', 'wb') as file:
        file.write(response.content)
else:
    print('Failed to retrieve the image.')
