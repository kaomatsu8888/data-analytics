from flask import Flask, render_template # Flaskクラスをインポート

app = Flask(__name__) # Flaskのクラスのインスタンスを生成

@app.route('/') # デコレーターを使ってルーティングを指定
def index(): # index関数を定義
    users = [ # テンプレートに渡すデータを定義
        {"name": "フリーレン", "age": 1020},
        {"name": "シュタルク", "age": 19},
        {"name": "フェルン", "age": 19},
        ]
    return render_template('users.html', # テンプレートを指定
                            users=users) # テンプレートに渡すデータを指定

if __name__ == '__main__': # 実行されたファイルがスクリプトとして実行されたかどうかを判定
    app.run(host='0.0.0.0') # Webサーバーを起動
