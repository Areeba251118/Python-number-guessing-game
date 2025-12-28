import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1

    if guess > secret:
        print("Too High!")
    elif guess < secret:
        print("Too Low!")
    else:
        print("Correct 🎉")
        print("You guessed in", attempts, "attempts")
        break
