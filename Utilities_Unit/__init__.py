import Calculator
import PasswordGenerator

print("-" * 70)
print("Utilities")
print("-" * 70)

while True:
    user_choose = int(input("Choose option\n"
                            "1) Password Generate\n"
                            "2) Calculator\n"
                            "3) Exit\n"))
    
    if user_choose == 1:
        PasswordGenerator.main
    elif user_choose == 2:
        Calculator.main
    else:
        break

print("good bye!!")
    


