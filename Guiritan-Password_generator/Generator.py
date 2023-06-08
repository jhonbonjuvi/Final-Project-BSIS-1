from tkinter import *
from random import randint

# Dark mode colors
bg_color = "#222222"
fg_color = "#ffffff"
entry_bg_color = "#333333"
button_bg_color = "#555555"
button_fg_color = "#ffffff"

root = Tk()
root.title('Strong Password Generator')
root.geometry("500x300")

# Configure dark mode colors
root.config(bg=bg_color)
root.option_add("*Font", "Helvetica")
root.option_add("*Label.Font", "Helvetica")
root.option_add("*Entry.Font", "Helvetica")

# Generate Random Strong Password
def new_rand():
    # Clear Our Entry Box
    pw_entry.delete(0, END)

    # Get PW Length and convert to integer
    pw_length = int(my_entry.get())

    # create a variable to hold our password
    my_password = ''

    # Loop through password length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    # Output password to the screen
    pw_entry.delete(0, END)
    pw_entry.insert(END, my_password)

# Copy to clipboard
def clipper():
    # Clear the clipboard
    root.clipboard_clear()
    # Copy to clipboard
    root.clipboard_append(pw_entry.get())

# Label Frame
lf = LabelFrame(root, text="How Many Characters?", bg=bg_color, fg=fg_color)
lf.pack(pady=20)

# Create Entry Box To Designate Number of Characters
my_entry = Entry(lf, font=("Helvetica", 24), bg=entry_bg_color, fg=fg_color, bd=0, justify="center")
my_entry.pack(pady=20, padx=20)

# Create Entry Box For Our Returned Password
pw_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg=entry_bg_color, fg=fg_color, justify="center")
pw_entry.pack(pady=20)

# Create a frame for our Buttons
my_frame = Frame(root, bg=bg_color)
my_frame.pack(pady=20)

# Create our Buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand, bg=button_bg_color, fg=button_fg_color)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper, bg=button_bg_color, fg=button_fg_color)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()