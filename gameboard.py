import tkinter as tk
import random
import main
from PIL import Image, ImageTk

main_screen = tk.Tk()
main_screen.title("Rock Paper and Scissors")
#Canvas is the window that gets created when we run the app
main_screen_canvas = tk.Canvas(main_screen, width = 600, height = 600, bg="RoyalBlue4")
main_screen_canvas.pack()
player_choice_box = tk.StringVar()
computer_choice_box = tk.StringVar()
result_box = tk.StringVar()

#Label 1 is for naming the App
header = tk.Label(main_screen, text='Rock, Paper & Scissor')
header.config(font=('helvetica', 17, 'bold',  'underline'),bg='Royalblue4',fg='white')
main_screen_canvas.create_window(300, 20, window=header)
#Label 2 is for giving the text to entry field
sub_head_label = tk.Label(main_screen, text='Make your move!')
sub_head_label.config(font=('helvetica', 15, 'bold'),bg='RoyalBlue4',fg='white')
main_screen_canvas.create_window(300, 75, window=sub_head_label)
#Label for Player
player_label = tk.Label(main_screen, text='Player')
player_label.config(font=('helvetica', 15, 'bold'),bg='RoyalBlue4',fg='white')
main_screen_canvas.create_window(190, 350, window=player_label)
#Label for Computer
computer_label = tk.Label(main_screen, text='Computer')
computer_label.config(font=('helvetica', 15, 'bold'),bg='RoyalBlue4',fg='white')
main_screen_canvas.create_window(410, 350, window=computer_label)
#Label for Vs
vs_label = tk.Label(main_screen, text='VS')
vs_label.config(font=('helvetica', 15, 'bold'),bg='RoyalBlue4',fg='white')
main_screen_canvas.create_window(300, 350, window=vs_label)
#Entry for player
player_entry=tk.Entry(main_screen, textvariable = player_choice_box, justify = 'center', width = 10, font=('helvetica', 10, 'bold'),bg='SkyBlue4',fg='white')
main_screen_canvas.create_window(190, 400, window=player_entry)
#Entry for Computer
computer_entry=tk.Entry(main_screen, textvariable = computer_choice_box, justify = 'center', width = 10, font=('helvetica', 10, 'bold'),bg='SkyBlue4',fg='white')
main_screen_canvas.create_window(410, 400, window=computer_entry)
#Entry for storing result
result=tk.Label(main_screen, textvariable = result_box, width = 20, font=('helvetica', 16, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(300,450, window=result)

#Importing Images
stone_image1 = Image.open("Rock.png")
stone_image = ImageTk.PhotoImage(stone_image1)

paper_image1 = Image.open("Paper.png")
paper_image = ImageTk.PhotoImage(paper_image1)

scissors_image1 = Image.open("Scissors.png")
scissors_image = ImageTk.PhotoImage(scissors_image1)

choice = ["rock", "paper", "scissor"]
#button for Rock
rock_btn = tk.Button(image=stone_image, text = 'Rock', command = lambda:main.game(choice[0]), font=('helvetica', 12, 'bold'),bg='RoyalBlue4',fg='white')
main_screen_canvas.create_window(100, 200, window=rock_btn)
#button for paper
paper_btn = tk.Button(image=paper_image,text = 'Paper', command = lambda:main.game(choice[1]), font=('helvetica', 12, 'bold'),bg='RoyalBlue4',fg='white')
main_screen_canvas.create_window(300, 200, window=paper_btn)
#button for scissors
scissor_btn = tk.Button(image=scissors_image,text = 'Scissors', command = lambda:main.game(choice[2]), font=('helvetica', 12, 'bold'),bg='RoyalBlue4',fg='white')
main_screen_canvas.create_window(500, 200, window=scissor_btn)



main_screen.mainloop()
