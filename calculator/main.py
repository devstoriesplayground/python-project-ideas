def arithmetic_option(option, first_, second_):
    if 'A' in option or 'a' in option:
        total = int(first_) + int(second_)
        return total, "+"
    elif 'S' in option or 's' in option:
        total = int(first_) - int(second_)
        return total, "-"
    elif 'M' in option or 'm' in option:
        total = int(first_) * int(second_)
        return total, "*"
    elif 'D' in option or 'd' in option:
        total = int(first_) / int(second_)
        return total, "/"


def add(n, m):
    return n + m


def subs(n, m):
    return n - m


def prod(n, m):
    return n * m


def div(m, n):
    return m / n


def main():
    global total
    a = True
    while a:
        print("WELCOME TO DEVSTORIES PLAYGROUND")
        print("***** M E N U ******")
        print("[B] BASIC CALCULATOR")
        print("[E] EXIT")
        user_menu_choice = input('Choose your menu option: ')
        if user_menu_choice == "B":
            print("Press following keys to use the calculator")
            print("[A] Addition")
            print("[S] Subtraction")
            print("[M] Multiplication")
            print("[D] Division")
            user_choice = input("Enter your arithmetic: ")
            first_ = input("Enter first number: ")
            second_ = input("Enter second number: ")

            match user_choice:
                case "A":
                    total = add(int(first_), int(second_))
                case "S":
                    total = subs(int(first_), int(second_))
                case "M":
                    total = prod(int(first_), int(second_))
                case "D":
                    total = div(int(first_), int(second_))
                case _:
                    print("Invalid arithmetic option!")
                    continue

            # total, user_choice = arithmetic_option(user_choice, first_, second_)
            print(f"TOTAL COMPUTATION: {total}")
            print("\n")
        elif user_menu_choice == "E":
            print("THANK YOU FOR USING THE BASIC CALCULATOR - DEVSTORIES PLAYGROUND")
            break


if __name__ == "__main__":
    main()

