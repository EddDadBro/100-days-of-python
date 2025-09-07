import coin_art
import random

choice = input("Chose Heads or Tails!\n       Your Choice: ").lower()

print("\n       ...and the flip!!!\n")

random_flip = random.randint(0, 1)
if random_flip == 0:
    print("Its Heads!\n")
else:
    print("Its Tails\n")
if random_flip == 0 and choice == "heads":
    print("That's a match, you win!")
elif random_flip == 1 and choice == "tails":
    print("That's a match, you win!")
else:
    print("Whomp Whomp! You lose!")
