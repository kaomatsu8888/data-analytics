from flask import Flask

# Flaskのインスタンスを作成
app = Flask(__name__)

# ルーティングの設定
@app.route('/')
def hello_world():
    return 'Hello, Flask!'

# 実行する
if __name__ == '__main__':
    app.run(host= '0.0.0.0')
