# 株価予想
import datetime # 日付関連のライブラリ

import matplotlib # グラフ描画のライブラリ
import matplotlib.pyplot as plt # グラフ描画のライブラリ
import numpy as np # 行列計算のライブラリ
import pandas_datareader # 株価データの取得ライブラリ
import sklearn # 機械学習ライブラリ
import sklearn.linear_model # 線形回帰モデルのライブラリ
import sklearn.model_selection # モデル検証のライブラリ

# データの取得
df_aapl = pandas_datareader.data.DataReader('AAPL', 'yahoo', '2014/1/1')

