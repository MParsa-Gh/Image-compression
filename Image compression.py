from PIL import Image
from tkinter.filedialog import *
from customtkinter import *

root = CTk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Image compression app")


about_text = """
Just select an image and save it !

Version : 1.1.9
Developed by MParsa
Github : github.com/MParsa-Gh
"""
label_about_text = CTkLabel(master=root, text=about_text, justify="left",
                            font=CTkFont(size=18), corner_radius=20, width=200, anchor="w",)
label_about_text.place(anchor="center", x=235, y=315)

label_about = CTkLabel(
    master=root, text="About this app", font=CTkFont(size=18, weight="bold"),)
label_about.place(anchor="center", x=162, y=230)

notification_entry = CTkEntry(
    root, width=400, height=150, state="disabled", font=CTkFont(size=18), justify="center")
notification_entry.place(anchor="center", x=600/2, y=120)


def update_notification(message):
    notification_entry.configure(state="normal")
    notification_entry.delete(0, "end")
    notification_entry.insert(0, message)
    notification_entry.configure(state="disabled")


def compression():
    try:
        file_path = askopenfilename()
        if not file_path:
            update_notification("No file were selected")
            return

        img = Image.open(file_path)
        myHeight, myWidth = img.size

        img = img.resize((myHeight, myWidth), Image.Resampling.LANCZOS)

        save_path = asksaveasfilename()
        img.save(save_path+"_compressed.JPG")
        if not save_path:
            update_notification("The save path was not selected.")
            return

        update_notification("The operation was successful!")

    except:
        update_notification("An error occurred, please select JPG file.")


Button_ = CTkButton(master=root, width=220, height=50,
                    corner_radius=5, text="Image compress", font=CTkFont(size=25, weight="bold"), command=compression)
Button_.place(anchor="center", x=600/2, y=50)


root.mainloop()
