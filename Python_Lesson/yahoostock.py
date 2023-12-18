from yahoo_finance_api2 import share # 株価データの取得ライブラリ
from yahoo_finance_api2.exceptions import YahooFinanceError # 株価データの取得ライブラリ
import pandas as pd # 行列計算のライブラリ

code = 3323 #ターゲット
S_year = 10 #何年前から
S_day = 1 #何日前まで

# 目的変数を作成する
def kabuka(): # 株価データの取得
    company_code = str(code) + '.T' # 企業コード
    my_share = share.Share(company_code) # 株価データの取得
    symbol_data = None # 株価データの取得

    try: # 株価データの取得
        symbol_data = my_share.get_historical(share.PERIOD_TYPE_YEAR, 
                                            S_year,
                                            share.FREQUENCY_TYPE_DAY,
                                            S_day)
    except YahooFinanceError as e:
        print(e.message)
        sys.exit(1)
    # 株価をデータフレームに入れている
    df_base = pd.DataFrame(symbol_data)
    df_base = pd.DataFrame(symbol_data.values(), index=symbol_data.keys()).T
    df_base.timestamp = pd.to_datetime(df_base.timestamp, unit='ms')
    df_base.index = pd.DatetimeIndex(df_base.timestamp, name='timestamp').tz_localize('UTC').tz_convert('Asia/Tokyo')
    #df_base = df_base.drop(['timestamp', 'open', 'high', 'low', 'volume'], axis=1)
    
    #df_base = df_base.rename(columns={'close':company_code + '対象'})
    #df_base = df_base[:-1] #一番最後の行を削除
    df_base = df_base.reset_index(drop=True)
    
    
    return company_code, df_base

result = kabuka()
print(str(result[0]), result[1].shape)

# データフレームへもどす
df_base = result[1]

df_base.head()
