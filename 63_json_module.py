import json

data = '{"var1":"Sufiyaan", "var2":"Harry"}'

parsed = json.loads(data)
print(parsed)
print(parsed["var1"])

data2 = {
    "channelName": "CodeWithHarry",
    "cars": ["bmw", "Audi A8", "Ferrari"],
    "fridge": ("Roti", 540),
    "isBad": False
}

jscomp = json.dumps(data2)
print(jscomp)
