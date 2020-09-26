import random

def start():
    num = random.randrange(10) + 1
    
    print("I'm thinking of a number between 1 and 10.")
    guess = int(input("What is your guess?"))
    
    while guess < 1 or guess > 10:
        print("That number is not in range!")
        guess = int(input("What is your guess?"))
        
    
    if guess == num:
        print("You guessed it!")
    else:
        print("Nope. That wasn't it. I was thinking of", num)
        
if __name__ == "__main__":
    start()