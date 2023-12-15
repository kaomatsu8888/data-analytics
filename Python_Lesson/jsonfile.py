import json

j = {
    "employees": [
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"},
]
}

print(j) #
print("####################")
print(json.dumps(j)) # json.dumps() converts a Python object into a json string
