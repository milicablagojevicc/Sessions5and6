# Virtual dice game
# You win if you roll a 6
#You have 3 lives
from random import randint

lives = 3
while lives > 0:
    dice_roll = randint(1, 6)
    if dice_roll == 6:
        print ("Congrats! You Win")
        break
    else:
        lives = lives - 1 #you lose a life
        print(f" You got a {dice_roll}. You lose a life. Lives left: {lives}")
else:
            print("You lose!")