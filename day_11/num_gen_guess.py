import random
import os

difficulty_dict = {"easy": 10, "hard": 5}

print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")

def game():
    difficulty_number = difficulty_dict[input("'easy' or 'hard").lower()]
    random_num = random.choice(range(0,101))
    
    for i in range(difficulty_number):
        guessed_number = int(input('Select a num: '))
        if guessed_number == random_num:
            print("You win. :)")
            return 
        elif guessed_number > random_num:
            print(f"Too high, you have {difficulty_number-1} trials left.")
            difficulty_number -= 1
        elif guessed_number < random_num:
            print(f"Too low, you have {difficulty_number-1} trials left.")
            difficulty_number -= 1
    print("You lose :)")

game()