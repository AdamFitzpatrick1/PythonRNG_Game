import random #imports the random number generator library.
import sys #imports the system library.





print("-----------------------------------------------------------------")    #Prints the top part of a border
print("W E L C O M E  T O  T H E  N U M B E R  G U E S S I N G  G A M E ")    #Prints the main text displayed for the welcome message
print("-----------------------------------------------------------------")    #Prints the bottom part of a border

print() #Empty print statement(just prints the text below on a new line, provides whitespace)



for i in range(1,6): #A for loop which gives the user 5 chances to enter the correct answer. As computers start counting from 0 its techically counting from 0-4 which still alows for 5 chances.
         randomnumber=random.randint(1,100) #Initialise the random number function and set it to create a random number in the range 1 to 100.
         gameinput = int(input("Please guess a number between 1 and 100 ")) #User input using the keyboard as an integer it instructs them to enter a guess
         if gameinput == randomnumber: #An if statement that compares what the user has inputted to the previously generated random number
             print("Your guess is correct!") #When the if statement condiiton is true, it will print that the user is correct
         else:
             print("Better luck next time!") #If it's not true (false) it will print better luck next time!
 
 
 


