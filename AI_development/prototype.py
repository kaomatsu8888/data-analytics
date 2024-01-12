import pityna                           # ptnaモジュールのインポート

""" 実行ブロック
"""
def prompt(obj):
    """ ピティナのプロンプトを作る関数
    
        Parameters:
            obj(object): 呼び出し元のPtnaオブジェクト        
        Returns:
            str: ピティナのプロンプト用の文字列
    """
    # 「'Ptnaオブジェクト名:応答オブジェクト名 > '」の文字列を返す
    return obj.get_name() + ':' + obj.get_responder_name() + '> '

# ここからプログラム開始
print('Pityna System prototype : Pityna') # プログラムの情報を表示
pityna = pityna.Pityna('pityna')          # Pitynaオブジェクトを生成

while True:                               # 対話処理開始
    inputs = input(' > ')
    if not inputs:
        print('バイバイ')
        break
    response = pityna.dialogue(inputs)    # 応答文字列を取得
    print(prompt(pityna), response)       # プロンプトと応答文字列をつなげて表示
