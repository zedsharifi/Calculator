def welcome():
    print("Welcome to my calculator")


def calculate():
    operation=input('''
    please type a operation that you want :
    + for addition
    - for subtraction
    * for multiplication
    / for division
''' )

    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    try:
        if operation == '+':
            print('{} + {} ='.format(num1, num2), num1+num2)

        elif operation == '-':
            print('{} - {} ='.format(num1, num2), num1-num2)

        elif operation == '*':
            print('{} * {} ='.format(num1, num2), num1*num2)

        elif operation == '/':
            print('{} / {} ='.format(num1, num2), num1/num2)

        else:
            print("operation not found!")
            again()

    except ZeroDivisionError:
        print("division by zero!")
        again()
    again()

def again():
    repeat=input('''
    Do you want to calculate again ?
    if your answer is yes please type Y
    and if no please type N
    ''')

    if repeat.upper()=='Y' :
        calculate()
    else:
        print("See you later, goodbye!")

welcome()
calculate()