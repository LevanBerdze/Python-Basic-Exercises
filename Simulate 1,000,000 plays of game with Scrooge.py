"""
pick 6 coins at random, and if they sum to at least $0.50, you win and can keep your
money! But if you lose, you have to pay Scrooge a dollar.
simulate 1,000,000 plays of this game. And tell what is % that you will be sucsesfull 
in the game.

"""
import random


num_of_plays = 10 ** 6
success = 0 
winnings = 0 


mylist = [0.01, 0.05, 0.10, 0.25] 
   
for i in range(num_of_plays):
    sum = 0
    for j in range(6):
        sum += random.choice(mylist)
    
    if sum >= 0.50:
        success += 1
        winnings += sum
    else:
        winnings -= 1




print(f'{success/num_of_plays:.2f}')
print(f'{winnings/num_of_plays:.2f}')
