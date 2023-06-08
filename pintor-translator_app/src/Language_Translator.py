from tkinter import *
import googletrans
import textblob
import tkinter as tk
import time
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

root = tk.Tk()
root.title('Language Translator')
root.iconbitmap(r'img/icn.ico')
root.config(bg='white')
root.geometry('690x580')
root.resizable(False, False)

# Create frames
top_frame = Frame(root, bg= 'white', relief="solid")
top_frame.grid(row=0, column = 0, pady=20)

middle_frame = Frame(root,  bg= 'white')
middle_frame.grid(row=1, column=0, padx = 10)

bottom_frame = Frame(root,  bg= 'white',)
bottom_frame.grid(row=2, column=0,pady=5)

last_frame = Frame(root,  bg= 'white')
last_frame.grid(row=0, column=1 ,pady=10)


# Clock
def clock():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    ampm = time.strftime('%p')
    day = time.strftime('%A')
    month = time.strftime("%d %B, %Y")

    show_time.config(text=hour + ':' + minute + ':' + second + ' ' + ampm)
    show_day.config(text=month + ' ' + day)
    show_time.after(1000, clock)

logo = ImageTk.PhotoImage(Image.open('img/Logo.png'))
logo_out=Label(top_frame, image = logo, bg = 'gray1' )
logo_out.grid(row=1, rowspan=5, column=0, padx=5)


show_time = tk.Label(top_frame, text='', bg = 'white', font=('ds-digital', 45, 'bold'))
show_time.grid(row=1, column=1)

show_day = tk.Label(top_frame, text='',bg= 'white', font=('Helvetica', 15, 'bold'))
show_day.grid(row=2, column=1)


# Translator
def translate_word():
    translate_text.delete(1.0, END)

    try:
        for key, value in language.items():
            if value == language_opt.get():
                from_language_key = key
                

        for key, value in language.items():
            if value == language_opt_trans.get():
                to_language_key = key

        words = textblob.TextBlob(original_text.get(1.0, END))
        words = words.translate(from_lang=from_language_key, to=to_language_key)
        translate_text.insert(1.0, words)

    except Exception as e:
        messagebox.showerror('Translator', e)

def clear():
    original_text.delete(1.0, END)
    translate_text.delete(1.0, END)

# Languages from googletrans
language = googletrans.LANGUAGES
language_list = list(language.values())

# Textbox
label1 = tk.Label(middle_frame, text='Original Text : ',bg='white' ,font = ('bold'))
label1.grid(row=0, column= 0)
original_text = Text(middle_frame, height=15, width=35, borderwidth=4, relief="sunken", bg = 'gray1', fg = 'white', font=('Lato',11, 'bold'))
original_text.grid(row=1, column=0, pady=5, padx=5)

original_text_scrollbar = Scrollbar(middle_frame)
original_text_scrollbar.grid(row=1, column=1, sticky="ns")
original_text.configure(yscrollcommand=original_text_scrollbar.set)
original_text_scrollbar.configure(command=original_text.yview)

label2 = tk.Label(middle_frame, text='Translated Text : ',bg='white' , font = ('bold'))
label2.grid(row=0, column= 3)
translate_text = Text(middle_frame, height=15, width=35, borderwidth=4, relief="sunken", bg = 'gray1', fg = 'white', font=('Lato',11, 'bold'))
translate_text.grid(row=1, column=3, pady=5, padx=5)

translate_text_scrollbar = Scrollbar(middle_frame)
translate_text_scrollbar.grid(row=1, column=4, sticky="ns")
translate_text.configure(yscrollcommand=translate_text_scrollbar.set)
translate_text_scrollbar.configure(command=translate_text.yview)

# Language option
language_opt = ttk.Combobox(middle_frame, state='readonly', width=25, value=language_list)
language_opt.current(21)
language_opt.grid(row=2, column=0)

language_opt_trans = ttk.Combobox(middle_frame, state='readonly', width=25, value=language_list)
language_opt_trans.current(26)
language_opt_trans.grid(row=2, column=3)

#arrow icon
img = ImageTk.PhotoImage(Image.open('img/arrow.png'))
my_img = Button(middle_frame,bg= 'white',  image = img, command=translate_word, borderwidth=0, relief="ridge")
my_img.grid(row=1, column=2, padx=5)

# Button
translate_button = Button(bottom_frame, text='Translate', bg='gray1', fg = 'white', font=('Helvetica', 15, 'bold'), command=translate_word)
translate_button.grid(row=0, column=0)

clear_button = Button(bottom_frame, text='Clear', bg='gray1', fg = 'white', font=('Helvetica', 10, 'bold'), command=clear)
clear_button.grid(row=1, column=0, pady=5)


#color change

button_state = True


def color_change():
    global button_state

    if button_state:
        button_mode.config(image=off, bg='gray1')

        root.config(bg='gray1')
        top_frame.config(bg='gray1')
        middle_frame.config(bg='gray1')
        bottom_frame.config(bg='gray1')
        last_frame.config(bg='gray1')

        show_time.config(bg='gray1')
        show_day.config(bg='gray1')
        show_day.config(fg='yellowgreen')
        show_time.config(fg='yellowgreen')
        logo_out.config(bg= 'white')

        original_text.config(bg = 'white', fg = 'gray1')
        translate_text.config(bg = 'white', fg = 'gray1')
        label1.config(fg='white', bg = 'gray1')
        label2.config(fg='white', bg = 'gray1')
        my_img.config(bg = 'yellowgreen')


        translate_button.config(bg='white', fg = 'gray1')
        clear_button.config(bg='white', fg = 'gray1')

        

        button_state = False
    else:
        button_mode.config(image=on, bg='white')

        root.config(bg='white')
        top_frame.config(bg='white')
        middle_frame.config(bg='white')
        bottom_frame.config(bg='white')
        last_frame.config(bg='white')

        show_time.config(bg = 'white')
        show_day.config(bg='white')
        show_day.config(fg='gray1')
        show_time.config(fg='gray1')
        logo_out.config(bg = 'gray1')

        original_text.config(bg = 'gray1', fg = 'white')
        translate_text.config(bg = 'gray1', fg = 'white')
        label1.config(fg='gray1', bg = 'white')
        label2.config(fg='gray1', bg = 'white')
        my_img.config(bg = 'white')

        translate_button.config(bg='gray1', fg = 'white')
        clear_button.config(bg='gray1', fg = 'white')

        
        button_state = True

on = ImageTk.PhotoImage(Image.open('img/light2.png'))
off = ImageTk.PhotoImage(Image.open('img/dark2.png'))

button_mode = tk.Button(top_frame, bg= 'white', image = on, command = color_change,  borderwidth=0, relief="ridge")
button_mode.grid(row = 1, column = 2)


clock()

root.mainloop()