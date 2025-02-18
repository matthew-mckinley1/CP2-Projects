
"""
r = read
w = write (won't create a file)
w+ = read and write
a = append (add things but not write over) (will create the file if it isn't there)
x = create a file

"""


"""
with open("Notes\things.txt", "a") as file:
    file.write("\nI just made another line on my file")

with open("Notes\things.txt", "r") as file:
    print(file.read())

"""

import csv

with open("Notes\sample.csv", "r",) as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        print({row[0]:row[1]})