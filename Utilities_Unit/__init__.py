import PasswordGenerator
import Calculator
import Unit_Conveter
import BMI_Calculator
import File_Organizer
import word_alphabet_counter
import File_Duplicate

print("-" * 80)
print("Utilities".center(70))
print("-" * 80)

while True:
    user_choose = int(input("Choose option\n"
                            "1) Password Generate\n"
                            "2) Calculator\n"
                            "3) Unit Converter\n"
                            "4) Bmi calculator\n"
                            "5) File Organizer\n"
                            "6) Word and Alphabet Counter\n"
                            "7) File Duplicate\n"
                            "8) Exit\n"))
    
    if user_choose == 1:
        PasswordGenerator.main()
    elif user_choose == 2:
        Calculator.main()
    elif user_choose == 3:
        Unit_Conveter.main()
    elif user_choose == 4:
        BMI_Calculator.main()
    elif user_choose == 5:
        File_Organizer.main()
    elif user_choose == 6:
        word_alphabet_counter.main()
    elif user_choose == 7:
        File_Duplicate.main()
    else:
        break

print("good bye!!")
    


