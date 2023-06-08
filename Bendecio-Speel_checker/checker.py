from tkinter import *
from textblob import TextBlob
import pyttsx3


def clrAll():
    word1_place.delete(0, END)
    word2_place.delete(0, END)


def crction():
    input_wrd = word1_place.get()
    blob_object = TextBlob(input_wrd)
    crctd_word = str(blob_object.correct())

    word2_place.delete(0, END)
    word2_place.insert(0, crctd_word)

    
    engine = pyttsx3.init()
    engine.say(crctd_word)
    engine.runAndWait()



if __name___== "___main__":
    base = Tk()

    base.configure(background='light green')

    base.geometry("600x500")

    base.title("Spell Corrector")

    
    headlbl = Label(base, text='Welcome to Spelling checker',
                    fg='white', bg="red", font=('times new roman', 15, 'bold'))

   
    lbl1 = Label(base, text="Input Word",
                 fg='white', bg='dark green', font=('times new roman', 15, 'bold'))

    lbl2 = Label(base, text="Corrected Word",
                 fg='white', bg='dark green', font=('times new roman', 15, 'bold'))

    headlbl.grid(row=0, column=1)
    lbl1.grid(row=1, column=0)
    lbl2.grid(row=3, column=0, padx=10)

    word1_place = Entry(width=50)
    word2_place = Entry(width=50)

    word1_place.grid(row=1, column=1, padx=10, pady=10)
    word2_place.grid(row=3, column=1, padx=10, pady=10)

    btn1 = Button(base, text="Correction", bg="red", fg="white", font=('times new roman', 15, 'bold'),
                  command=crction)
    btn1.grid(row=2, column=1)

    btn2 = Button(base, text="Clear", bg="red",
                  fg="white", command=clrAll, font=('times new roman', 15, 'bold'))
    btn2.grid(row=5, column=1)

    base.mainloop()