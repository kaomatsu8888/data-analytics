# ライブラリの取り込み
import geoip2.database

# 確認したいIPアドレスの指定
check_ip = '157.7.44.174'

# データベースファイルを読み込む
reader = geoip2.database.Reader('GeoLite2-City.mmdb')

# DBを検索
rec = reader.city(check_ip)
# 検索結果を表示
print('IP:', check_ip) # IPアドレス
print('Country:', rec.country.name) # 国名
print('City:', rec.city.name) # 市区町村名
print('Latitude:', rec.location.latitude) # 緯度
print('Longitude:', rec.location.longitude) # 経度
