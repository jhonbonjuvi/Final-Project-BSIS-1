import tkinter as tk
from tkinter import messagebox
from random import shuffle
import threading
import winsound


class RiddleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Riddle Game")
        self.master.geometry("600x700")
        self.master.config(bg="light gray")

        self.dark_mode = False  # Added dark mode toggle

        self.riddles = [
            {
                "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
                "choices": ["Whistle", "Cloud", "Echo", "Music"],
                "answer": "Echo"
            },
            {
                "question": "What has keys but can't open locks?",
                "choices": ["Piano", "Keyboard", "Map", "Chest"],
                "answer": "Piano"
            },
            {
                "question": "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
                "choices": ["Gold", "Diamond", "Coal", "Pencil"],
                "answer": "Pencil"
            },
            {
                "question": "What has a heart that doesn't beat?",
                "choices": ["Clock", "Deck of cards", "Artichoke", "Computer"],
                "answer": "Deck of cards"
            },
            {
                "question": "What has to be broken before you can use it?",
                "choices": ["Egg", "Glass", "Mirror", "Telephone"],
                "answer": "Egg"
            },
            {
                "question": "I have cities but no houses, forests but no trees, and rivers but no water. What am I?",
                "choices": ["Globe", "Map", "Book", "Planet"],
                "answer": "Map"
            },
            {
                "question": "The more you take, the more you leave behind. What am I?",
                "choices": ["Footsteps", "Memories", "Breath", "Time"],
                "answer": "Footsteps"
            },
            {
                "question": "What gets wet while drying?",
                "choices": ["Towel", "Soap", "Clothes", "Sun"],
                "answer": "Towel"
            },
            {
                "question": "What can you catch, but not throw?",
                "choices": ["Fish", "Ball", "Cold", "Fire"],
                "answer": "Cold"
            },
            {
                "question": "I am always hungry, I must always be fed, The finger I touch, Will soon turn red. What am I?",
                "choices": ["Fire", "Baby", "Stove", "Money"],
                "answer": "Fire"
            },
            {
                "question": "What comes once in a minute, twice in a moment, but never in a thousand years?",
                "choices": ["Hour", "Second", "Millennium", "Year"],
                "answer": "Second"
            },
            {
                "question": "What goes up but never comes down?",
                "choices": ["Age", "Stairs", "Rocket", "Balloon"],
                "answer": "Age"
            },
            {
                "question": "What can be broken but is never held?",
                "choices": ["Heart", "Mirror", "Promise", "Secret"],
                "answer": "Promise"
            },
            {
                "question": "I am a word of letters three, add two and fewer there will be. What am I?",
                "choices": ["Few", "Six", "Five", "Nine"],
                "answer": "Few"
            },
            {
                "question": "I am an odd number. Take away one letter and I become even. What number am I?",
                "choices": ["Seven", "Three", "Five", "Nine"],
                "answer": "Seven"
            },
            {
                "question": "What has a head, a tail, is brown, and has no legs?",
                "choices": ["Penny", "Snake", "Dog", "Worm"],
                "answer": "Penny"
            },
            {
                "question": "What comes once in a minute, twice in a moment, but never in a thousand years?",
                "choices": ["M", "N", "I", "O"],
                "answer": "M"
            },
            {
                "question": "What has keys but can't open locks, space but no room, and you can enter but not go in?",
                "choices": ["Computer", "Calculator", "Keyboard", "Telephone"],
                "answer": "Keyboard"
            },
            # Add more riddles...
        ]

        self.current_riddle = 0
        self.score = 0
        self.max_score = len(self.riddles)
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Riddle Game", font=("times new roman", 18, "bold"), bg="light gray",
                              fg="black")
        self.label.pack(pady=10)

        self.instructions_button = tk.Button(self.master, text="Instructions", command=self.display_instructions,
                                             font=("times new roman", 14, 'bold'))
        self.instructions_button.pack(pady=10)

        self.score_label = tk.Label(self.master, text="Score: 0", font=("times new roman", 14, 'bold'), bg="light gray")
        self.score_label.pack(side=tk.TOP, pady=10)

        self.riddle_text = tk.Label(self.master, text=self.riddles[self.current_riddle]["question"], wraplength=500,
                                    font=("Arial", 16, 'bold'), bg="light gray")
        self.riddle_text.pack(pady=20)

        self.choices_frame = tk.Frame(self.master, bg="light gray")
        self.choices_frame.pack()

        self.choices = []
        for i in range(4):
            choice = tk.Button(self.choices_frame, text="", command=lambda i=i: self.select_choice(i),
                               font=("Arial", 14), width=15)
            choice.grid(row=i, column=0, pady=5)
            self.choices.append(choice)

        self.next_button = tk.Button(self.master, text="Next Riddle", command=self.next_riddle,
                                     font=("Arial", 14, "bold"))
        self.next_button.pack(pady=10)
        self.next_button.config(state=tk.DISABLED)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.quit_game, font=("Arial", 14, "bold"))
        self.quit_button.pack(pady=10)

        self.theme_button = tk.Button(self.master, text="Toggle Theme", command=self.toggle_theme,
                                      font=("Arial", 14, "bold"))
        self.theme_button.pack(pady=10)

        self.update_choices()

    def select_choice(self, choice_index):
        selected_choice = self.choices[choice_index].cget("text")
        self.play_sound("C:/Users/rubom/PycharmProjects/Riddle Game/click.wav")
        self.check_answer(selected_choice)

    def update_choices(self):
        choices = self.riddles[self.current_riddle]["choices"]
        shuffle(choices)

        for i in range(len(choices)):
            self.choices[i].config(text=choices[i])

    def check_answer(self, answer):
        correct_answer = self.riddles[self.current_riddle]["answer"]

        self.play_sound(
            "C:/Users/rubom/PycharmProjects/Riddle Game/correct.wav" if answer == correct_answer else "C:/Users/rubom/PycharmProjects/Riddle Game/wrong.wav")

        if answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Congratulations! You got the right answer.")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct answer is '{correct_answer}'.")

        self.score_label.config(text=f"Score: {self.score}/{self.max_score}")
        self.next_button.config(state=tk.NORMAL)
        for choice in self.choices:
            choice.config(state=tk.DISABLED)

    def next_riddle(self):
        self.current_riddle += 1

        if self.current_riddle < len(self.riddles):
            self.riddle_text.config(text=self.riddles[self.current_riddle]["question"])
            self.next_button.config(state=tk.DISABLED)
            self.update_choices()

            # Reset choice button states
            for choice in self.choices:
                choice.config(state=tk.NORMAL)
        else:
            messagebox.showinfo("Game Over",
                                f"You have completed all the riddles!\nYour final score is {self.score}/{self.max_score}")
            self.reset_game()

    def play_sound(self, filename):
        try:
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        except Exception as e:
            print(f"Failed to play sound '{filename}': {e}")

    def reset_game(self):
        self.current_riddle = 0
        self.score = 0
        self.riddle_text.config(text=self.riddles[self.current_riddle]["question"])
        self.score_label.config(text=f"Score: {self.score}/{self.max_score}")
        self.update_choices()

    def quit_game(self):
        result = messagebox.askyesno("Quit Game", "Are you sure you want to quit?")
        if result:
            self.master.destroy()

    def display_instructions(self):
        instructions = """
                Welcome to the Riddle Game!

                - You will be presented with a riddle.
                - Select one of the multiple-choice options.
                - Click the 'Check Answer' button to see if your answer is correct.
                - After checking the answer, click the 'Next Riddle' button to proceed.
                - Your score will be displayed at the top.
                - You can quit the game anytime by clicking the 'Quit' button.

                Good luck and have fun!
                """
        messagebox.showinfo("Instructions", instructions)

    def toggle_theme(self):
        if self.dark_mode:
            self.master.config(bg="light gray")
            self.choices_frame.config(bg="light gray")
            self.label.config(bg="light gray")
            self.score_label.config(bg="light gray", fg="black")
            self.riddle_text.config(bg="light gray", fg="black")
            self.dark_mode = False
        else:
            self.master.config(bg="black")
            self.choices_frame.config(bg="black")
            self.label.config(bg="black", fg="white")
            self.score_label.config(bg="black", fg="white")
            self.riddle_text.config(bg="black", fg="white")
            self.dark_mode = True


if __name__ == "__main__":
    root = tk.Tk()
    game = RiddleGame(root)
    root.mainloop()
