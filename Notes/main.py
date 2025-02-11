#Matthew McKinley, Reading Files notes

import csv



with open("Notes/Class CSV sample - Sheet1.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        print(f"row {row[0]}, favorite color {row[1]}")

csv_reader = open("Notes/Class CSV sample - Sheet1.csv", "r")