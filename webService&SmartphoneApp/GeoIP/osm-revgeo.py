import geocoder

# 経度緯度を指定
pos = (35.659025, 139.745025)
# OpenStreetMapの逆ジオコーディング
g = geocoder.osm(pos, method='reverse') # method='reverse'を指定
# 結果表示
print('Country:', g.country) # 国名
print('State:', g.state) # 都道府県名
print('City:', g.city) # 市区町村名
print('Street:', g.street) # 丁目/番地
