from wonderwords import RandomSentence, RandomWord
import requests

def main():
    import random


    loop = 1

    while loop < 100:
        print("----------------WELCOME TO DEVSTORIES PLAYGROUND--------------------------")
        # All the questions that the program asks the user
        first_noun = input("Choose a noun: ")
        plural_noun = input("Choose a plural noun: ")
        second_noun = input("Choose a noun: ")
        name_of_place = input("Name a place: ")
        adjective = input("Choose an adjective (Describing word): ")
        third_noun = input("Choose a noun: ")

        # Displays the story based on the users input
        print("The story goes ...")
        print(f"I had lunch with a {first_noun} in my car because I'm NOT crazy.")
        print(f"I {plural_noun} at a baseball bat in your bathroom because I'm cool like that")
        print(f"{second_noun} kicked a squirrel at the {name_of_place} because {first_noun} told me to.")
        print(f"{third_noun} danced {adjective} with my sister in Church because Daddy would like some sausages.")
        print("Well. add is done.")
        print("------------------------------------------")

        # Loop back to "loop = 1"
        loop = loop + 1


if __name__ == "__main__":
    main()

