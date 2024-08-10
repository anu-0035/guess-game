# guess-game
#a script that generates a random number between a fixed range, and  if the user guesses the number right in three chances, then user wins otherwise user lose. This game user can play as many numbers of times and whenever user wins a score is to be given to the user.
print("""This is a game where the user enter the strating and ending range. 
Both student and computer guesses a number in that given range.
If the user guess the same number in the 3 attempt then u won otherwise be a losser""")

import random

def guess():
    for i in range(3):
        if i==0:
            a=int(input("enter  your 1st guess: "))
            if a==x:
                print("Congrat's u have guessed the right number","score: 100")
                break
            else:
                print("have 2 more try")
        elif i==1:
            a=int(input("enter your 2nd guess: "))
            if a==x:
                print("Congrat's u have guessed the right number","score: 75")
                break
            else:
                print("have one more try")
        elif i==2:
            a=int(input("enter your 3rd guess: "))
            if a==x:
                print("Congrat's u have guessed the right number","score=50")
                break
            else:
                print("Better Luck Next Time!","score=00")
                print("the cumputer guessed number is: ",x)
n=1
while n==1:
    a=int(input("enter the starting range: "))
    b=int(input("enter the ending range: "))
    x=random.randint(a,b)
    guess()
    n=int(input("want to play more the enter 1 or enter 0 for exit: "))
