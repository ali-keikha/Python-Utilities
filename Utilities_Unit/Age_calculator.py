from datetime import datetime

def calculate_age():
    
    birthday = input("Enter your birthday (YYYY-MM-DD): ")
    birthday = datetime.strptime(birthday, "%Y-%m-%d").date()

    today_date = datetime.today().date()

    age = today_date.year - birthday.year

    if (today_date.month, today_date.day) < (birthday.month, birthday.day):
        age -= 1

    return age

def main():

    while True:
        user_choose = int(input("Choose option : \n"
            "1) Age calculate\n" \
            "2) Exit\n"))

        if user_choose == 1:
            age = calculate_age()
            print(f"your age is {age} years")
        
        else:
            break

if __name__ == "__main__":
    main()