from keras.models import _clone_functional_model, load_model
import tkinter as tk
from tkinter import *
from PIL import Image, ImageGrab
import numpy as np
from numpy.lib.shape_base import column_stack
import win32gui

model = load_model('mnist.h5')

def predict_digit(img):
    img = img.resize((28, 28))
    img = img.convert('L')
    img = np.array(img)
    img = img.reshape(1,28,28,1)
    img = img/255.0

    res = model.predict([img])[0]
    print("Цифра - ", np.argmax(res), max(res))

image_path = r'C:\\Users\\Pechka\\Desktop\\dataScience\\2.png'
img = Image.open(image_path)
img = img.crop((530, 800, 635, 925))
# img.show()
predict_digit(img)




# class App(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)

#         self.x = self.y = 0

#         self.canvas = tk.Canvas(self, width=300, height=300, bg="white", cursor="cross")
#         self.label = tk.Label(self, text="Ожидание...", font=("Helvetica", 48))
#         self.classify_btn = tk.Button(self, text="Расознать", command=self.classify_handwritting)
#         self.button_clear = tk.Button(self, text="Очистить", command=self.clear_all)

#         self.canvas.grid(row=0, column=0, pady=2, sticky=W)
#         self.label.grid(row=0, column=1, pady=2, padx=2)
#         self.classify_btn.grid(row=1, column=1, padx=2)
#         self.button_clear.grid(row=1, column=0, pady=2)

#         self.canvas.bind("<B1-Motion>", self.draw_line)

#     def clear_all(self):
#         self.canvas.delete("all")

#     def classify_handwritting(self):
#         HWND = self.canvas.winfo_id()
#         rect = win32gui.GetWindowRect(HWND)
#         im = ImageGrab.grab(rect)

#         digit, acc = predict_digit(im)
#         self.label.configure(text=str(digit)+', ' + str(int(acc*100)) + '%')

#     def draw_line(self, event):
#         self.x = event.x
#         self.y = event.y
#         r=8
#         self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='black')

# app = App()
# mainloop()