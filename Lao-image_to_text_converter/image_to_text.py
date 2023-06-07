import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract as tess
import pytesseract
tess.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def convert_image():
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    
    if file_path:
        # Open the image file
        image = Image.open(file_path)
        
        # Convert the image to grayscale
        image = image.convert("L")
        
        # Use Tesseract OCR to extract text from the image
        text = pytesseract.image_to_string(image)
        
        # Display the extracted text in the GUI
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)

# Create the main application window
window = tk.Tk()
window.title("Image to Text Converter")
window.config(bg="Pink")

# Create a button to browse and select an image file
browse_button = tk.Button(window, text="Browse Image", command=convert_image)
browse_button.pack(pady=10)

# Create a text box to display the extracted text
text_box = tk.Text(window, height=35, width=150, bd=5, font=("Arial", 15))
text_box.pack()

# Start the Tkinter event loop
window.mainloop()
