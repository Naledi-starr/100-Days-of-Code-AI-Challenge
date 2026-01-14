import json

new_entry = {
    "day": 2,
    "task": "File handling & JSON",
    "status": "completed"
}

with open("daily_log.json", "a") as file:
    file.write(json.dumps(new_entry) + "\n")

