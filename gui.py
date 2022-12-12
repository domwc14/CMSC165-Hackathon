import tkinter as tk
from tkinter import filedialog
from tkinter import *
import cv2
from PIL import Image, ImageTk
import numpy as np

global text 
text = "Pollinated"
def select_image():

    path = filedialog.askopenfilename()

    if path:

        image = cv2.imread(path, 1)

        data = image.shape

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lw_range = np.array([0, 0, 0])
        up_range = np.array([255, 255, 255])

        mask = cv2.inRange(hsv, lw_range, up_range)
        res = cv2.bitwise_and(image, image, mask= mask)

        image = Image.fromarray(res).resize((600,600), Image.ANTIALIAS)

        image = ImageTk.PhotoImage(image)
        label_img = tk.Label(app, image=image, relief=tk.SOLID)
        label_img.image = image
        label_img.place(x=400, y=150)


def modify_image(name, value):
    print(name, value)
    
def detect_image(): #function to display altered image
    path = filedialog.askopenfilename()

    if path:

        image = cv2.imread(path, 1)

        data = image.shape

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lw_range = np.array([0, 0, 0])
        up_range = np.array([255, 255, 255])

        mask = cv2.inRange(hsv, lw_range, up_range)
        res = cv2.bitwise_and(image, image, mask= mask)

        image = Image.fromarray(res).resize((600,600), Image.ANTIALIAS)

        image = ImageTk.PhotoImage(image)
        label_img = tk.Label(app, image=image, relief=tk.SOLID)
        label_img.image = image 
        label_img.place(x=1200, y=150)


app = tk.Tk()

width = app.winfo_screenwidth()
height = app.winfo_screenheight()

app.geometry('{}x{}'.format(width, height))

btn = tk.Button(app, text="Select Image", command=select_image, width=12)
btn.place(x=150, y=600)

btn = tk.Button(app, text="Detect Image", command=detect_image, width=12)
btn.place(x=150, y=640)

label1 = tk.Label(app, text='HSV', width=7, height=2)
label1.place(x=50, y=160)

hsv= tk.StringVar()
w1 = tk.Scale(app, from_=0, to=1, orient=tk.HORIZONTAL, variable=hsv, width=15, command=lambda value:modify_image('h_min', value))
w1.place(x=150, y=150)

label2 = tk.Label(app, text='L-H', width=7, height=2)
label2.place(x=50, y=210)

l_h= tk.StringVar()
w2 = tk.Scale(app, from_=0, to=255, orient=tk.HORIZONTAL, variable=l_h, width=15, command=lambda value:modify_image('s_min', value))
w2.place(x=150, y=200)


label3 = tk.Label(app, text='L-S', width=7, height=2)
label3.place(x=50, y=260)

l_s= tk.StringVar()
w3 = tk.Scale(app, from_=0, to=255, orient=tk.HORIZONTAL, variable=l_s, width=15, command=lambda value:modify_image('v_min', value))
w3.place(x=150, y=250)

label4 = tk.Label(app, text='L-V', width=7, height=2)
label4.place(x=50, y=310)

l_v= tk.StringVar()
w4 = tk.Scale(app, from_=0, to=255, orient=tk.HORIZONTAL, variable=l_v, width=15, command=lambda value:modify_image('v_min', value))
w4.place(x=150, y=300)

label5 = tk.Label(app, text='U-H', width=7, height=2)
label5.place(x=50, y=360)

u_h= tk.StringVar()
w5 = tk.Scale(app, from_=0, to=255, orient=tk.HORIZONTAL, variable=u_h, width=15, command=lambda value:modify_image('v_min', value))
w5.place(x=150, y=350)


label6 = tk.Label(app, text='U-S', width=7, height=2)
label6.place(x=50, y=410)

u_s= tk.StringVar()
w6 = tk.Scale(app, from_=0, to=255, orient=tk.HORIZONTAL, variable=u_s, width=15, command=lambda value:modify_image('v_min', value))
w6.place(x=150, y=400)

label7 = tk.Label(app, text='U-V', width=7, height=2)
label7.place(x=50, y=460)

u_v= tk.StringVar()
w7 = tk.Scale(app, from_=0, to=255, orient=tk.HORIZONTAL, variable=u_v, width=15, command=lambda value:modify_image('v_min', value))
w7.place(x=150, y=450)

label8 = tk.Label(app, text='Gaussian Blur', width=20, height=2)
label8.place(x=10, y=510)

g_blur= tk.StringVar()
w8 = tk.Scale(app, from_=0, to=1, orient=tk.HORIZONTAL, variable=g_blur, width=15, command=lambda value:modify_image('v_min', value))
w8.place(x=150, y=500)



label9 = tk.Label(app, text=text, width=7, height=2)
label9.place(x=50, y=700)

app.mainloop()