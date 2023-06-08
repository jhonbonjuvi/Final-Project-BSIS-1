import tkinter as tk
import random
from tkinter import messagebox
from tkinter import ttk

questions = {
    "Easy": [
        {
            "question": "What is the command to print 'Hello, World!' in Python?",
            "options": ["print('Hello, World!')", "print('Hello')", "print('World!')", "print('Hello, ' + 'World!')"],
            "answer": "print('Hello, World!')"
        },
        {
            "question": "What is the symbol for single-line comments in Python?",
            "options": ["#", "//", "/* */", "--"],
            "answer": "#"
        },
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "What is the square root of 16?",
            "options": ["4", "8", "16", "64"],
            "answer": "4"
        }
    ],
    "Medium": [
        {
            "question": "What is the output of the following code?\n\nx = [1, 2, 3]\nprint(x[3])",
            "options": ["1", "2", "3", "IndexError"],
            "answer": "IndexError"
        },
        {
            "question": "What is the result of the following expression?\n\n3 + 2 * 4 / 2 - 1",
            "options": ["8", "7", "6", "5"],
            "answer": "7"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Venus", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "What is the largest ocean in the world?",
            "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
            "answer": "Pacific Ocean"
        }
    ],
    "Hard": [
        {
            "question": "What is the time complexity of a binary search algorithm?",
            "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
            "answer": "O(log n)"
        },
        {
            "question": "What is the output of the following code?\n\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)",
            "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "[1, 2, 4]", "[1, 2, 3, [4]]"],
            "answer": "[1, 2, 3, 4]"
        },
        {
            "question": "Which scientist developed the theory of relativity?",
            "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Marie Curie"],
            "answer": "Albert Einstein"
        },
        {
            "question": "What is the chemical symbol for the element Iron?",
            "options": ["Fe", "Ir", "In", "Io"],
            "answer": "Fe"
        }
    ]
}

class QuizGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Quiz Game")
        self.geometry("400x400")

        self.configure(bg="gray19")

        self.difficulty_var = tk.StringVar()
        self.question_label = tk.Label(
            self,
            text="Welcome to the Quiz Game!",
            wraplength=380,
            font=("Arial", 14),
            bg="gray19",
            fg="white"
        )
        self.question_number_label = tk.Label(
            self,
            text="",
            font=("Arial", 12),
            bg="gray19",
            fg="white"
        )
        self.options = []
        self.score = 0
        self.total_questions = 3
        self.question_count = 0

        self.difficulty_frame = ttk.Frame(self)
        self.difficulty_frame.pack(pady=10)
        self.question_label.pack(pady=10)
        self.question_number_label.pack(pady=10)

        for difficulty in questions.keys():
            ttk.Radiobutton(
                self.difficulty_frame,
                text=difficulty,
                variable=self.difficulty_var,
                value=difficulty,
                command=self.start_quiz,
                style="TRadiobutton"
            ).pack(side=tk.LEFT)

        self.style = ttk.Style()
        self.style.configure(
            "TRadiobutton",
            font=("Arial", 12),
            background="gainsboro",
            foreground="black"
        )
        self.style.configure(
            "TButton",
            font=("Arial", 12),
            background="DeepSkyBlue",
            foreground="black",
            width=20
        )

        self.submit_button = ttk.Button(
            self,
            text="Start",
            command=self.start_quiz,
            style="TButton"
        )
        self.submit_button.pack(pady=10)

       
        self.theme_button = ttk.Button(
            self,
            text="Switch Theme",
            command=self.switch_theme,
            style="TButton"
        )
        self.theme_button.pack(pady=10)

    def switch_theme(self):
        
        current_theme = self.configure("bg")[-1]
        if current_theme == "gray19":
            self.configure(bg="gray")
        else:
            self.configure(bg="gray19")

    def start_quiz(self):
        difficulty = self.difficulty_var.get()

        if difficulty:
            self.difficulty_frame.destroy()
            self.submit_button.destroy()
            self.theme_button.destroy()  # Hide the theme button during the quiz
            self.display_question(difficulty)
        else:
            messagebox.showinfo("Error", "Please select a difficulty level.")

    def display_question(self, difficulty):
        question = random.choice(questions[difficulty])
        self.question_count += 1
        self.question_number_label.config(text=f"Question {self.question_count}/{self.total_questions}", fg="white")
        self.question_label.config(text=question["question"], fg="yellow")

        for option in self.options:
            option.destroy()

        self.options = []

        for i, choice in enumerate(question["options"]):
            option = ttk.Button(
                self,
                text=choice,
                command=lambda choice=choice: self.check_answer(question, choice),
                style="TButton"
            )
            option.pack(pady=5)
            self.options.append(option)

    def check_answer(self, question, answer):
        if answer == question["answer"]:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", "Your answer is incorrect.")

        if self.question_count < self.total_questions:
            self.display_question(self.difficulty_var.get())
        else:
            messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{self.total_questions}")
            self.quit()

if __name__ == "__main__":
    game = QuizGame()
    game.mainloop()
