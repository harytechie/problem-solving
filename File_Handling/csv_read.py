import csv

with open("D:\py class\File_Handling\username.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(row)