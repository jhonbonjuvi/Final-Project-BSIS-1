from tkinter import messagebox as mb
import tkinter as tk
import random
import winsound

r = tk.Tk()
r.geometry('700x550')
r.title('Roll Dice')
c = tk.Canvas(r, width=700, height=550)
c.pack()

# Define available colors
colors = ['red', 'blue', 'green', 'yellow', 'purple']

# Variable to store the selected color
selected_color = tk.StringVar(value=colors[0])

# Variable to store the current theme state
current_theme = tk.StringVar(value="light")


def play_button_sound():
    # Play button click sound
    winsound.PlaySound("C:/Users/rubom/PycharmProjects/RollDice/click.wav", winsound.SND_ASYNC)


def play_winning_sound():
    # Play your winning sound here
    winsound.PlaySound('C:/Users/rubom/PycharmProjects/RollDice/winning.wav', winsound.SND_FILENAME)


def play_game_over_sound():
    # Play your game over sound here
    winsound.PlaySound('C:/Users/rubom/PycharmProjects/RollDice/game over.wav', winsound.SND_FILENAME)


def roll_dice():
    play_button_sound()
    global bttn_clicks
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    d = {'\u2680': 1, '\u2681': 2, '\u2682': 3, '\u2683': 4, '\u2684': 5, '\u2685': 6}
    die1 = random.choice(dice)
    die2 = random.choice(dice)
    ldice.configure(text=f'{die1} {die2}', fg=selected_color.get())
    c.create_window(350, 250, window=ldice)
    res = d[die1] + d[die2]
    label2.configure(text="You got  " + str(res))
    bttn_clicks += 1
    label1['text'] = "Dice rolled: " + str(bttn_clicks) + " times"

    if bttn_clicks == 10 and res != 10:
        rollbutton.configure(state='disabled')
        play_game_over_sound()
        mb.showerror("Game over", "Sorry, Try again")
    elif res == 10:
        rollbutton.configure(state='disabled')
        play_winning_sound()
        mb.showinfo("Winner", "Congrats, you won!!")


def restart():
    global bttn_clicks
    bttn_clicks = 0
    label1.configure(text="")
    label2.configure(text="Not rolled yet", fg='black')
    rollbutton.configure(state='normal')


def toggle_theme():
    current = current_theme.get()
    if current == "light":
        set_dark_theme()
    else:
        set_light_theme()


def set_light_theme():
    r.configure(bg="white")
    c.configure(bg="white")
    label1.configure(bg="white", fg="black")
    label2.configure(bg="white", fg="black")
    label3.configure(bg="white", fg="black")
    toggle_button.configure(text="Toggle Dark Theme", command=set_dark_theme)
    current_theme.set("light")


def set_dark_theme():
    r.configure(bg="black")
    c.configure(bg="black")
    label1.configure(bg="black", fg="white")
    label2.configure(bg="black", fg="white")
    label3.configure(bg="black", fg="white")
    toggle_button.configure(text="Toggle Light Theme", command=set_light_theme)
    current_theme.set("dark")


ldice = tk.Label(r, text='', font=('Times', 120), fg='green')
rollbutton = tk.Button(r, text='Roll the dice', font=('times', 20, "bold"), state="disabled", foreground='purple',
                       height=1, width=15, command=roll_dice)
rollbutton.configure(command=lambda: [roll_dice(), play_button_sound()])
c.create_window(350, 100, window=rollbutton)
button1 = tk.Button(r, text='Start/Restart game', font=('times', 20, "bold"), foreground='Black', height=1, width=15,
                    command=restart)
button1.configure(command=lambda: [restart(), play_button_sound()])
c.create_window(350, 50, window=button1)
label1 = tk.Label(r, text='', font=('Times', 20, 'bold'), fg='black')
c.create_window(180, 410, window=label1)
label2 = tk.Label(r, text='Not rolled yet', font=('Times', 20, 'bold'), fg='black', width=12)
c.create_window(480, 410, window=label2)
label3 = tk.Label(r, text='Winning rule: The player wins if they get a sum of 10 on rolling 2 dice, within 10 chances',
                  font=('Times', 13, 'bold'), fg='black')
c.create_window(350, 500, window=label3)

color_menu = tk.OptionMenu(r, selected_color, *colors)
color_menu.config(font=('Times', 14))
c.create_window(620, 50, window=color_menu)

toggle_button = tk.Button(r, text="Toggle Dark Theme", command=toggle_theme)
c.create_window(620, 120, window=toggle_button)

bttn_clicks = 0

set_light_theme()

r.mainloop()
