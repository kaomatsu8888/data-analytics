from flask import Flask, render_template # Flaskクラスをインポート
app = Flask(__name__) # Flaskのクラスのインスタンスを生成

@app.route('/') # デコレーターを使ってルーティングを指定
def index():
    # テンプレートエンジンに渡すデータを指定
    return render_template( # テンプレートエンジンを使ってHTMLを表示
        "card-age.html", # テンプレートファイルを指定
        username="フリーレン",
        age=20,
        email="friere@example.com")
if __name__ == "__main__":
    app.run(host="0.0.0.0") # サーバーを起動
