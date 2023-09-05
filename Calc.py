


def Calculator():
    operations = ['+', '-', '/', '*']
    choice = input('Input "+" for addition, "-" for subtraction, "/" for division or "*" for multiplication ')
    num1 = float(input("input first number "))
    num2 = float(input("input second number "))
    if choice == operations[0]:
        ans = num1 + num2 
        print(f"the sum of {num1} and {num2} is {ans}")
    elif choice == operations[1]:
        ans = num1 - num2
        print(f"the difference of {num1} and {num2} is {ans}")
    elif choice == operations[2]:
        ans = num1 / num2 
        print(f"the division of {num1} and {num2} is {ans}")
    elif choice == operations[3]:
        ans = num1 * num2
        print(f"the multiplication of {num1} and {num2} is {ans}")
    else:
        print("That is not a valid operator")

    return CalcAgain()
    


def CalcAgain():
        check = input('Do you want to perform another calculation type "y" to continue ')
        if check.upper() == 'Y':
            Calculator()
        else:
            print("calulation completed")



Calculator()
