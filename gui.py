import tkinter as tk
from tkinter import filedialog, messagebox
from test import classify
def show_alert(message):
    messagebox.showinfo("Output", message)

def get_file_path():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    value = classify(file_path)
    if file_path:
        txt = f"Image Belongs to : {value[0]} \nAccuraccy: {str(round(value[1]*100))}"
        show_alert(txt)
    else:
        show_alert("No file selected")

root = tk.Tk()
root.title("Banana Type Finder")

select_button = tk.Button(root, text="Select Image", command=get_file_path)
select_button.pack(pady=20)

root.mainloop()
