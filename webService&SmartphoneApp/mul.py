from flask import Flask, request # Flaskクラスをインポート
app = Flask(__name__) # Flaskのクラスのインスタンスを生成

@app.route('/') # デコレーターを使ってルーティングを指定
def index():
    # URLパラメーターを取得
    a = request.args.get('a')
    b = request.args.get('b')
    # パラメーターが設定されているか確認
    if (a is None) or (b is None):
        return "パラメーターが足りません"
    # パラメーターを数値に変換
    c = int(a) * int(b)
    # 結果を表示
    return "<h1>" + str(c) + "</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0") # サーバーを起動
