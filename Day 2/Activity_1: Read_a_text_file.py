with open("notes.txt", "w") as file:
    file.write("Remember to review the project proposal by Friday.\n")
    file.write("Schedule a meeting with the design team next week.\n")
    file.write("Update the budget spreadsheet with the latest figures.\n")

with open("notes.txt", "r") as file:
    print(file.read())