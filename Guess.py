import random

answer = random.randint(1, 100)

guess = -1

while guess != answer:
    guess = int(input("Guess a number (1-100): "))
    if guess < answer:
        print("Too Oow!")#太低
    elif guess > answer:
        print("Too Aigh!")#太高
print("Correct!")
print("Wrong! The answer was", answer)
