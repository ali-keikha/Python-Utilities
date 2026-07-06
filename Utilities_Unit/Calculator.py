print("*" * 80)
print("Calculator".center(80))
print("*" * 80)

def factorial(fact_num):
    flag_num = 1
    for i in range(1, fact_num + 1):
        flag_num = flag_num * i

    return flag_num


def set_number(first_number : float):
    
    while True:
        try:
            operator = int(input("Choose operator :\n"
                            "1) Addition\n"
                            "2) Subtraction\n"
                            "3) Multiplication\n"
                            "4) Division\n"
                            "5) Power\n"
                            "6) Square Root\n"
                            "7) Factorial\n"
                            "8) Modulo\n"
                            "9) Exit calculator\n"))
            if operator not in range(1,10):
                raise ValueError("choose number between 1-9")
            
            break
            
        except ValueError as e:
            print(e)
        
    if operator == 9:

        return None
    
    if operator in (1, 2, 3, 4, 5, 8):

        number = float(input("Enter number\n"))

        if operator == 1:
            result = (first_number + number)
        elif operator == 2:
            result = (first_number - number)
        elif operator == 3:
            result = (first_number * number)
        elif operator == 4:
            if number == 0:
                print("Cannot divide by zero")
                return first_number
            result = (first_number / number)
        elif operator == 5:
            result = (first_number ** number)
        elif operator == 8:
            if number == 0:
                print("Cannot modulo by zero")
                return first_number
            result = (first_number % number)

    else:
         
        if operator == 6:
            if first_number < 0:
                print("Negative numbers do not have a square root")
                return first_number
            result = (first_number ** 0.5)
        else:
            if first_number < 0:
                print("Negative numbers do not have a factorial")
                return first_number
            result = factorial(int(first_number))
        
    return result


def main():

    f_number = float(input("Enter Number :\n"))

    while True:
        result = set_number(f_number)
        if result == None:
            break
    
        f_number = result

    print(f_number)
    
if __name__ == "__main__":
    main()
