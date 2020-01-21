import random 
import sys





print("-----------------------------------------------------------------")
print("W E L C O M E  T O  T H E  N U M B E R  G U E S S I N G  G A M E ")
print("-----------------------------------------------------------------")

print("Please choose an input from the folowing list of options: ")
print()
print("1. Play the Game")
print("2. Exit the Game")



for i in range(1,6):
         randomnumber=random.randint(1,100)
         gameinput = int(input("Please guess a number between 1 and 100 "))
         if gameinput == randomnumber:
             print("Your guess is correct!")
         else:
             print("Better luck next time!")
 
 
 


