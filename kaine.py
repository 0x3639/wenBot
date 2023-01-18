import csv
import random

# with open('kaine.csv', 'r') as csv_file:
#     #csv_reader = csv.reader(csv_file, delimiter=',')
#     csv_reader = csv.reader(csv_file)
#     print("I am here")
#     row_number = random.randint(0,len(list(csv_reader))-1)
#     print (row_number)

    # for index, row in enumerate(csv_reader):
    #     if index == row_number:
    #         await ctx.send(row[1])

with open('kaine.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    random_row = random.choice(list(data))
    print(random_row[0])