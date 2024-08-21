import random


def main():
    total_chances = 5
    chances = 1
    print("WELCOME TO DEVSTORIES PLAYGROUND")
    print("LET'S PLAY NUMBER GUESSING")
    print("-------------------------")
    counter = True
    while counter:

        try:
            user_lowest_choice = int(input('Enter your lowest number range: '))
            user_highest_choice = int(input('Enter your highest number range: '))
            guess_number = random.randint(user_lowest_choice, user_highest_choice)

            while chances <= total_chances:
                try:
                    user_guess = int(input('Enter your guess number: '))
                    if user_guess > guess_number:
                        total_chances -= 1
                        print(f"You guessed too large! Try again. Remaining chances are {total_chances}")
                        if total_chances == 0:
                            print(f"The mystery number is {guess_number}. Better luck next time!")
                            counter = False
                            break
                        else:
                            continue
                    elif user_guess < guess_number:
                        total_chances -= 1
                        print(f"You guessed too small! Try again. Remaining chances are {total_chances}")
                        if total_chances == 0:
                            print(f"The mystery number is {guess_number}. Better luck next time!")
                            counter = False
                            break
                        else:
                            continue
                    elif guess_number == user_guess:
                        print("Great guess! Congratulation ☺ ")
                        break
                except Exception as e:
                    continue

        except Exception as ex:
            print("Wrong Choice...")
            continue


if __name__ == "__main__":
    main()

