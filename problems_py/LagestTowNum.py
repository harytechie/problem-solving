l = [26, 32, 34, 21, 34, 56, 45, 23, 12, 45, 56]
max_num = 0
sec_num = 0

for i in l:
    if i > max_num:
        max_num = i
    elif i > sec_num and i != max_num:
        sec_num = i

print("Largest number:", max_num)
print("Second largest number:", sec_num)
