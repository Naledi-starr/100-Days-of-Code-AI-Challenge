import json

user = {
    "name": "Naledi",
    "day" : 2,
    "topic": "File Handling + JSON",
    "completed": True
}
    
with open("progress.json", "r") as file:
    data = json.load(file)

data["confidence_level"] = 4

with open("progress.json", "w") as file:
    json.dump(data, file, index =4)    