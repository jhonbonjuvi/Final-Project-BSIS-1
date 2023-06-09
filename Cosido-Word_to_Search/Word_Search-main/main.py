import string
import random
import tkinter as tk
from tkinter import ttk
import yaml
import gameUtils as gutils
import os
import winsound
from tkinter import messagebox

root = tk.Tk()
root.title("Word Search Game")

wordPressed = ''
previous = [0, 0]
route = [0, 0]

click_sound = "D:/BSIS_Project/Cosido-Word_to_Search/Word_Search-main/click.wav"
correct_sound = "D:/BSIS_Project/Cosido-Word_to_Search/Word_Search-main/correct.wav"


# ***************> Game Starts <******************
# Function to play click sound effect
def play_click_sound():
    winsound.PlaySound(click_sound, winsound.SND_ASYNC)


# Function to play correct sound effect
def play_correct_sound():
    winsound.PlaySound(correct_sound, winsound.SND_ASYNC)


def quit_game():
    play_click_sound()
    confirm = messagebox.askyesno('QUIT', 'Are you sure you want to quit?')
    if confirm:
        root.destroy()


def gameHeader():
    game_header = tk.Frame(root)
    game_header.pack(fill=tk.X, side=tk.TOP)

    # Quit button
    quit_button = tk.Button(game_header,
                            text="Quit",
                            font=('Helvetica', 12),
                            bg='red',
                            fg='white',
                            command=quit_game)
    quit_button.pack(expand=True, padx=10)

    heading = tk.Label(game_header,
                       text='Word Search Game',
                       font=('Helvetica', 23, 'bold'),
                       fg='blue')
    heading.pack(expand=True, fill=tk.X, pady=12)


def gameFooter():
    game_footer = tk.Frame(root)
    game_footer.pack(fill=tk.X, side=tk.BOTTOM, pady=12)

    footer = tk.Label(
        game_footer,
        text='(Maxene)')
    footer.pack(expand=True, fill=tk.X, pady=0)


def startGame():
    frame1 = tk.Frame(master=root, bg="red")
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=20, pady=12)

    frame2 = tk.Frame(master=root)
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=12)

    configFile = gutils.readConfigFile()
    levelNum = configFile['player']['level']
    levelDetails = [
        configFile['levels'][levelNum]['name'],
        configFile['levels'][levelNum]['words']
    ]
    currScore = tk.StringVar()
    currScore.set(0)
    play_click_sound()

    def updateScore():
        configFile = gutils.readConfigFile()
        score = configFile['player']['score']
        configFile['player']['score'] = score + 1
        currScore.set(score + 1)
        gutils.writeConfigFile(configFile)
        root.update_idletasks()

    frame3 = tk.Frame(master=root)
    frame3.pack(fill=tk.BOTH, side=tk.RIGHT, padx=20, pady=30)

    labelWelcome = tk.Label(master=frame3,
                            text="Welcome",
                            fg='#2c334a',
                            font=('Helvetica', 12, 'bold')).grid(row=0,
                                                                 column=0)

    labelWName = tk.Label(master=frame3,
                          text=configFile['player']['name'],
                          fg='#2c334a',
                          font=('Helvetica', 12, 'bold')).grid(row=0, column=1)

    labelLevelLbl = tk.Label(master=frame3,
                             text="Level",
                             fg='#2c334a',
                             font=('Helvetica', 12)).grid(row=1, column=0)

    labelLevel = tk.Label(master=frame3,
                          text=levelDetails[0],
                          fg='#2c334a',
                          font=('Helvetica', 12, 'bold')).grid(row=1, column=1)

    labelLevelLbl = tk.Label(master=frame3,
                             text="Words",
                             fg='#2c334a',
                             font=('Helvetica', 12)).grid(row=2, column=0)

    labelLevel = tk.Label(master=frame3,
                          text=levelDetails[1],
                          fg='#2c334a',
                          font=('Helvetica', 12, 'bold')).grid(row=2, column=1)

    labelLevelLbl = tk.Label(master=frame3,
                             text="Score",
                             fg='#2c334a',
                             font=('Helvetica', 12)).grid(row=3, column=0)

    labelLevel = tk.Label(master=frame3,
                          textvariable=currScore,
                          fg='#2c334a',
                          font=('Helvetica', 12, 'bold')).grid(row=3, column=1)
    wordList = []

    with open(r'C:/Users/rubom/PycharmProjects/WordSearch/data/words.yaml') as file:
        wordFile = yaml.load(file, Loader=yaml.FullLoader)
        wordList = [word for word in wordFile['words']]

    size = numWords = configFile['words_count']

    arr = [[0 for x in range(size)] for y in range(size)]
    button = [[0 for x in range(size)] for y in range(size)]
    check = [0 for numWords in range(size)]
    dictionary = [0 for createWordSet in range(numWords)]

    directionArr = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1],
                    [0, -1], [1, -1]]
    play_click_sound()

    class Square:
        status = False
        filled = False
        char = ''

    def fill(x, y, word, direction):
        for i in range(len(word)):
            arr[x + direction[0] * i][y + direction[1] * i].char = word[i]
            arr[x + direction[0] * i][y + direction[1] * i].filled = True

    def wordPlace(j, dictionary):
        word = random.choice(wordList)
        direction = directionArr[random.randrange(0, 7)]

        x = random.randrange(0, size - 1)
        y = random.randrange(0, size - 1)

        if (x + len(word) * direction[0] > size - 1 or x + len(word) * direction[0] < 0 or y + len(word) * direction[
            1] > size - 1) or y + len(word) * direction[1] < 0:
            wordPlace(j, dictionary)
            return

        for i in range(len(word)):
            if (arr[x + direction[0] * i][y +
                                          direction[1] * i].filled == True):
                if (arr[x + direction[0] * i][y + direction[1] * i].char !=
                        word[i]):
                    wordPlace(j, dictionary)
                    return
        dictionary[j] = word

        check[j] = tk.Label(frame2,
                            text=word,
                            height=1,
                            width=15,
                            font=('None %d ' % (10)),
                            fg='#254359',
                            bg='#cbe5f7',
                            anchor='c')
        check[j].grid()

        fill(x, y, word, direction)
        return dictionary

    def colourWord(wordPressed, valid):
        route[0] *= -1
        route[1] *= -1
        for i in range(len(wordPressed)):
            if valid or arr[previous[0] + i * route[0]][previous[1] + i * route[1]].status:
                button[previous[0] + i * route[0]][previous[1] + i * route[1]].config(bg='#535edb', fg='white')
                arr[previous[0] + i * route[0]][previous[1] + i * route[1]].status = True
            else:
                button[previous[0] + i * route[0]][previous[1] + i * route[1]].config(bg='#255059', fg='white')

        if valid:
            play_correct_sound()

    # Function to check if the selected word is correct
    def checkWord():
        global wordPressed

        if wordPressed in dictionary:
            wordIndex = dictionary.index(wordPressed)
            if dictionary[wordIndex] != '':
                check[int(wordIndex)].configure(font=('Helvetica', 1), fg='#f0f0f0', bg='#f0f0f0')
                dictionary[wordIndex] = ''

                updateScore()
                colourWord(wordPressed, True)
        else:
            colourWord(wordPressed, False)

        wordPressed = ''
        previous = [0, 0]

    def buttonPress(x, y):
        global wordPressed, previous, route
        newPressed = [x, y]
        play_click_sound()

        if (len(wordPressed) == 0):
            previous = newPressed
            # print(previous)
            wordPressed = arr[x][y].char
            button[x][y].configure(bg='yellow', fg='#255059')

        elif (len(wordPressed) == 1 and (x - previous[0]) ** 2 <= 1
              and (y - previous[1]) ** 2 <= 1 and newPressed != previous):
            wordPressed += arr[x][y].char
            button[x][y].configure(bg='yellow', fg='#255059')

            route = [x - previous[0], y - previous[1]]
            previous = [x, y]

        elif (len(wordPressed) > 1 and x - previous[0] == route[0]
              and y - previous[1] == route[1]):
            wordPressed += arr[x][y].char
            button[x][y].configure(bg='yellow', fg='#255059')
            previous = [x, y]

    for x in range(size):
        for y in range(size):
            arr[x][y] = Square()

    for i in range(numWords):
        wordPlace(i, dictionary)

    for y in range(size):
        for x in range(size):

            if (arr[x][y].filled == False):
                arr[x][y].char = random.choice(string.ascii_uppercase)

            button[x][y] = tk.Button(
                frame1,
                text=arr[x][y].char,
                bg='#255059',
                fg='white',
                width=2,
                height=1,
                relief=tk.FLAT,
                command=lambda x=x, y=y: buttonPress(x, y))
            button[x][y].grid(row=x, column=y)

    checkWordBtn = tk.Button(frame2,
                             text="Check Word",
                             height=1,
                             width=15,
                             anchor='c',
                             bg="#70889c",
                             font=('Helvetica', 10),
                             fg='white',
                             command=checkWord)
    checkWordBtn.grid()


def main():
    gameHeader()
    frame = tk.Frame(root)
    frame.pack(pady=56, padx=180)

    def updateUserInput():
        username = userNameField.get().strip()
        if not username:
            messagebox.showerror("Error", "Please enter your name.")
            return

        gutils.gameLevel(str(levelInpCombo.get()), str(userNameField.get()))
        startGame()
        frame.destroy()

    tk.Label(frame, text="Name", font=('Helvetica', 15),
             fg='#456263').grid(row=0, padx=10, pady=6)
    userNameField = tk.Entry(frame)
    userNameField.grid(row=0, column=1, ipady=6, ipadx=10)

    tk.Label(frame, text="Game Level", font=('Helvetica', 15),
             fg='#456263').grid(row=1)
    levelInpCombo = ttk.Combobox(frame,
                                 values=['Mini', 'Normal', 'Pro', 'Pro Max'])
    levelInpCombo.grid(row=1, column=1, ipady=6, ipadx=10)
    levelInpCombo.current(0)

    tk.Button(frame,
              text="Start Game",
              font=('Helvetica', 12),
              bg='blue',
              fg='white',
              command=updateUserInput).grid(row=3,
                                            column=1,
                                            pady=8,
                                            ipady=6,
                                            ipadx=10)

    gameFooter()
    root.mainloop()


if __name__ == '__main__':
    main()
