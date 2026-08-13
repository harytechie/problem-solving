def main():
    print("wlcome to ATM")
    acc_bal=2000
    try:
        user_input = input("Enter a Pin: ")
        correct_password = "1234"
        
        if user_input == correct_password:
            print("Welcome")
            option=int(input("press '1' withdraw if press '2' deposit "))
            if(option==1):
                w_d=int(input("Enter amount : "))
                result1=acc_bal-w_d
                print("successfully withdraw")
                print("balance : ",result1)
            if(option==2):
                w_d=int(input("Enter amount : "))
                result2=acc_bal+w_d
                print("successfully deposit")
                print("balance : ",result2)            
        else:
            raise ValueError("Incorrect password")

    except ValueError:
       print("Pin number wrong. Please try again")
       print()
       main()
main()




