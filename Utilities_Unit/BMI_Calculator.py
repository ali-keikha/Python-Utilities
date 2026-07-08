def calculate_bmi(Weight: float, Height: float):   #weight = Kg
                                                   #height = Meter
    bmi = Weight / (Height ** 2)

    healty_weight_max = (Height ** 2) * 25
    healty_weight_min =(Height ** 2) * 18.5

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

    return bmi, category, healty_weight_max, healty_weight_min
    

def main():
    while True:
        user_choose = int(input("Select Option:\n"
                                "1) BMI Calculate\n"
                                "2) Exit"))
        
        if user_choose == 1:
            user_weight = float(input("Enter your Weight(Kg):\n"))
            user_height = float(input("Enter your Height(Meter):\n"))

            bmi, category, healthy_weight_max, healthy_weight_min = calculate_bmi(user_weight, user_height)    
        
            print(f"BMI: {bmi:.2f}")
            print(f"Category: {category}")
            print("healty BMI range is 18.5-24.9")
            print(f"healty max weight for your height is: {healthy_weight_max:.2f} Kg")
            print(f"healty min weight for your height is: {healthy_weight_min:.2f} Kg")
        
        else:
            break