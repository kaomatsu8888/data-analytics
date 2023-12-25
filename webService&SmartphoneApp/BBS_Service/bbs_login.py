# ログインを実現するモジュールを作成する
from flask import session, redirect

# ログイン用ユーザーの一覧を定義する
USERLIST = {
    'taro': 'aaa',
    'jiro': 'bbb',
    'sabu': 'ccc',
}

# ログインをしているか調べる
def is_login():
    return 'login' in session

# ログインを行う
def try_login(user, password): # ユーザー名とパスワードを受け取る
    # 該当ユーザーがいるか？
    if user not in USERLIST: # ユーザー名が辞書にない
        return False # ログイン失敗
    # パスワードが合っているか？
    if USERLIST[user] != password: # パスワードが一致しない
        return False # ログイン失敗
    # ログイン成功
    session['login'] = user # セッションにログイン情報を保存
    return True # ログイン成功

# ログアウトを行う
def try_logout(): # 引数はなし
    session.pop('login', None) # セッションからログイン情報を削除
    return True # ログアウト成功

# セッションからユーザー名を取得する
def get_user(): # 引数はなし
    if is_login(): return session['login'] # ログインしているならユーザー名を返す
    return 'not login' # ログインしていないならメッセージを返す
