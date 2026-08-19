try:
    fruits = ["apple", "banana"]
    fruit_iterator = iter(fruits)

    print(next(fruit_iterator))  
    print(next(fruit_iterator))
    print(next(fruit_iterator))
    print(next(fruit_iterator))
    print(next(fruit_iterator))
except Exception:
    print("code error")
