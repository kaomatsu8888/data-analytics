from flask import Flask, request # Flaskクラスをインポート
app = Flask(__name__) # Flaskのクラスのインスタンスを生成

# サーバールートへアクセスがあった場合にindex関数を実行
@app.route('/') # デコレーターを使ってルーティングを指定
def index():
    # フォームを表示する
    return """
        <html><body>
        <form action="/hello" method="GET">
        名前: <input type="text" name="name">
        <input type="submit" value="送信">
        </form>
        </body></html>
    """

# /helloへアクセスがあった場合にhello関数を実行
@app.route('/hello') # デコレーターを使ってルーティングを指定
def hello():
    # nameパラメーターを取得
    name = request.args.get('name')
    # パラメーターが設定されているか確認
    if name is None: name = '名無し'
        # 自己紹介を自動作成
    return """
        <h1>こんにちは！{0}さん！</h1>
        """.format(name)

if __name__ == "__main__":
    app.run(host="0.0.0.0") # サーバーを起動
