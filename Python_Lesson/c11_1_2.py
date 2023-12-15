import json

j = {
    "employees": [
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"},
]
}


with open("test.json", "w") as f :
    json.dump(j, f) # jsonnをファイルに書き込む
