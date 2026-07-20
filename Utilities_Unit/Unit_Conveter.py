def get_number():
    while True:
        try:
            number = float(input("Enter unit Number:\n"))
            break

        except ValueError:
            print("Please enter a valid number")

    return number


def length(value : float):
    unit = {1 : 1,              #Meter
            2 : 1000,           #Kilometer
            3 : 1/100,          #Centimeter
            4 : 254/10000,      #Inch
            5 : 3048/10000,     #Foot
            6 : 9144/10000,     #Yard
            7 : 1609/344        #Mile
        }     
    
    while True:
        try:
            unit_choose = int(input("choose unit:\n"
                            "1) Meter\n"
                            "2) Kilometer\n"
                            "3) Centimeter\n"
                            "4) Inch\n"
                            "5) Foot\n"
                            "6) Yard\n"
                            "7) Mile\n"))

            if not 1 <= unit_choose <= 7:
                print("Please enter a number between 1 and 7")
                continue
            break

        except ValueError:
            print("Please enter a valid number")

    convert_basic_unit = value * unit[unit_choose]    #convert all units to meter(basic unit)
    
    while True:
        try:
            unit_for_convert = int(input("choose unit to convert:\n"
                            "1) Meter\n"
                            "2) Kilometer\n"
                            "3) Centimeter\n"
                            "4) Inch\n"
                            "5) Foot\n"
                            "6) Yard\n"
                            "7) mile\n"))
            
            if not 1 <= unit_for_convert <= 7:
                print("Please enter a number between 1 and 7")
                continue
            break

        except ValueError:
            print("Please enter a valid number")
    
    convert = convert_basic_unit / unit[unit_for_convert]   #convert to user unit

    return convert

def weight(value : float):
    units = {
            1: 1,                # Kilogram
            2: 0.001,            # Gram
            3: 0.000001,         # Milligram
            4: 1000,             # Metric Ton
            5: 0.45359237,       # Pound
            6: 0.028349523125    # Ounce
    }

    while True:
        try:
            unit_choose = int(input("choose unit:\n"
                            "1) Kilogram\n"
                            "2) Gram\n"
                            "3) Milligram\n"
                            "4) Metric Ton\n"
                            "5) pound\n"
                            "6) Ounce\n"))
            
            if not 1 <= unit_choose <= 6:
                print("Please enter a number between 1 and 6")
                continue

            break

        except ValueError:
            print("Please enter a valid number")
    
    while True:
        try:
    
            unit_for_convert = int(input("choose unit:\n"
                            "1) Kilogram\n"
                            "2) Gram\n"
                            "3) Milligram\n"
                            "4) Metric Ton\n"
                            "5) pound\n"
                            "6) Ounce\n"))
            
            if not 1 <= unit_for_convert <= 6:
                print("Please enter a number between 1 and 6")
                continue

            break

        except ValueError:
            print("Please enter a valid number")
    
    convert_basic = value * units[unit_choose]  #convert to kilogram
    convert = convert_basic / units[unit_for_convert]

    return convert

def temperature(value : float):
    
    while True:
        try:
            unit_choose = int(input("Select Temperature Unit:\n"    #unit for value
                                    "1) kelvin\n"
                                    "2) fahrenheit\n"
                                    "3) celsius\n"))
            
            if not 1 <= unit_choose <= 3:
                print("Please enter a number between 1 and 3")
                continue

            break

        except ValueError:
            print("Please enter a valid number")
            
    if unit_choose == 1:
        basic_unit = value - 273.15              #basic unit is celsius
    elif unit_choose == 2:
        basic_unit = (value - 32) * (5 / 9)
    else:
        basic_unit = value

    while True:
        try:
            unit_for_convert = int(input("Select Temperature Unit to convert:\n"    #unit for value
                                 "1) kelvin\n"
                                 "2) fahrenheit\n"
                                 "3) celsius\n"))
            
            if not 1 <= unit_for_convert <= 3:
                print("Please enter a number between 1 and 3")
                continue

            break

        except ValueError:
            print("Please enter a valid number")
    
    if unit_for_convert == 1:
        convert = basic_unit + 273.15
    elif unit_for_convert == 2:
        convert = (basic_unit * 9 / 5) + 32
    else:
        convert = basic_unit

    return convert

def main():
    while True:
        while True:
            try:
                user_choose = int(input("Select Option :\n"
                                "1) Length Unit Converter\n"
                                "2) Weight Unit Converter\n"
                                "3) Temperature Unit Converter\n"
                                "4) Exit\n"))
                if not 1 <= user_choose <= 4:
                    print("Please enter a number between 1 and 4")
                    continue
                break

            except ValueError:
                print("Please enter a valid number")
        if user_choose == 1:
            
            unit_value = get_number()
            l_unit = length(unit_value)
            print(l_unit)
        elif user_choose == 2:
            unit_value = get_number()
            w_uint = weight(unit_value)
            print(w_uint)
        elif user_choose == 3:
            unit_value = get_number()
            t_unit = temperature(unit_value)
            print(t_unit)
        else:
            break

if __name__ == "__main__":
    main()

