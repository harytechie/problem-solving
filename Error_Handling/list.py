try:
    num=[12,23,34,12,34,12,34,12,34]
    ind=int(input("Enter a number : "))
    print(num[ind])
except ValueError:
    print("please enter a number")
except IndexError:
    print("Invalid index")