import json

data = [True, False, None,'Hola, mundo']
with open("data.json", "w") as f:
    json.dump(data,f)