import tkinter as tk
from tkinter import Text
from PIL import Image, ImageTk
import pygame


def play_sound(sound_file, volume=1.0):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()


def play_kick(event=None):
    play_sound('C:/Users/rubom/PycharmProjects/drumProject/kick-bass.mp3', volume=0.9)


def play_snare(event=None):
    play_sound('C:/Users/rubom/PycharmProjects/drumProject/snare.mp3', volume=0.9)


def play_crash(event=None):
    play_sound('C:/Users/rubom/PycharmProjects/drumProject/crash.mp3', volume=0.9)


def play_tom1(event=None):
    play_sound('C:/Users/rubom/PycharmProjects/drumProject/tom-1.mp3', volume=0.9)


def play_tom2(event=None):
    play_sound('C:/Users/rubom/PycharmProjects/drumProject/tom-2.mp3', volume=0.9)


def play_tom3(event=None):
    play_sound('C:/Users/rubom/PycharmProjects/drumProject/tom-3.mp3', volume=0.9)


def play_tom4(event=None):
    play_sound('C:/Users/rubom/PycharmProjects/drumProject/tom-4.mp3', volume=0.9)

def play_tom5(event=None):
    play_sound('C:/Users/rubom/PycharmProjects/drumProject/tom-5.mp3', volume=0.9)


root = tk.Tk()
root.title("Drum Kit")
root.geometry('520x600')
root.config(bg="dark gray")

# Drum set layout
header_label = tk.Label(root, text="Drum Kit", font=("times new roman", 24, "bold"), bg="dark gray")
header_label.grid(row=0, column=0, columnspan=3, pady=20)

kick_image = Image.open("C:/Users/rubom/PycharmProjects/drumProject/kick.png")
snare_image = Image.open("C:/Users/rubom/PycharmProjects/drumProject/snare.png")
crash_image = Image.open("C:/Users/rubom/PycharmProjects/drumProject/crash.png")
tom1_image = Image.open("C:/Users/rubom/PycharmProjects/drumProject/tom1.png")
tom2_image = Image.open("C:/Users/rubom/PycharmProjects/drumProject/tom2.png")
tom3_image = Image.open("C:/Users/rubom/PycharmProjects/drumProject/tom3.png")
tom4_image = Image.open("C:/Users/rubom/PycharmProjects/drumProject/tom4.png")



kick_image = kick_image.resize((150, 150))
snare_image = snare_image.resize((150, 150))
crash_image = crash_image.resize((150, 150))
tom1_image = tom1_image.resize((150, 150))
tom2_image = tom2_image.resize((150, 150))
tom3_image = tom3_image.resize((150, 150))
tom4_image = tom4_image.resize((150, 150))

kick_photo = ImageTk.PhotoImage(kick_image)
snare_photo = ImageTk.PhotoImage(snare_image)
crash_photo = ImageTk.PhotoImage(crash_image)
tom1_photo = ImageTk.PhotoImage(tom1_image)
tom2_photo = ImageTk.PhotoImage(tom2_image)
tom3_photo = ImageTk.PhotoImage(tom3_image)
tom4_photo = ImageTk.PhotoImage(tom4_image)

tom4_button = tk.Button(root, image=tom4_photo, command=play_tom4)
tom4_button.grid(row=2, column=2, padx=10, pady=10)

crash_button = tk.Button(root, image=crash_photo, command=play_crash)
crash_button.grid(row=1, column=0, padx=10, pady=10)

snare_button = tk.Button(root, image=snare_photo, command=play_snare)
snare_button.grid(row=2, column=1, padx=10, pady=10)

tom1_button = tk.Button(root, image=tom1_photo, command=play_tom1)
tom1_button.grid(row=2, column=0, padx=10, pady=10)

tom2_button = tk.Button(root, image=tom2_photo, command=play_tom2)
tom2_button.grid(row=1, column=2, padx=10, pady=10)

tom3_button = tk.Button(root, image=tom3_photo, command=play_tom3)
tom3_button.grid(row=1, column=1, padx=10, pady=10)

kick_button = tk.Button(root, image=kick_photo, command=play_kick)
kick_button.grid(row=3, column=1, padx=10, pady=10)

# Register hotkeys
root.bind('<KeyPress-space>', play_kick)
root.bind('<KeyPress-A>', play_snare)
root.bind('<KeyPress-S>', play_crash)
root.bind('<KeyPress-D>', play_tom1)
root.bind('<KeyPress-J>', play_tom2)
root.bind('<KeyPress-K>', play_tom3)
root.bind('<KeyPress-L>', play_tom4)

drum_instructions = """Drum Control Instruction:
- Press Spacebar: Kick
- Press A: Snare
- Press S: Crash
- Press D: Tom 1
- Press J: Tom 2
- Press K: Tom 3
- Press L: Tom 4"""

instructions_text = Text(root, width=20, height=10, font=("Arial", 10))
instructions_text.insert('1.0', drum_instructions)
instructions_text.config(state='disabled')
instructions_text.grid(row=3, column=0, padx=10, pady=10)

pygame.mixer.init()

root.mainloop()
