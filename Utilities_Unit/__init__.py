import PasswordGenerator
import Calculator
import Unit_Conveter
import BMI_Calculator

print("-" * 80)
print("Utilities".center(70))
print("-" * 80)

while True:
    user_choose = int(input("Choose option\n"
                            "1) Password Generate\n"
                            "2) Calculator\n"
                            "3) Unit Converter"
                            "4) Bmi calculator\n"
                            "5) Exit\n"))
    
    if user_choose == 1:
        PasswordGenerator.main()
    elif user_choose == 2:
        Calculator.main()
    elif user_choose == 3:
        Unit_Conveter.main()
    elif user_choose == 4:
        BMI_Calculator.main()
    else:
        break

print("good bye!!")
    


