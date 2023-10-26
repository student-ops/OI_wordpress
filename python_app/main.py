import interpreter
import os

interpreter.auto_run = True

username =os.getenv("WORDPRESS_USERNAME")
app_pass=os.getenv("WORDPRESS_APP_PASS")




auth = """
username = "oi_test"
app_pass=os.getenv("WORDPRESS_APP_PASS")
"""
interpreter.chat("./send.pyを使用してページをwordpressで投稿してください")


interpreter.chat("特に指定はしません。画像を使用したページをアップロードして")
interpreter.chat("続けて")
interpreter.chat("it's information you need to know." + auth)
interpreter.chat("コード、コマンドを実行してください")
