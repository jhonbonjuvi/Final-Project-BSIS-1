import tkinter as tk
import winsound
from tkinter import messagebox

# Create a Tkinter window
window = tk.Tk()
window.title("Bulb")
window.geometry("400x800")
window.configure(bg="black")

# Load bulb images
on_image = tk.PhotoImage(file="C:/Users/rubom/PycharmProjects/bulbProject/bulb_on.png")
off_image = tk.PhotoImage(file="C:/Users/rubom/PycharmProjects/bulbProject/bulb_off.png")

exit_sound = "C:/Users/rubom/PycharmProjects/bulbProject/click.wav"

header_label = tk.Label(window, text="UV TORCH LIGHT", font=("Times New Roman", 20, "bold"), bg="red", fg="black")
header_label.pack(pady=10)

# Create a frame for the bulb image and shadow slider
bulb_frame = tk.Frame(window, bg="black")
bulb_frame.pack(pady=20)

# Create a label to display the bulb image
bulb_label = tk.Label(bulb_frame, image=off_image, bg="black", width=500, height=400)
bulb_label.pack()


# Function to update the shadow effect based on the slider value
def update_shadow(intensity):
    intensity = int(intensity)
    shadow_color = "#%02x%02x%02x" % (intensity, 0, intensity)  # Ultraviolet color
    bulb_label.config(bg=shadow_color)


# Function to turn the bulb on
def turn_on():
    bulb_label.config(image=on_image)
    toggle_button_off.config(state=tk.NORMAL)
    toggle_button_on.config(state=tk.DISABLED)
    update_shadow(shadow_slider.get())


# Function to turn the bulb off
def turn_off():
    bulb_label.config(image=off_image)
    toggle_button_on.config(state=tk.NORMAL)
    toggle_button_off.config(state=tk.DISABLED)
    update_shadow(shadow_slider.get())


def exit_application():
    play_exit_sound()
    confirm_exit = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm_exit:
        window.quit()


def play_exit_sound():
    winsound.PlaySound(exit_sound, winsound.SND_ASYNC)


shadow_frame = tk.Frame(window, bg="black")
shadow_frame.pack(pady=10)

# Create a button to turn the bulb on
toggle_button_on = tk.Button(shadow_frame, text="ON", command=turn_on, fg="red", font=("Georgia", 12, "bold"))
toggle_button_on.pack(side=tk.LEFT, padx=10)

# Create a button to turn the bulb off
toggle_button_off = tk.Button(shadow_frame, text="OFF", command=turn_off, state=tk.DISABLED, fg="red",
                              font=("Georgia", 12, "bold"))
toggle_button_off.pack(side=tk.LEFT, padx=10)

# Create a slider to adjust the shadow intensity
shadow_slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, length=200, command=update_shadow, bg="red")
shadow_slider.pack(pady=10)

# Create a button to exit the application
exit_button = tk.Button(window, text="Exit", command=exit_application, fg="red", font=("Georgia", 12, "bold"))
exit_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
