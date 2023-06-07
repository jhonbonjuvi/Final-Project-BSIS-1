
import tkinter as tk
from tkinter import font

def convert():
    try:
        temperature = float(entry.get())
        result_label.config(text="")
        if selected.get() == 1:  # Celsius to Fahrenheit
            result = (temperature * 9/5) + 32
            result_label.config(text=f"{temperature}°C = {result}°F")
        elif selected.get() == 2:  # Fahrenheit to Celsius
            result = (temperature - 32) * 5/9
            result_label.config(text=f"{temperature}°F = {result}°C")
    except ValueError:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("500x300")
root.configure(bg="black")

selected = tk.IntVar()

celsius_to_fahrenheit = tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=selected, value=1, bg="black", fg="white", font=("Courier", 12))
celsius_to_fahrenheit.pack()

fahrenheit_to_celsius = tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=selected, value=2, bg="black", fg="white", font=("Courier", 12))
fahrenheit_to_celsius.pack()

entry_font = font.Font(family='Courier', size=12)
entry = tk.Entry(root, justify='center', font=entry_font)
entry.pack()

convert_button = tk.Button(root, text="Convert", command=convert, bg="black", fg="white", font=("Courier", 12))
convert_button.pack()

result_label_font = font.Font(family='Courier', size=12)
result_label = tk.Label(root, font=result_label_font, bg="black", fg="white")
result_label.pack()

root.geometry("400x150")  # Set the window size

root.mainloop()