class Bank:
    def __init__(self):
        self.__bal = 1000

    def get_bal(self):
        return self.__bal

b = Bank()

print(b.get_bal())  # Output: 1000
