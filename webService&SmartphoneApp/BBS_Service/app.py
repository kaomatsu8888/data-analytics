# 会員制の掲示板のメインプログラム
from flask import Flask, redirect, url_for, session # Flaskとリダイレクト、セッションをインポートする
from flask import render_template, request # テンプレートとリクエストをインポートする
import os, json, datetime # OSとJSONと日時をインポートする
import bbs_login # ログイン管理用モジュールをインポートする
import bbs_data # データ管理用モジュールをインポートする
# Flaskインスタンスと暗号化キーを設定する
app = Flask(__name__) # Flaskインスタンスを生成する
app.secret_key = 'sunabaco' # 暗号化キーを設定する

# 掲示板のメイン画面を表示する
@app.route('/') # アクセスするURLを指定する
def index():
    # ログインが必要
    if not bbs_login.is_login():
        return redirect('/login') # ログイン画面にリダイレクトする
    # ログインしているならメイン画面を表示する
    return render_template('index.html', 
                           user=bbs_login.get_user(), 
                           data=bbs_data.load_data())

# ログイン画面を表示する
@app.route('/login') # アクセスするURLを指定する
def login():
    return render_template('login.html') # ログイン画面を表示する

# ログイン処理を行う
@app.route('/try_login', methods=['POST']) # アクセスするURLを指定する
def try_login():
    user = request.form.get('user', '') # ユーザー名を取得する
    pw = request.form.get('pw', '') # パスワードを取得する
    # ログインに成功したらルートページに飛ぶ
    if bbs_login.try_login(user, pw):
        return redirect('/')
    # ログインに失敗したらメッセージを表示する
    return show_msg('ログインに失敗しました')

# ログアウト処理を行う
@app.route('/logout') # アクセスするURLを指定する
def logout():
    bbs_login.try_logout() # ログアウトする
    return show_msg('ログアウトしました')

# 書き込み処理
@app.route('/write', methods=['POST']) # アクセスするURLを指定する
def write():
    # ログインが必要
    if not bbs_login.is_login():
        return redirect('/login') # ログイン画面にリダイレクトする
    # フォームのテキストを取得する
    ta = request.form.get('ta', '') # テキストエリアの内容を取得する
    if ta == '': return show_msg('書き込みが空でした')
    # ログを追記保存する
    bbs_data.save_data_append(user=bbs_login.get_user(), text=ta)
    # メイン画面にリダイレクトする
    return redirect('/')

# テンプレートを利用してメッセージを表示する
def show_msg(msg):
    return render_template('msg.html', 
                           msg=msg)

# 実行する
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # デバッグモードを有効にして実行する
