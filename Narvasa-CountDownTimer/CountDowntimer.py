import time
from tkinter import *
from tkinter import ttk, messagebox
from playsound import playsound
from threading import *
import os
import multiprocessing
import winsound

hour_list = list(range(0, 25))
min_sec_list = list(range(0, 60))

ringtone_dir = 'C:/Users/rubom/PycharmProjects/TimerProject/Ringtones'  # Directory where the ringtones are stored
ringtones = os.listdir(ringtone_dir)  # List all the ringtones in the directory


class CountDown:
    def __init__(self):
        self.time_display = None
        self.time_left = None
        self.window = root
        self.window.geometry("480x450")
        self.window.title('CountDown Timer')
        self.window.configure(bg='dark gray')
        self.window.resizable(width=False, height=False)
        self.pause = False
        self.theme = "dark"

        self.button_frame = Frame(self.window, bg="dark gray", width=240, height=40)
        self.button_frame.place(x=220, y=220)

        time_label = Label(self.window, text="", font=("times new roman", 20), bg='dark gray', fg='black')
        time_label.place(x=160, y=50)
        self.update_time(time_label)

        date_label = Label(self.window, text="", font=("times new roman", 20), bg='dark gray', fg='black')
        date_label.pack(side=TOP, pady=10)
        self.update_date(date_label)

        header_label = Label(self.window, text="CountDown Timer", font=("times new roman", 20, "bold"), bg='dark gray',
                             fg='navy')
        header_label.place(x=140, y=100)

        hour_label = Label(self.window, text="Hour", font=("times new roman", 15), bg='dark gray', fg='black')
        hour_label.place(x=50, y=140)

        minute_label = Label(self.window, text="Minute", font=("times new roman", 15), bg='dark gray', fg='black')
        minute_label.place(x=200, y=140)

        second_label = Label(self.window, text="Second", font=("times new roman", 15), bg='dark gray', fg='black')
        second_label.place(x=350, y=140)

        self.hour = IntVar()
        self.hour_combobox = ttk.Combobox(self.window, width=8, height=10, textvariable=self.hour,
                                          font=("times new roman", 15))
        self.hour_combobox['values'] = hour_list
        self.hour_combobox.current(0)
        self.hour_combobox.place(x=50, y=180)

        self.minute = IntVar()
        self.minute_combobox = ttk.Combobox(self.window, width=8, height=10, textvariable=self.minute,
                                            font=("times new roman", 15))
        self.minute_combobox['values'] = min_sec_list
        self.minute_combobox.current(0)
        self.minute_combobox.place(x=200, y=180)

        self.second = IntVar()
        self.second_combobox = ttk.Combobox(self.window, width=8, height=10, textvariable=self.second,
                                            font=("times new roman", 15))
        self.second_combobox['values'] = min_sec_list
        self.second_combobox.current(0)
        self.second_combobox.place(x=350, y=180)

        ringtone_label = Label(self.window, text="Ringtone", font=("times new roman", 15), bg='dark gray', fg='black')
        ringtone_label.place(x=350, y=10)

        self.ringtone_var = StringVar()
        self.ringtone_combobox = ttk.Combobox(self.window, width=10, height=10, textvariable=self.ringtone_var,
                                              font=("times new roman", 12), state="readonly")
        self.ringtone_combobox['values'] = ringtones
        self.ringtone_combobox.current(0)
        self.ringtone_combobox.place(x=350, y=50)

        cancel_button = Button(self.window, text='Cancel', font=("times new roman", 15), bg="dark blue", fg="white",
                               command=self.Cancel, width=15)
        cancel_button.place(x=90, y=220)

        set_button = Button(self.window, text='Set', font=("times new roman", 15), bg="dark blue", fg="white",
                            command=self.Get_Time, width=15)
        set_button.place(x=260, y=220)

        toggle_button = Button(self.window, text='Toggle Theme', font=("times new roman", 10), bg="dark blue",
                               fg="white", command=self.Toggle_Theme)
        toggle_button.place(x=10, y=20)

    def Cancel(self):
        self.pause = True
        self.window.destroy()

    def Get_Time(self):
        self.time_display = Label(self.window, font=("times new roman", 20, 'bold'), bg='dark gray', fg='navy')
        self.time_display.place(x=130, y=350)

        try:
            h = (int(self.hour_combobox.get()) * 3600)
            m = (int(self.minute_combobox.get()) * 60)
            s = (int(self.second_combobox.get()))
            self.time_left = h + m + s

            if s == 0 and m == 0 and h == 0:
                messagebox.showwarning('Warning!', 'Please select a valid time')
            else:
                start_button = Button(self.window, text='Start', font=("times new roman", 15), bg="blue", fg="white",
                                      command=self.Threading, width=15)
                start_button.place(x=100, y=280)

                pause_button = Button(self.window, text='Pause', font=("times new roman", 15), bg="blue", fg="white",
                                      command=self.pause_time, width=13)
                pause_button.place(x=250, y=280)
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")

    def Threading(self):
        x = Thread(target=self.start_time, daemon=True)
        x.start()

    def Clear_Screen(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def pause_time(self):
        self.pause = True
        mins, secs = divmod(self.time_left, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)
        self.time_display.config(text=f"Time Left: {hours}:{mins}:{secs}")
        self.time_display.update()

    def start_time(self):
        self.pause = False
        while self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)
            self.time_display.config(text=f"Time Left: {hours}:{mins:02d}:{secs:02d}")
            self.time_display.update()
            time.sleep(1)
            self.time_left = self.time_left - 1

            if self.time_left <= 0:
                selected_ringtone = self.ringtone_combobox.get()
                ringtone_path = os.path.join(ringtone_dir, selected_ringtone)
                process = multiprocessing.Process(target=playsound, args=(ringtone_path,))
                process.start()
                messagebox.showinfo('Time Over', 'Please ENTER to stop playing')
                process.terminate()
                self.Clear_Screen()

            if self.pause:
                break

    def update_time(self, label):
        current_time = time.strftime("%I:%M:%S %p")
        label.config(text=f"{current_time}")
        self.window.after(1000, lambda: self.update_time(label))

    def update_date(self, label):
        current_date = time.strftime("%B-%d-%Y")
        label.config(text=f"{current_date}")
        self.window.after(1000, lambda: self.update_date(label))

    def Toggle_Theme(self):
        if self.theme == "dark":
            self.theme = "light"
            self.window.configure(bg="white")
            for widget in self.window.winfo_children():
                if isinstance(widget, Frame):
                    widget.configure(bg="white")
                elif isinstance(widget, Label):
                    widget.configure(bg="white", fg="black")
                elif isinstance(widget, Button):
                    widget.configure(bg="blue", fg="white")
        else:
            self.theme = "dark"
            self.window.configure(bg="dark gray")
            for widget in self.window.winfo_children():
                if isinstance(widget, Frame):
                    widget.configure(bg="dark gray")
                elif isinstance(widget, Label):
                    widget.configure(bg="dark gray", fg="black")
                elif isinstance(widget, Button):
                    widget.configure(bg="dark blue", fg="white")


if __name__ == "__main__":
    root = Tk()
    obj = CountDown()
    root.mainloop()
