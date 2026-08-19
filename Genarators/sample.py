def count_up_to(limit):
    current = 1
    while current <= limit:
        yield current  
        current += 1

counter = count_up_to(3)

print(next(counter))  
print(next(counter))  
print(next(counter))  
