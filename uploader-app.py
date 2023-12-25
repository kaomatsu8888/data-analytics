# 画像をアップロードするwebアプリケーション
from flask import Flask, request, redirect # Flaskクラスをインポート
from datetime import datetime # datetimeクラスをインポート
import os # osモジュールをインポート

# 保存先のディレクトリとURLの指定
IMAGES_DIR = "./static/images"
IMAGES_URL = "/static/images"
app = Flask(__name__) # Flaskのクラスのインスタンスを生成

# 画像をアップロードするHTMLを表示する
@app.route('/') # デコレーターを使ってルーティングを指定
def index_page():
    return """
    <html><body>
    <h1>画像をアップロードする</h1>
    <form method="POST" action="/upload" enctype="multipart/form-data">
    <input type="file" name="upfile">
    <input type="submit" value="アップロード">
    </form>
    </body></html>
    """

# 画像をアップロードする
@app.route('/upload', methods=['POST']) # デコレーターを使ってルーティングを指定
def upload():
    # アップされていなければメインページへリダイレクト
    if not ('upfile' in request.files):
        return redirect('/')
    # アップしたファイルのオブジェクトを取得
    temp_file = request.files['upfile']
    # JPEGファイル以外は却下する
    if temp_file.filename == '':
        return redirect('/')
    if not is_jpegfile(temp_file.stream):
        return '<h1>JPEGファイル以外はアップロードできません</h1>'
    # ファイル名を決定する
    time_s = datetime.now().strftime('%Y%m%d%H%M%S')
    fname = time_s + '.jpeg'
    # ディレクトリの存在を確認し、存在しない場合は作成
    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)
    # 一時ファイルを保存先ディレクトリに保存する
    temp_file.save(IMAGES_DIR + '/' + fname)
    # 画像の表示ページへリダイレクトする
    return redirect('/photo/' + fname)

@app.route('/photo/<fname>') # デコレーターを使ってルーティングを指定
def photo_page(fname):
    # 画像ファイルがあるか確認する
    if fname is None: return redirect('/')
    image_path = IMAGES_DIR + '/' + fname
    image_url = IMAGES_URL + '/' + fname
    if not os.path.exists(image_path): return '<h1>画像がありません</h1>'
    # 画像を表示する
    return """
    <h1>画像がアップロードされています</h1>
    <p>URL: {0}<br>
file: {1}</p>
    <img src="{0}" width="400">
    """.format(image_url, image_path)

# JPEGファイルかどうかを判定する
def is_jpegfile(fp):
    byte = fp.read(2)
    fp.seek(0)
    return byte[:2] == b'\xff\xd8'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
