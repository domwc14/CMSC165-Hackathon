import tkinter as tk
from tkinter import filedialog
from tkinter import *
import cv2
from PIL import Image, ImageTk
import numpy as np

global text 
text = "Pollinated"

def nothing(x):
    pass

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
        sample_text.insert(0, "Detected: ")
        f = open("test_file.txt", "w")
        f.write("Detected: 3")
        f.close()

app = tk.Tk()

width = app.winfo_screenwidth()
height = app.winfo_screenheight()

app.geometry('{}x{}'.format(width, height))


#(win, text="Button-1",height= 5, width=10).pack()
btn = tk.Button(app, text="Select Image", command=select_image, width=12)
btn.place(x=150, y=600)

btn = tk.Button(app, text="Detect Image", command=detect_image, width=12)
btn.place(x=150, y=640)

#textbox below the buttons
sample_text = tk.Entry(app)
sample_text.place(x=150, y=690)
#sample_text.config(state=DISABLED)


window_name = "Trackbars"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
cv2.resizeWindow(window_name,300,40) #w,h
cv2.createTrackbar("L - H", window_name, 0, 179, nothing)
cv2.createTrackbar("L - S", window_name, 0, 255, nothing)
cv2.createTrackbar("L - V", window_name, 0, 255, nothing)
cv2.createTrackbar("U - H", window_name, 179, 179, nothing)
cv2.createTrackbar("U - S", window_name, 255, 255, nothing)
cv2.createTrackbar("U - V", window_name, 255, 255, nothing)

# while True:
#     l_h = cv2.getTrackbarPos("L - H", window_name)
#     l_s = cv2.getTrackbarPos("L - S", window_name)
#     l_v = cv2.getTrackbarPos("L - V", window_name)
#     u_h = cv2.getTrackbarPos("U - H", window_name)
#     u_s = cv2.getTrackbarPos("U - S", window_name)
#     u_v = cv2.getTrackbarPos("U - V", window_name)

app.mainloop()