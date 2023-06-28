# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import ttk
import os

root=Tk()
root.title("Image Viewer")
root.geometry("666x666")
root.configure(bg="medium orchid")

label_img = Label(root, bg="white", highlightthickness=5)
label_img.place(relx=0.5, rely=0.5, anchor=CENTER)

label_direct = Label(root, bg = "black", fg = "white", text = "Direction ::  ")
label_direct.place(relx = 0.3, rely = 0.8, anchor = CENTER)

directions = ["Left", "Right", "Up", "Down"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = directions, textvariable = selectedval)

img_path = ""

def openImg():
    global img_path
    img_path = filedialog.askopenfilename(title = "Open Image File", filetypes = [{"Image File", "*.jpg *.gif *.png *.jpeg"}])
    print(img_path)
    image = Image.open(img_path)
    img = ImageTk.PhotoImage(image)
    name = os.path.basename(img_path)
    formatted_name = name.split('.')[0]
    root.title(formatted_name)
    label_img["image"] = img
    img.close()

def rotateimg():
    global img_path
    directions = selectedval.get()
    
    if(directions == "Left"):
        image = Image.open(img_path)
        img = ImageTk.PhotoImage(image.rotate(270))
        print(img_path)
        label_img["image"] = img
        img.close()
    
    elif(directions == "Rights"):
        image = Image.open(img_path)
        img = ImageTk.PhotoImage(image.rotate(90))
        print(img_path)
        label_img["image"] = img
        img.close()
    
    elif(directions == "Up"):
        image = Image.open(img_path)
        img = ImageTk.PhotoImage(image.rotate(180))
        print(img_path)
        label_img["image"] = img
        img.close()
    
    elif(directions == "Down"):
        image = Image.open(img_path)
        img = ImageTk.PhotoImage(image.rotate(0))
        print(img_path)
        label_img["image"] = img
        img.close()

open_btn = Button(root, text="Open Image", bg="Grey", fg="white", font={"Times New Roman", 15, "bold"}, padx=15, pady=10, relief=SOLID, command=openImg)
open_btn.place(relx=0.5, rely=0.1, anchor = CENTER)

rotate_btn = Button(root, text="Rotate Image", bg="Grey", fg="white", font={"Times New Roman", 15, "bold"}, padx=15, pady=10, relief=SOLID, command=openImg)
rotate_btn.place(relx=0.5, rely=0.9, anchor = CENTER)

root.mainloop()