# ファイルとデータベースの操作を行うモジュール
from tinydb import TinyDB, where # データベース操作用モジュール
import uuid, time, os # UUIDと時間とOSをインポートする

# パスの指定
BASE_DIR = os.path.dirname(__file__) # このファイルのあるディレクトリを取得
FILES_DIR = BASE_DIR + '/files/' # このファイルのあるディレクトリにfiles/を指定
DATA_FILE = BASE_DIR + '/data/data.json' # このファイルのあるディレクトリにdata/data.jsonを指定

# アップロードされたファイルとメタ情報の保存
def save_file(upfile, meta):
    # UUIDを生成する
    id = 'FS' + uuid.uuid4().hex # ランダムな文字列を生成する
    # アップロードされたファイルを保存する
    upfile.save(FILES_DIR + '/' + id)
    # メタデータをDBに保存する
    db = TinyDB(DATA_FILE) # データベースを開く
    meta['id'] = id # IDを追加する
    # 期限を計算
    term = meta['limit'] * 24 * 60 * 60 # 期限を秒に変換
    meta['time_limit'] = time.time() + term # 現在時刻に期限を加算
    # 情報をデータベースに挿入
    db.insert(meta)
    return id # IDを返す

# データベースから任意のIDのデータを取得する
def get_data(id):
    db = TinyDB(DATA_FILE) # データベースを開く
    f = db.get(where('id') == id) # IDが一致するデータを取得
    if f is not None:
        f['path'] = FILES_DIR + '/' + id
    return f # データを返す

# データを更新する
def set_data(id, meta):
    db = TinyDB(DATA_FILE) # データベースを開く
    db.update(meta, where('id') == id) # IDが一致するデータを更新

#全てのデータを取得する
def get_all():
        db = TinyDB(DATA_FILE) # データベースを開く
        return db.all()
    
# アップロードされたファイルとメタ情報の削除
def remove_data(id):
    # ファイルを削除する
    path = FILES_DIR + '/' + id # ファイルのパスを取得
    os.remove(path) # ファイルを削除
    # データベースから削除する
    db = TinyDB(DATA_FILE) # データベースを開く
    db.remove(where('id') == id) # IDが一致するデータを削除
    

