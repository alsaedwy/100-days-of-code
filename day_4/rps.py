import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


options_list = [rock, paper, scissors]

your_choice = int(input("Choose 1 for rock, 2 for paper, 3 for scissors\n"))

print(options_list[your_choice-1])

computer_choice = random.choice(options_list)

print(computer_choice)

if your_choice == rock and computer_choice == paper:
  print("Computer wins!")

if your_choice == paper and computer_choice == scissors:
  print("Computer wins!")

if your_choice == scissors and computer_choice == rock:
  print("Computer wins!")

if your_choice == scissors and computer_choice == paper:
  print("You win!")

if your_choice == rock and computer_choice == scissors:
  print("You win!")

if your_choice == paper and computer_choice == rock:
  print("You win!")

else:
  print("It's a draw!")

