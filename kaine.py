import csv
import random

with open('kaine.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    random_row = random.choice(list(data))
    print(random_row[0])