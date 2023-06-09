from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        age = int(age_entry.get())

        if unit_var.get() == "cm":
            height /= 100  
        elif unit_var.get() == "in":
            height *= 0.0254  

        if weight_var.get() == "lbs":
            weight *= 0.45359237  

        bmi = weight / (height ** 2)

        category = ""
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for height, weight, and age.")

import tkinter
import customtkinter

root= customtkinter.CTk()
root.geometry('480x500')
root.title('BMI_Calculator')

frame_1= customtkinter.CTkFrame(master=root)
frame_1.pack(pady=20,padx=60,fill=tkinter.BOTH,expand=True)

def My_BMI():
    l = switch.get()
    l = int(l)

    if l==1:
        customtkinter.set_appearance_mode("dark")
        switch.configure(text='dark mode')
    else:
        customtkinter.set_appearance_mode("light")
        switch.configure(text='light mode')


switch= customtkinter.CTkSwitch(master=frame_1,command=My_BMI)
switch.configure(text='MODE')
switch.pack(pady=12,padx=10)
switch.select()


window_width = 400
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


frame = Frame(root)
frame.pack(pady=100)

unit_var = StringVar(value="cm")
weight_var = StringVar(value="kg")


height_label = Label(frame, text="Height:")
height_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

height_entry = Entry(frame)
height_entry.grid(row=0, column=1, padx=5, pady=5)

unit_menu = OptionMenu(frame, unit_var, "cm", "inch")
unit_menu.grid(row=0, column=2, padx=5, pady=5, sticky="w")


weight_label = Label(frame, text="Weight:")
weight_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

weight_entry = Entry(frame)
weight_entry.grid(row=1, column=1, padx=5, pady=5)

weight_menu = OptionMenu(frame, weight_var, "kg", "lbs")
weight_menu.grid(row=1, column=2, padx=5, pady=5, sticky="w")


gender_label = Label(frame, text="Gender:")
gender_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

gender_var = StringVar(value="Male")
gender_menu = OptionMenu(frame, gender_var, "Male", "Female")
gender_menu.grid(row=2, column=1, padx=5, pady=5, columnspan=2, sticky="w")


age_label = Label(frame, text="Age:")
age_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

age_entry = Entry(frame)
age_entry.grid(row=3, column=1, padx=5, pady=5)


calculate_button = Button(root, text="Calculate", command=calculate_bmi)
calculate_button.pack(pady=10)

root.mainloop()