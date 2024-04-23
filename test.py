import json


with open("dump.json", "r") as fp:
    data = json.load(fp)
    
    print(data)
