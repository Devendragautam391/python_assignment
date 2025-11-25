import random
num_dice = int(input("How many dice would you like to roll? "))
total = 0
for number in range(num_dice):
    roll = random.randint(1, 6)
    total += roll
    print("The total sum of the dice rolls is:", total)
