import json

with open("tmp2.text", "r", encoding="utf-8") as f:
    # 序列化

    cookies = json.load(f)
    print(f.read())

for i in cookies:
    print(i)
