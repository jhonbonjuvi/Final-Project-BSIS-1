import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Define custom font
font = ("Helvetica", 18, "bold")

label = tk.Label(window, text="EDIT TEXT HERE", font=font)
label.pack()


def bold_text():
    if not txt_edit.tag_ranges(tk.SEL):
        return

    current_tag = "bold"
    txt_edit.tag_configure(current_tag, font=("TkDefaultFont", font_size.get(), "bold"))

    current_selection = txt_edit.tag_ranges(tk.SEL)

    txt_edit.tag_add(current_tag, current_selection[0], current_selection[1])


def unbold_text():
    if not txt_edit.tag_ranges(tk.SEL):
        return

    txt_edit.tag_remove("bold", tk.SEL_FIRST, tk.SEL_LAST)


def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt")
    if not filepath:
        return
    with open(filepath, "w") as file:
        file.write(txt_edit.get("1.0", tk.END))


txt_edit = tk.Text(window, font=("TkDefaultFont", 14), spacing3=2)
txt_edit.pack()
fr_buttons = tk.Frame(window)

txt_edit.pack(side="left", fill="both", expand=True)
fr_buttons.pack(side="right", fill="both")

btn_open = tk.Button(fr_buttons, text='Open', font=font)
btn_save = tk.Button(fr_buttons, text="Save As", font=font, command=save_file)

font_size = tk.IntVar(value=14)

font_size_label = tk.Label(window, text="Font Size:", font=font)
font_size_label.pack()

font_size_slider = tk.Scale(window, from_=8, to=48, variable=font_size, orient="horizontal")
font_size_slider.pack()

bold_button = tk.Button(window, text="Bold", font=font, command=bold_text)
bold_button.pack()

btn_save.pack()

unbold_button = tk.Button(window, text="Unbold", font=font, command=unbold_text)
unbold_button.pack()

window.mainloop()