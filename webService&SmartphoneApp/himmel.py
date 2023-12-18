# 19歳ヒンメルのデータをcard.htmlに渡しています。

from flask import Flask, render_template # Flaskクラスをインポート
app = Flask(__name__) # Flaskのクラスのインスタンスを生成

@app.route('/') # デコレーターを使ってルーティングを指定
def index():
    # テンプレートエンジンに渡すデータを指定
    return render_template('index.html'
