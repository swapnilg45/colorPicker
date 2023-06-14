"""pip install PIL, cv2, numpy before running the script """

from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np


def click_event(event, x, y , flags, params):
    """
    Allows user to click on the image and displays the RGB value of that specific point.
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = '( '+str(red) + ', ' + str(blue) + ', ' + str(green)+ ' )'
        print(strBGR)
        text.delete(0, END)
        text.insert(END, strBGR)
        root.update_idletasks()

def show_values(file_name):
    """
    Opens a new window containing the image selected. 
    """
    img1 = cv2.imread(file_name)
    global img
    img = cv2.resize(img1, (521, 521))


    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def showImage():
    """
    Displays the image of the thumbnail in a 350*350 frame. 
    """
    fln = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select Image File',
                                      filetypes = (("All Files", "."), ("png files", ".png"), ("jpg files", ".jpg")))
    img = Image.open(fln)
    img.thumbnail((350, 350))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image = img)
    lbl.image = img
    root.update_idletasks()
    show_values(fln)



## UI Area
root = Tk()

frm = Frame(root)
frm.pack(side = BOTTOM, padx = 15, pady = 15)

lbl = Label(root)
lbl.pack()

btn = Button(frm, text = 'Browse Image', command = showImage)
btn.pack(side = tk.BOTTOM)


lbl2 = Label(frm, text = "RGB Values :")
lbl2.pack(side = tk.LEFT, pady = 10)

text = Entry(frm)
text.pack(side = BOTTOM, pady = 10)

root.title("Image Browser")
root.geometry('400x400')

root.mainloop()
