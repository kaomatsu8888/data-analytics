import reverse_geocode

# 調べたい緯度経度を配列で指定
coords = [(35.659025, 139.74505)]
# 逆ジオコーディング
areas = reverse_geocode.search(coords)
# 結果表示
print('Coord:', coords[0]) # 緯度経度
print('Country:', areas[0]['country']) # 国名
print('City:', areas[0]['city']) # 市区町村名
