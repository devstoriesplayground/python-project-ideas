import random
import string


def ascii_letters_character():
    print(string.ascii_letters)
    return string.ascii_letters


def ascii_lowercase_character():
    return string.ascii_lowercase


def ascii_uppercase_character():
    return string.ascii_uppercase


def digits():
    return string.digits


def hexdigits():
    return string.hexdigits


def octdigits():
    return string.octdigits


def punctuation():
    return string.punctuation


def main():
    print("WELCOME TO DEVSTORIES PLAYGROUND")
    print("----- PASSWORD GENERATOR -----")
    try:
        character_list = []
        user_password_length = int(input("PASSWORD LENGTH: "))
        while True:
            print("CHOOSE YOUR COMBINATION SET:")
            print("[1] ASCII LETTERS")
            print("[2] ASCII LOWERCASE")
            print("[3] ASCII UPPERCASE")
            print("[4] DIGITS")
            print("[5] OCTDIGITS")
            print("[6] PUNCTUATION")
            print("[7] EXIT")
            user_combination_choice = int(input('ENTER YOUR CHOICE: '))

            match user_combination_choice:
                case 1:
                    string_combination = string.ascii_letters
                    character_list.append(string_combination)
                case 2:
                    string_combination = string.ascii_lowercase
                    character_list.append(string_combination)
                case 3:
                    string_combination = string.ascii_uppercase
                    character_list.append(string_combination)
                case 4:
                    string_combination = string.digits
                    character_list.append(string_combination)
                case 5:
                    string_combination = string.octdigits
                    character_list.append(string_combination)
                case 6:
                    string_combination = string.punctuation
                    character_list.append(string_combination)
                case 7:
                    break
                case _:
                    print("Invalid option! Try Again...")
                    continue

        password = ""
        for index in range(user_password_length):
            password = password + random.choice("".join(character_list))
        print(password)

    except Exception as ex:
        print(f"ERROR ENCOUNTERED: {ex}")


if __name__ == "__main__":
    main()
