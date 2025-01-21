# Virtual dice game
# You win if you roll a 6
#You have 3 lives
from random import randint

lives = 3
while True: # sort of infinite loop
    dice_roll = randint(1, 6)
    if dice_roll == 6:
        print ("Congrats! You Win")
        break
    else:
        lives = lives - 1 #you lose a life;; if we comment this line out, infinite loop until you win
        print(f" You got a {dice_roll}. You lose a life. Lives left: {lives}")
        if lives == 0:
            print("You lost!")
            break
            print("Thank you for playing the game!")
