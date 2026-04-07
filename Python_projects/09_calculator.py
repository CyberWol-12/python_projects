from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

function = {
    "+": add,
    "-": sub,
    "*": multi,
    "/":divide
}


def calculator():
    should_accumulate = True
    first_number = float(input("Type your first number:"))
    while should_accumulate:
        for symbol in function:
            print(symbol)
        math_operation = input("Type function:")
        second_number = float(input("Type second Number:"))
        answer = function[math_operation](first_number,second_number)
        print(f"{first_number} {math_operation} {second_number} = {answer }")

        user_ask = input("you want to continue?Type 'yes' or 'no'.")
        if user_ask == 'yes':
                num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()