# ユーザーとログイン管理のモジュール
# ログインなどユーザーに関する処理をまとめた
from flask import Flask, session, redirect
from functools import wraps

# ユーザー名とパスワードの一覧
USER_LOGIN_LIST = {
    'taro': 'aaa',
    'jiro': 'bbb',
    'sabu': 'ccc',
    'siro': 'ddd',
    'goro': 'eee',
    'muro': 'fff'
}

# ログインしているかどうかのチェック
def is_login():
    return 'login' in session

# ログインを試行する
def try_login(form):
    user = form.get('user', '')
    password = form.get('pw', '')
    # パスワードチェック
    if user not in USER_LOGIN_LIST:
        return False
    if USER_LOGIN_LIST[user] != password:
        return False
    # ログイン成功
    session['login'] = user
    return True

# ユーザー名を取得する
def get_id():
    return session['login'] if is_login() else '未ログイン'

# 全ユーザー名を取得する
def get_allusers():
    return [u for u in USER_LOGIN_LIST ]

# ログアウトする
def try_logout():
    session.pop('login', None)

# ログイン必須を処理するデコレーター
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_login():
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper
