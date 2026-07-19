def get_number():
    while True:
        try:
            number = float(input("Enter Number:\n"))
            break
        except ValueError:
            print("Enter Number")
    
    return number

def factorial(fact_num):
    result = 1
    for i in range(1, fact_num + 1):
        result *= i

    return result


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
            if not 1 <= operator <= 9:
                print("Please enter a number between 1 and 9")

            else:
                break
            
        except ValueError:
            print("Please enter a valid number")
        
    if operator == 9:
        return None
    
    if operator in (1, 2, 3, 4, 5, 8):

        number = get_number()

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
            
            elif first_number.is_integer():
                result = factorial(int(first_number))
        
            else:
                print("Factorial is only defined for integers")
                return first_number
    return result


def main():

    f_number = get_number()

    while True:
        result = set_number(f_number)
        
        if result is None:
            break
    
        f_number = result

        print(f"your answer is : {result}")
    
if __name__ == "__main__":
    main()
