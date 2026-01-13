student = {
    "name": "Naledi Mankgogele-Motswiane",
    "course": "100 Days of Code - AI Challenge",
    "progress": {
        "days_completed": 0,
        "current_day": 1
    }
}

student["progress"]["days_completed"] += 1
student["progress"]["current_day"] += 1
print(f"{student['name']} has completed {student['progress']['days_completed']} days in the {student['course']}. Currently on day {student['progress']['current_day']}.")