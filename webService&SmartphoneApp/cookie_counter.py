# FlaskでCookieを使う方法
# FlaskではCookieを使うために、make_response関数を使う。
# 以下のように、make_response関数を使って、Responseオブジェクトを作成する。
from flask import Flask
from flask import make_response,request # cookieを使うためにmake_responseをインポート
from datetime import datetime # cookieの有効期限を設定するためにdatetimeをインポート
app = Flask(__name__) # Flaskのクラスのインスタンスを生成

@app.route('/') # デコレーターを使ってルーティングを指定
def index():
    # cookieの値を取得
    cnt_s = request.cookies.get('cnt')
    if cnt_s is None:
        cnt = 0
    else:
        cnt = int(cnt_s)
    # 訪問回数カウンタに1を加算
    cnt += 1
    response = make_response("""
        <h1>訪問回数：{0}</h1>
    """.format(cnt))
    # cookieの値を設定
    max_age = 60 * 60 * 24 * 90  # 有効期限は90日
    expires = int(datetime.now().timestamp()) + max_age # 有効期限の日時
    response.set_cookie('cnt', value=str(cnt), max_age=max_age, expires=expires) # cookieを設定
    return response # レスポンスを返す

if __name__ == "__main__": # 実行されたファイルがスクリプトとして実行されたかどうかを判定
    app.run(host="0.0.0.0", debug=True)  # サーバーを起動.debug=Trueでデバッグモードになる

