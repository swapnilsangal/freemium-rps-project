import gameboard 
import random 

def game(player_choice): 
    choice = ["rock", "paper", "scissor"]
    computer_choice=random.choice(choice) 
    gameboard.player_choice_box.set(player_choice) 
    gameboard.computer_choice_box.set(computer_choice) 

    if(computer_choice==player_choice):
        gameboard.result_box.set("It's a Tie.")
    elif(computer_choice=="scissor" and player_choice=="rock"):
        gameboard.result_box.set("Player won!!")
    elif(computer_choice=="scissor" and player_choice=="paper"):
        gameboard.result_box.set("Computer won!! ")
        
    elif(computer_choice=="paper" and player_choice=="rock"):
        gameboard.result_box.set("Computer won!!")
    elif(computer_choice=="paper" and player_choice=="scissor"):
        gameboard.result_box.set("Player won!!")
    elif(computer_choice=="rock" and player_choice=="paper"):
        gameboard.result_box.set("Player won!!")
    elif(computer_choice=="rock" and player_choice=="scissor"):
        gameboard.result_box.set("Computer won!!")
