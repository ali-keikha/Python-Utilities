def word_couner(sentence: str):

    word_list = sentence.split(" ")
    word_num = len(word_list)

    return word_num

def alphabet_counter(sentence: str):

    counter = 0
    for letter in sentence:
        if letter not in (" ", "  ", "   ", "    "):
            counter = counter + 1

    return counter

def main():

    while True:

        user_option = int(input("Select option:\n"
                                "1) Word Counte in sentence\n"
                                "2) Alphabet Counter in sentence\n" \
                                "3) Exit\n"))

        if user_option == 1:

            user_text = input("Write Text\n")
            print(word_couner(user_text))

        elif user_option == 2:
            user_text = input("Write Text\n")
            print(alphabet_counter(user_text))

        else:
            break


if __name__ == "__main__":
    main()

