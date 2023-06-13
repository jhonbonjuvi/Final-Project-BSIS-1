from tkinter import *
import random
import winsound
from tkinter import messagebox

root = Tk()
root.title("Rock, Paper, Scissor Game")
root.config(bg="green")
width = 570
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
# root.config(bg="pink")

# ================================IMAGES========================================
blank_img = PhotoImage(file="blank.png")
player_rock = PhotoImage(file="player_rock.png")
sm_player_rock = player_rock.subsample(3, 3)


player_paper = PhotoImage(file="player_paper.png")
sm_player_paper = player_paper.subsample(3, 3)
player_scissor = PhotoImage(file="player_scissor.png")
sm_player_scissor = player_scissor.subsample(3, 3)
com_rock = PhotoImage(file="com_rock.png")
com_paper = PhotoImage(file="com_paper.png")
com_scissor = PhotoImage(file="com_scissor.png")

# ===============================METHODS========================================
player_score = 0
computer_score = 0


def play_sound(filename):
    winsound.PlaySound(filename, winsound.SND_ASYNC)


def Rock():
    global player_choice
    player_choice = 1
    player_img.configure(image=player_rock)
    play_sound("click.wav")
    MatchProcess()


def Paper():
    global player_choice
    player_choice = 2
    player_img.configure(image=player_paper)
    play_sound("click.wav")
    MatchProcess()


def Scissor():
    global player_choice
    player_choice = 3
    player_img.configure(image=player_scissor)
    play_sound("click.wav")
    MatchProcess()


def MatchProcess():
    global player_score, computer_score
    com_choice = random.randint(1, 3)
    if com_choice == 1:
        comp_img.configure(image=com_rock)
        ComputerRock()
    elif com_choice == 2:
        comp_img.configure(image=com_paper)
        ComputerPaper()
    elif com_choice == 3:
        comp_img.configure(image=com_scissor)
        ComputerScissor()


def ComputerRock():
    global player_score, computer_score
    if player_choice == 1:
        lbl_status.config(text="Game Tie")
        play_sound("tie.wav")
    elif player_choice == 2:
        lbl_status.config(text="Player Win")
        player_score += 1
        lbl_player_score.config(text=f"Player Score: {player_score}")
        lbl_player_score.config(fg="dark red", font=('times new roman', 12, 'bold'))  # Set foreground color
        play_sound("win.wav")
    elif player_choice == 3:
        lbl_status.config(text="Computer Win")
        computer_score += 1
        lbl_computer_score.config(text=f"Computer Score: {computer_score}")
        lbl_computer_score.config(fg="dark blue", font=('times new roman', 12, 'bold'))  # Set foreground color
        play_sound("lose.wav")


def ComputerPaper():
    global player_score, computer_score
    if player_choice == 1:
        lbl_status.config(text="Computer Win")
        computer_score += 1
        lbl_computer_score.config(text=f"Computer Score: {computer_score}")
        lbl_computer_score.config(fg="dark blue", font=('times new roman', 12, 'bold'))  # Set foreground color
        play_sound("lose.wav")
    elif player_choice == 2:
        lbl_status.config(text="Game Tie")
        play_sound("tie.wav")
    elif player_choice == 3:
        lbl_status.config(text="Player Win")
        player_score += 1
        lbl_player_score.config(text=f"Player Score: {player_score}")
        lbl_player_score.config(fg="dark red", font=('times new roman', 12, 'bold'))  # Set foreground color
        play_sound("win.wav")


def ComputerScissor():
    global player_score, computer_score
    if player_choice == 1:
        lbl_status.config(text="Player Win", font=("times new roman", 12, 'bold'))
        player_score += 1
        lbl_player_score.config(text=f"Player Score: {player_score}")
        lbl_player_score.config(fg="dark red", font=('times new roman', 12, 'bold'))  # Set foreground color
        play_sound("win.wav")
    elif player_choice == 2:
        lbl_status.config(text="Computer Win", font=("times new roman", 10, 'bold'))
        computer_score += 1
        lbl_computer_score.config(text=f"Computer Score: {computer_score}")
        lbl_computer_score.config(fg="dark blue", font=('times new roman', 12, 'bold'))  # Set foreground color
        play_sound("lose.wav")
    elif player_choice == 3:
        lbl_status.config(text="Game Tie")
        play_sound("tie.wav")


def NewGame():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    lbl_player_score.config(text="Player Score: 0", fg="black")
    lbl_computer_score.config(text="Computer Score: 0", fg="black")
    lbl_status.config(text="")
    player_img.configure(image=blank_img)
    comp_img.configure(image=blank_img)


def ExitApp():
    confirm = messagebox.askyesno("Quit", "Are you sure you want to quit?")
    if confirm:
        root.destroy()
        exit()


# ===============================LABEL WIDGET=========================================
player_img = Label(root, image=blank_img)
comp_img = Label(root, image=blank_img)
lbl_player = Label(root, text="PLAYER", font=('times new roman', 12, 'bold'))
lbl_player.grid(row=1, column=1)
lbl_player.config(bg="green")
lbl_computer = Label(root, text="COMPUTER", font=('times new roman', 12, 'bold'))
lbl_computer.grid(row=1, column=3)
lbl_computer.config(bg="green")
lbl_status = Label(root, text="", font=('times new roman', 12, 'bold'))
lbl_status.config(bg="green")
player_img.grid(row=2, column=1, padx=30, pady=20)
comp_img.grid(row=2, column=3, pady=20)
lbl_status.grid(row=3, column=2)
lbl_player_score = Label(root, text="Player Score: 0", font=('times new roman', 12, 'bold'))
lbl_player_score.config(bg="green", fg="dark red")  # Set foreground color
lbl_player_score.grid(row=4, column=1)
lbl_computer_score = Label(root, text="Computer Score: 0", font=('times new roman', 12, 'bold'))
lbl_computer_score.config(bg="green", fg="dark blue")  # Set foreground color
lbl_computer_score.grid(row=4, column=3)

# ===============================BUTTON WIDGET===================================
rock = Button(root, image=sm_player_rock, command=Rock)
paper = Button(root, image=sm_player_paper, command=Paper)
scissor = Button(root, image=sm_player_scissor, command=Scissor)
btn_new_game = Button(root, text="New Game", command=NewGame, font=('times new roman', 12, 'bold'))
btn_quit = Button(root, text="Quit", command=ExitApp, font=('times new roman', 12, 'bold'))
rock.grid(row=5, column=1, pady=30)
paper.grid(row=5, column=2, pady=30)
scissor.grid(row=5, column=3, pady=30)
btn_quit.grid(row=6, column=3, pady=10)
btn_new_game.grid(row=6, column=1,  pady=10)

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
