import random

choices = list(range(100))

while True:
    number = random.choice(choices)
    print('================================================')
    guess = int(input("New Guess Please\n"))
    while True:
        if number == guess:
            print("correct\n")
            break
        elif number > guess:
            guess = int(input('guess greater\n'))
        else:
            guess = int(input('guess lower\n'))
