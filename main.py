import random

elements = ["rock", "paper", "scissors"]

print("Let's go to war!!!")

user1 = input("What's your weapon? Rock, Paper or Scissors ")
user2 = random.choice(elements)

print(user1, user2)

if user1 == "rock" and user2 == "scissors":
    print("You win!")
elif user1 == "scissors" and user2 == "paper":
    print("You win!")
elif user1 == "paper" and user2 == "rock":
    print("You win!")
elif user1 == user2:
    print("It's draw!!")
else:
    print("You lose")

