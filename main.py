logo = """
 _____________________
|  _________________  |
| | 00000000000000. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
print("Welcome to the calculator")


def Addition(x, y):
    result = x + y
    return result


def Subtraction(y, x):
    result = (y - x)
    return result


def Multiplication(x, y):
    result = x * y
    return result


def Division(x, y):
    result = x / y
    return result


def Exponent(x, y):
    result = x ** y
    return result


operators = {"+": Addition, "-": Subtraction, "*": Multiplication, "/": Division, "^": Exponent, }
opr_names = ["Addition", "Subtraction", "Multiplication", "Division", "Exponent"]

def calculator():
    A = float(input("Enter the first number: "))
    continue_calculations = True
    n=0
    for opr in operators:
        print(f"{opr} for {opr_names[n]}.")
        n += 1
    while continue_calculations == True:

        selected_opr = input("Select the required operation from the list above:\n")

        B = float(input("Enter the other number: "))

        calculation_function = operators[selected_opr]
        answer = calculation_function(A, B)

        print(f"{A} {selected_opr} {B} = {answer}")

        more = input(
            "Type 'y' to continue calculation using the previous answer or type 'z' to start fresh calculation. Type 'n' to exit the calculator: ")
        if more == "y":
            A = answer
        elif more == "z":
            continue_calculations = False
            calculator()
        else:
            print("Thank you for using calculator. Good Bye!")
            continue_calculations = False


calculator()

