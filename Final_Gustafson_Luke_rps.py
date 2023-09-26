# this file was created by Luke Gustafson on 9/25/23
'''
Goals:
When a user click on their choice, the computer randomly chooses and displays the result 

'''


import turtle # the site of the graphics 
from turtle import *
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images') # where the images are drawn from in the graphics 

WIDTH, HEIGHT = 1000, 400  # where the graphic pops up in the terminal 
rock_w, rock_h = 256, 280 # with and hight of rock and were it sits in the terminal
paper_w, paper_h = 256, 204 # with and hight of paper and were it sits in the terminal
scissors_w, scissors_h = 256, 170 # with and hight of scissors and were it sits in the terminal 

# source day 13 class code 

screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")
# what makes the graphis apear in the terminal 



cv = screen.getcanvas()

cv._rootwindow.resizable(False, False)

rock_image = os.path.join(images_folder, 'rock.gif')
rock_instance = turtle.Turtle() # the rock image from immages file 
paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()  # the paper image from immages file 
scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
# the scisors image from immages file 

def show_rock(x,y): # where rock pops up in terminal 
    screen.addshape(rock_image)
    rock_instance.shape(rock_image)
    rock_instance.penup() 
    rock_instance.setpos(x,y)

def show_paper(x,y): # where paper pops up in terminal 
    screen.addshape(paper_image)  
    paper_instance.shape(paper_image) 
    paper_instance.penup()  
    paper_instance.setpos(x,y)

def show_scissors(x,y): # where scissors pops up in terminal 
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

t = turtle.Turtle()
text = turtle.Turtle()
text.color('deep pink') # Color of the text in the terminal 
t.penup()
text.hideturtle()

t.hideturtle()

show_rock(-300, 0) # the location where rock, paper and scisors pops up in terminal 
show_paper(0,0)
show_scissors (300,0)

text.penup()
text.hideturtle()
text.setpos(-300,150)
text.write("What do you choose, rock, paper, or scissors?", False, "left", ("Arial", 24, "normal"))
 # where the text of the players choice pops up in the terminal

def collide(x,y,obj,w,h): # this function uses and x y value, an obj
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False
    t.penup()
# source form day 13 code 
def player(x, y): 
    global text

    if (collide(x,y,rock_instance, rock_w, rock_h)):
        user_choice = "rock" 
    elif(collide(x,y,paper_instance,rock_w,rock_h)):
        user_choice = "paper"
    elif(collide(x,y,scissors_instance,scissors_w,scissors_h)):
        user_choice = "scissors"
    
    text.penup()
    text.clear()  
    text.goto(-100, 150)
    text.write(f"You chose {user_choice}!", align="left", font=("Arial", 24, "normal"))

    from random import randint 

    choices = ["rock", "paper", "scissors"]
    computer = choices[randint(0, 2)] # the computors choice of rock, paper or scissors 

    message = f"Computer chooses... {computer}!"
    x, y = -200, -200
    target_x, target_y = -200, -200
    text.penup()
    text.goto(x, y)
    text.write(message, align="left", font=("Arial", 24, "normal"))
    text.goto(target_x, target_y)
    # the text of the computors choice of the outcome of rock paper scissors 


    import time
    time.sleep(2) # the time it takes for the computor to output with the result of the Rock, paper scisors game is. 

    if user_choice == computer:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer == "scissors") or \
         (user_choice == "paper" and computer == "rock") or \
         (user_choice == "scissors" and computer == "paper"):
        result = "You won!"
    else:
        result = "You lost!"

    text.clear()
    text.goto(-82, 151)
    text.write(result, align="left", font=("Arial", 24, "normal"))
    

playerchoice = screen.onclick(player)

playerchoice = screen.mainloop() # loops back and allows the player to play again 

# while True: 
     
#     '''
#     The Code for User and Computer Inputs - Possible Inputs that the Computer can choose from and how they are interpreted
    
#     '''
    
#     choices = ["rock", "paper", "scissors"] # the list of possible choices for the computer
#     y = (choices[randint(0,2)]) # prints "rock", "paper", or "scissors"

#     # x = (input("You chose:")) # asks rock paper scissors?
#     x = x.lower() # converts any uppercase user inputs into lowercase

#     print(f"The Computer Chose: {y}") # prints the computer's choice

    
    
#     y = randint(0,2)
#     '''
#     Rock Paper Scissors Logic - how the computer decides who wins or loses
    
#     '''
    
#     if x == y:
#         print("Tie") # If the player input and the computer input are the same, the result is a tie
#     elif x == "rock" and y == "scissors" or x == "paper" and y == "rock" or x == "scissors" and y == "paper":
#         print("You Win!") # The logic for determining what wins in a given situation
#     else:
#         print("You Lose!") # Every other matchup is a loss
#     if x == "rock" and y == "scissors":
#         print("You Win!")
#     elif x == "rock" and y == "paper":
#         print("You Lose!")
#     elif x == "rock" and y == "rock":
#         print("Tie")

#     if x == "paper" and y == "rock":
#         print("You Win!")
#     elif x == "paper" and y == "scissors":
#         print("You Lose!")
#     elif x == "paper" and y == "paper":
#         print("Tie")
#     if x == "scissors" and y == "paper":
#         print("You Win!")
#     elif x == "scissors" and y == "rock":
#         print("You Lose!")
#     elif x == "scissors" and y == "scissors":
#         print("Tie")
    
