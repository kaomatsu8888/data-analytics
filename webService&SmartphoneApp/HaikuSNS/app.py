# 俳句SNSのメインプログラム
from flask import Flask, redirect, render_template  # Flask: Flaskのクラスをインポート
from flask import request # request: リクエストを受け取る
from markupsafe import Markup # request: リクエストを受け取る
import os, time # os: ファイル操作, time: 時間を扱う
import sns_user as user, sns_data as data # sns_user: ユーザー情報を扱う, sns_data: データを扱う

# Flaskクラスのインスタンスと暗号化キーの指定
app = Flask(__name__)
app.secret_key = 'HaikuSNS'

# URLのルーティング
# ログイン画面
@app.route('/')
@user.login_required
def index():
    me = user.get_id()
    return render_template('index.html', id=me,
                        users=user.get_allusers(),
                        fav_users=data.get_fav_list(me),
                        timelines=data.get_timeline(me))

@app.route('/login') 
def login(): # ログイン画面を表示
    return render_template('login_form.html') # ログイン画面を表示

@app.route('/login/try', methods=['POST'])
def login_try():
    ok = user.try_login(request.form) # ログインの試行
    if not ok: return msg('ログインに失敗しました')
    return redirect('/')

@app.route('/logout')
def logout():
    user.try_logout()
    return msg('ログアウトしました')

@app.route('/users/<user_id>')
@user.login_required
def users(user_id):
    if user_id not in user.USER_LOGIN_LIST:
        return msg('ユーザーが存在しません')
    me = user.get_id()
    return render_template('user.html', 
                        user_id=user_id, id=me,
                        is_fav=data.is_fav(me, user_id),
                        text_list=data.get_text(user_id))

@app.route('/fav/add/<user_id>')
@user.login_required
def fav_add(user_id):
    data.add_fav(user.get_id(), user_id)
    return redirect('/users/' + user_id)

@app.route('/fav/remove/<user_id>')
@user.login_required
def remove_fav(user_id):
    data.remove_fav(user.get_id(), user_id)
    return redirect('/users/' + user_id)

@app.route('/write')
@user.login_required
def write():
    return render_template('write_form.html', id=user.get_id())

@app.route('/write/try', methods=['POST'])
@user.login_required
def try_write():
    text = request.form.get('text', '')
    if text == '':
        return msg('俳句が空です')
    data.write_text(user.get_id(), text)
    return redirect('/')

def msg(msg):
    return render_template('msg.html', msg=msg)

# テンプレートのフィルターなど拡張機能の指定
# CSSなどの静的ファイルの後ろにバージョンを自動追記
@app.context_processor
def add_staticfile():
    return dict(staticfile=staticfile_cp)
def staticfile_cp(fname):
    path = os.path.join(app.root_path, 'static', fname)
    mtime = str(int(os.stat(path).st_mtime))
    return '/static/' + fname + '?v=' + str(mtime)

# 改行を有効にするフィルターを追加
@app.template_filter('linebreak')
def linebreak_filter(s):
    s = s.replace('&', '&amp;').replace('<', '&lt;') \
        .replace('>', '&gt;').replace('\n', '<br>')
    return Markup(s)

# 日付をフォーマットするフィルターを追加
@app.template_filter('datestr')
def datestr_filter(s):
    return time.strftime('%Y 年 %m 月 %d 日', time.localtime(s))

# メインプログラム
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # デバッグモードを有効にして実行
