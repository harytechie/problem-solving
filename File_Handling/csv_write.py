import csv
new_row = ["vicky", "6094", "haran", "hary"]
with open("File_Handling/username.csv", "a", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(new_row)
print("Successfully appended Alex Miller to your CSV file!")

with open("File_Handling/username.csv","r")as file:
    reader=csv.reader(file,delimiter=";")

    for row in reader:
        print (row)