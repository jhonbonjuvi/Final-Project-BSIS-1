from tkinter import *
import random
import winsound


def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")
        winsound.PlaySound("C:/Users/rubom/PycharmProjects/tictactoe/click.wav", winsound.SND_ASYNC)


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player
    winsound.PlaySound("C:/Users/rubom/PycharmProjects/tictactoe/click.wav", winsound.SND_ASYNC)

    player = random.choice(players)

    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg=button_color)


def toggle_theme():
    global button_color, label_color, background_color
    winsound.PlaySound("C:/Users/rubom/PycharmProjects/tictactoe/click.wav", winsound.SND_ASYNC)

    if button_color == "white":
        button_color = "blue"
        label_color = "white"
        background_color = "gray"  # New line: set the background color

    else:
        button_color = "white"
        label_color = "black"
        background_color = "white"  # New line: set the background color

    window.config(bg=background_color)

    reset_button.config(bg=button_color, fg=label_color)
    label.config(bg=button_color, fg=label_color)

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(bg=button_color, fg=label_color)


window = Tk()
window.title("Tic-Tac-Toe")
window.geometry('600x650')
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

button_color = "white"
label_color = "black"
background_color = "white"

theme_button = Button(text="Toggle Theme", font=('times new roman', 15, 'bold'), command=toggle_theme, bg=button_color, fg=label_color)
theme_button.pack(side="top")

reset_button = Button(text="Restart", font=('times new roman', 20, 'bold'), command=new_game, bg=button_color, fg=label_color)
reset_button.pack(side="top")

label = Label(text=player + " turn", font=('times new roman', 20, 'bold'), bg=button_color, fg=label_color)
label.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('times new roman', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column),
                                      bg=button_color, fg=label_color)
        buttons[row][column].grid(row=row, column=column)

window.config(bg=background_color)  # New line: set the background color of the window

window.mainloop()
