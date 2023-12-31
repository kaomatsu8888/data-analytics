from flask import Flask, redirect, request # Flaskとリダイレクトとリクエストをインポートする
from flask import render_template, send_file # テンプレートとファイル送信をインポートする
import os, json, time # OSとJSONと時間をインポートする
import fs_data # データ管理用モジュールをインポートする


app = Flask(__name__) # Flaskインスタンスを生成する
MASTER_PW = "abcd" # マスターパスワードを設定する

@app.route('/') # アクセスするURLを指定する
def index():
    #ファイルのアップロードフォームを表示
    return render_template('index.html')

@app.route('/upload', methods=['POST']) # アクセスするURLを指定する
def upload():
    # アップロードしたファイルのオブジェクト
    upfile = request.files.get('upfile', None) # ファイルを取得する
    if upfile is None: return msg('アップロード失敗')
    if upfile.filename == '': return msg('アップロード失敗')
    # メタ情報を取得する
    meta = {
        'name': request.form.get('name', '名無し'), # 名前を取得する
        'memo': request.form.get('memo', 'なし'), # メモを取得する
        'pw': request.form.get('pw', ''), # パスワードを取得する
        'limit': int(request.form.get('limit', '1')), # 期限を取得する
        'count': int(request.form.get('count', '0')), # ダウンロード回数を取得する
        'filename': upfile.filename # ファイル名を取得する
}
    if (meta['limit'] == 0) or (meta['pw'] == ''): 
        return msg('パラメーターが不正です')
# ファイルを保存する
    fs_data.save_file(upfile, meta)
# ダウンロード先の表示
    return render_template('info.html',
                        meta=meta, mode='upload', 
                        url=request.host_url + 'download/' + meta['id'])

@app.route('/download/<id>') # アクセスするURLを指定する
def download(id):
    # URLが正しいかチェックする
    meta = fs_data.get_data(id)
    if meta is None: return msg('パラメーターが不正です')
    # ダウンロードページを表示する
    return render_template('info.html', 
                        meta=meta, mode='download', 
                        url=request.host_url + 'download_go/' + id)

@app.route('/download_go/<id>', methods=['POST']) # アクセスするURLを指定する
def download_go(id):
    print("download_go function called with ID:", id)
    # URLが正しいかチェックする
    meta = fs_data.get_data(id)
    # エラーのためprintを追加。ここでパスの存在を確認 #
    if os.path.exists(meta['path']):
        print("File exists at:", meta['path'])
    else:
        print("File does not exist at:", meta['path'])

    if meta is None: return msg('パラメーターが不正です')
    # パスワードが合っているかチェックする
    pw = request.form.get('pw', '')
    if pw != meta['pw']: return msg('パスワードが違います')
    # ダウンロード回数のチェック
    meta['count']  = meta['count'] - 1 # ダウンロード回数を減らす
    if meta['count'] < 0: return msg('ダウンロード回数を超えました')
    fs_data.set_data(id, meta) # メタ情報を更新する
    # ダウンロード期限のチェック
    if meta['time_limit'] < time.time(): return msg('ダウンロード期限が切れました')
    # ダウンロード出来るようにファイルを送信する
    print("File path:", meta['path']) # パスを表示
    return send_file(meta['path'], as_attachment=True, download_name=meta['filename']) # ファイルを送信する
    # 注記attachment_filenameをdownload_nameに変更した。as_attachment=Trueはファイルをダウンロードするためのもの。attachmentは使えない


@app.route('/admin/list') # アクセスするURLを指定する
def admin_list():
    # マスターパスワードのチェック
    if request.args.get('pw', '') != MASTER_PW: return msg('パスワードが違います')
    # 全データをデータベースから取り出して表示する
    return render_template('admin_list.html', 
                        files=fs_data.get_all(), pw=MASTER_PW)

@app.route('/admin/remove/<id>') # アクセスするURLを指定する
def admin_remove(id):
    # マスターパスワードのチェックしてファイルとデータを削除する
    if request.args.get('pw', '') != MASTER_PW: return msg('パスワードが違います')
    fs_data.remove_data(id)
    return msg('削除しました')

# テンプレートを利用してエラー画面を表示する
def msg(s):
    return render_template('error.html', message=s)

# 日時フォーマットを簡易表示するフィルター設定
def filter_datetime(tm):
    return time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(tm))
# フィルターをテンプレートエンジンに登録する
app.jinja_env.filters['datetime'] = filter_datetime

# 実行する
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # デバッグモードを有効にして実行する
