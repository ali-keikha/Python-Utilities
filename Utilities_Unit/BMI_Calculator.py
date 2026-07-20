def calculate_bmi(weight: float, height: float):   #weight = Kg
                                                   #height = Meter
    bmi = weight / (height ** 2)

    healthy_weight_max = (height ** 2) * 25
    healthy_weight_min = (height ** 2) * 18.5

    if bmi < 16:
        category = "Severe Thinness"

    elif bmi < 17:
        category = "Moderate Thinness"

    elif bmi < 18.5:
        category = "Mild Thinness"

    elif bmi < 25:
        category = "Normal Weight"

    elif bmi < 30:
        category = "Overweight"

    elif bmi < 35:
        category = "Obesity Class I"

    elif bmi < 40:
        category = "Obesity Class II"

    else:
        category = "Obesity Class III"

    return bmi, category, healthy_weight_max, healthy_weight_min
    

def main():
    while True:
        while True:
            try:
                user_choose = int(input("Select Option:\n"
                                    "1) BMI Calculate\n"
                                    "2) Exit\n"))
                
                if not 1 <= user_choose <= 2:
                    print("Please enter a number between 1 and 2")
                    continue
                
                break

            except ValueError:
                print("Please enter a valid number")
            
        
        if user_choose == 1:
            while True:
                try:
                    user_weight = float(input("Enter your Weight(Kg):\n"))

                    if user_weight <= 0 :
                        print("Weight must be greater than zero")
                        continue
                    
                    user_height = float(input("Enter your Height(Meter):\n"))

                    if user_height <= 0 :
                        print("Height must be greater than zero")
                        continue

                    break

                except ValueError:
                    print("Please enter a valid number")

            bmi, category, healthy_weight_max, healthy_weight_min = calculate_bmi(user_weight, user_height)    
        
            print(f"BMI: {bmi:.2f}")
            print(f"Category: {category}")
            print("healthy BMI range is 18.5-24.9")
            print(f"healthy max weight for your height is: {healthy_weight_max:.2f} Kg")
            print(f"healthy min weight for your height is: {healthy_weight_min:.2f} Kg")
        
        else:
            break

if __name__ == "__main__":
    main()