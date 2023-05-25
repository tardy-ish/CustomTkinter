import sys
sys.path.append("../customtkinter")
import customtkinter as ctk
import tkinter as tk

app = ctk.CTk()

app.geometry("400x300")




def open_box():
    ctk.CTkConfirmationBox(yes=_yes_event,no=_no_event)

def _yes_event():
    print("This is when the yes button gets pressed")

def _no_event():
    print("This is when the no button gets pressed")

button = ctk.CTkButton(master=app,text="open confirmation box",command=open_box)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


app.mainloop()