import random
secret_number=random.randint(1,10)
while True:
    your_guess=input("Enter your guess: ")
    guess=int(your_guess)
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed it!")
        break
