import os, json, datetime
# 保存先のファイルを指定
BASE_DIR = os.path.dirname(__file__) # このファイルのあるディレクトリを取得
SAVE_FILE = BASE_DIR + '/data/log.json' # このファイルのあるディレクトリにdata/log.jsonを指定

# ログファイル（json形式）を読み出す関数
def load_data():
    if not os.path.exists(SAVE_FILE): # ファイルが存在しない場合
        return []
    with open(SAVE_FILE, 'rt', encoding='utf-8') as f: # ファイルを読み込みモードで開く
        return json.load(f) # json形式で読み込む
    
# ログファイル（json形式）に書き込む関数
def save_data(data_list):
    with open(SAVE_FILE, 'wt', encoding='utf-8') as f:
        json.dump(data_list, f) # json形式で書き込む

# ログを追記保存する関数
def save_data_append(user, text):
    # レコードを用意
    tm = get_datetime_now() # 現在の日時を取得
    data = {'name': user, 'text': text, 'date': tm}
    # 戦闘にレコードを追加
    data_list = load_data() # ログファイルを読み込む
    data_list.insert(0, data) # 先頭に追加
    save_data(data_list) # ログファイルに書き込む

    # 日時を文字列で得る関数
def get_datetime_now():
    now = datetime.datetime.now()
    return "{0:%Y/%m/%d %H:%M:%S}".format(now) # 2020/01/01 12:34:56の形式で返す
