# ログイン処理を実装
from flask import Flask, request, session, redirect
app = Flask(__name__) # Flaskのクラスのインスタンスを生成
app.secret_key = 'hogehoge' # セッションを暗号化するためのキーを設定

# ログインに使うユーザー名とパスワード
USERLIST = {
    "taro": "aaa",
    "jiro": "bbb",
    "sabu": "ccc",
    }

@app.route('/') # デコレーターを使ってルーティングを指定
def index():
    # ログインフォームの表示
    return """
    <html><body><h1>ログインフォーム</h1>
    <form action="/check_login" method="POST">
    ユーザー名: <br/>
    <input type="text" name="user"><br>
    パスワード: <br/>
    <input type="password" name="pw"><br>
    <input type="submit" value="ログイン">
    </form>
    <p><a href="/private">秘密のページ</a></p>
    """

@app.route('/check_login', methods=['POST']) # デコレーターを使ってルーティングを指定
def check_login():
    # フォームの値を取得
    user, pw = (None, None) # ユーザー名とパスワード
    if 'user' in request.form: 
        user = request.form['user'] # ユーザー名を取得
    if 'pw' in request.form:
        pw = request.form['pw']
    # ユーザー名とパスワードをチェック
    if (user is None) or (pw is None):
        return redirect('/')
    # ログインチェック
    if try_login(user, pw) == False:
        return """
        <h1>ログイン失敗！</h1>
        <p><a href="/">戻る</a></p>
        """
    # 非公開ページへリダイレクト
    return redirect('/private')

@app.route('/private') # デコレーターを使ってルーティングを指定
def private_page():
    # ログインしているかチェック
    if not is_login():
        return """
        <h1>ログインしてください！</h1>
        <p><a href="/">→ログインする</a></p>
        """
    # 秘密のページを表示
    return """
    <h1>秘密のページ</h1>
    <p>ログイン成功！</p>
    <p><a href="/">→ログアウト</a></p>
    """

@app.route('/logout') # デコレーターを使ってルーティングを指定
def logout_page():
    try_logout() # ログアウト処理
    return """
    <h1>ログアウトしました</h1>
    <p><a href="/">→ログインする</a></p>
    """

# 以下、ログインに関する処理をまとめたもの
# ログインしているかチェック
def is_login():
    if 'login' in session:
        return True
    return False

# ログイン処理
def try_login(user, password):
    # ユーザーがリストに存在するかチェック
    if not user in USERLIST:
        return False
    # パスワードをチェック
    if USERLIST[user] != password:
        return False
    # ログイン成功
    session['login'] = user
    return True

# ログアウト処理
def try_logout():
    session.pop('login', None)
    return True

if __name__ == "__main__":
    app.run(host="0.0.0.0") # サーバーを起動
