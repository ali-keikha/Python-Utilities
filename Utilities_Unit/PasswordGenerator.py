from random import randint

def Generator(password_len):

    characters = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',

    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',

    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
    '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
    '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
    '}', '~'
    ]

    password = ""

    for _ in range(1, password_len + 1):
        chr_len = randint(0, len(characters) - 1)
        password = password + characters[chr_len]

    return password

def main():

    try:
        pass_length = int(input("Choose your password length: \n"))

    except ValueError:
        print("Please enter valid number")
    
    password = Generator(pass_length)

    print(f"Your Password Generate!:\n {password}")

if __name__ == "__main__":
    main()
