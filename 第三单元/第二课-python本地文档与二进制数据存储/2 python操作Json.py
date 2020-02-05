import json

#dumps --- dict to json
data = {
    'name': 'python',
    'pwd': 123456
}
print(json.dumps(data))

#dump --- 字典写入json文件
with open('dict_to_json.json', 'w') as f:
    json.dump(obj=data, fp=f)

#loads --- json to dict
json_data = '{"name": "python", "pwd": 123456}'
print(json.loads(s=json_data))

#load --- 读取json文件
with open('dict_to_json.json','r') as f:
    res = json.load(f)
    print(res)