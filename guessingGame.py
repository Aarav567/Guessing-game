import random
number = random.randint(1, 9)  # NUMBER ALSO USED IN LINE 7
chances = 5
print("Guess a number(between 1 and 9):")
while chances < 6:
    guess = int(input("Enter Guess-"))
    if(guess == number):
        print("CONGRATULATIONS!! You Win!")
    elif guess < number:
        print("Guess too low ",chances , " chances remain")
    elif guess > number:
        print("Guess too high",chances , " chances remain")
chances = chances -1

if chances == 5:
    print("YOU LOSE. THE NUMBER IS",number)