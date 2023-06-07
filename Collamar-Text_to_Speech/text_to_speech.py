import tkinter as tk
import pyttsx3

def convert_text_to_speech():
    text = entry.get()
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
    engine.setProperty('volume', 1.0)  # Adjust the volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

# Create the Tkinter window
window = tk.Tk()
window.title("Text-to-Speech")
window.geometry("300x200")

# Create the entry widget
entry = tk.Entry(window, width=30)
entry.pack(pady=20)

# Create the button widget
button = tk.Button(window, text="Convert", command=convert_text_to_speech)
button.pack()

# Start the Tkinter event loop
window.mainloop()