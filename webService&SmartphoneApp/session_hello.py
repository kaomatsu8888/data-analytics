# セッションを利用してデータを保存してみる
from flask import Flask, request, session, redirect
app = Flask(__name__) # Flaskのクラスのインスタンスを生成
app.secret_key = "9KStWezC" # セッションを暗号化するためのキーを設定
@app.route('/') # デコレーターを使ってルーティングを指定
def index():
    # ユーザー名の入力フォームを出力
    return """
    <html><body><h1>ユーザー名を入力</h1>
    <form action="/setname" method="GET">
        名前: <input type="text" name="username">
        <input type="submit" value="開始">
    </form></body></html>
    """

@app.route('/setname') # デコレーターを使ってルーティングを指定
def setname():
    # GETの値を取得
    name = request.args.get('username') # ユーザー名を取得
    if not name: return redirect('/')
    # セッションに値を保存
    session['name'] = name
    # 他のページにリダイレクト
    return redirect('/morning')

def getLinks():
    # リンクのHTMLを作成
    result = """
    <ul><li><a href="/morning">朝の挨拶</a></li>
    <li><a href="/afternoon">昼の挨拶</a></li>
    <li><a href="/evening">夜の挨拶</a></li></ul>
    """
    return result  # リンクのHTMLを返す

@app.route('/morning') # デコレーターを使ってルーティングを指定
def morning():
    # セッションにnameがある？
    if not ("name" in session):
        # ない場合はリダイレクト
        return redirect('/')
    # セッションからnameを取得
    name = session['name']
    # メッセージを表示
    return """
    <h1>おはようございます！{0}さん！</h1>{1}
    """.format(name, getLinks())

@app.route('/afternoon') # デコレーターを使ってルーティングを指定
def afternoon():
    # セッションにnameがある？
    if not ("name" in session):
        # ない場合はリダイレクト
        return redirect('/')
    # セッションからnameを取得
    name = session['name']
    # メッセージを表示
    return """
    <h1>こんにちは！{0}さん！</h1>{1}
    """.format(session["name"], getLinks())

@app.route('/evening') # デコレーターを使ってルーティングを指定
def evening():
    # セッションにnameがある？
    if not ("name" in session):
        # ない場合はリダイレクト
        return redirect('/')
    # セッションからnameを取得
    name = session['name']
    # メッセージを表示
    return """
    <h1>こんばんは！{0}さん！</h1>{1}
    """.format(session["name"], getLinks())

if __name__ == "__main__":
    app.run(host="0.0.0.0") # サーバーを起動
