import sys
import calendar

lines = [
    "Monday and Monday's child is fair of face.",
    "Tuesday and Tuesday's child is full of grace.",
    "Wednesday and Wednesday's child is full of woe.",
    "Thursday and Thursday's child has far to go.",
    "Friday and Friday's child is loving and giving.",
    "Saturday and Saturday's child works hard for a living.",
    "Sunday and Sunday's child is fair and wise and good in every way."
]

dob = sys.stdin.readline()
while dob != "":
    dob = dob.split()
    print("You were born on a", lines[calendar.weekday(int(dob[2]), int(dob[1]), int(dob[0]))])
    dob = sys.stdin.readline()