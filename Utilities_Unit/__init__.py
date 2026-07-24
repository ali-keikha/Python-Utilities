import PasswordGenerator
import Calculator
import Unit_Conveter
import BMI_Calculator
import File_Organizer
import word_alphabet_counter
import File_Duplicate
import Age_calculator

while True:
    
    while True:
        
        try:
            print("-" * 80)
            print("Utilities".center(70))
            print("-" * 80)
            user_choice = int(input("Choose option\n"
                            "1) Password Generate\n"
                            "2) Calculator\n"
                            "3) Unit Converter\n"
                            "4) Bmi calculator\n"
                            "5) File Organizer\n"
                            "6) Word and Alphabet Counter\n"
                            "7) File Duplicate\n"
                            "8) Age Calculator\n"
                            "9) Exit\n"))
            
            if user_choice not in range(1,10):
                print("Enter Number between 1-9")
            else:
                break
        
        except ValueError :
            print("Enter Number")
    
    if user_choice == 1:
        PasswordGenerator.main()
    elif user_choice == 2:
        Calculator.main()
    elif user_choice == 3:
        Unit_Conveter.main()
    elif user_choice == 4:
        BMI_Calculator.main()
    elif user_choice == 5:
        File_Organizer.main()
    elif user_choice == 6:
        word_alphabet_counter.main()
    elif user_choice == 7:
        File_Duplicate.main()
    elif user_choice == 8:
        Age_calculator.main()
    else:
        break

print("good bye!!")
    


