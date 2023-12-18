from flask import Flask, render_template # Flaskクラスをインポート

app = Flask(__name__) # Flaskのクラスのインスタンスを生成

@app.route('/') # デコレーターを使ってルーティングを指定
def index(): # index関数を定義
    # データを指定
    username = "ヒンメル"
    age = 19
    email = "hinmel@example.com"
    # テンプレートにデータを渡す
    return render_template('card.html', # テンプレートを指定
                            username=username, # データを指定
                            age=age, # データを指定
                            email=email) # データを指定

if __name__ == '__main__': # 実行されたファイルがスクリプトとして実行されたかどうかを判定
    app.run(host='0.0.0.0') # Webサーバーを起動
