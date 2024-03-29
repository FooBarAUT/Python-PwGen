import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import random
import string

width = 400
height = 220

# read out state of the checkboxes and the slider, generate a random password with those values
def generate():
 chosenOnes = ""

 if letters.get():
     chosenOnes += string.ascii_letters
 if number.get():
     chosenOnes += string.digits
 if symbol.get():
     chosenOnes += string.punctuation

 result = ''.join(random.choice(chosenOnes) for i in range(slider.get()))
 var.set(result)

# draw the window and give it dimensions
# window = tk.Tk()
window = ThemedTk(theme="breeze")
window.title('PwGen')
window.geometry(str(width) + "x" + str(height))
window.minsize(width, height)
window.attributes('-topmost',True)

# create the label which will hold the password later
ent = tk.Entry(window, state='readonly', readonlybackground='white', fg='black', justify="center")
var = tk.StringVar()
var.set('choose below')
ent.config(textvariable=var, relief='flat')
ent.pack(fill="x")

# set up vars for the checkboxes
letters = tk.IntVar()
number = tk.IntVar()
symbol = tk.IntVar()

# set up checkboxes and pack them in the window
c1 = ttk.Checkbutton(window, text='letters',variable=letters, onvalue=1, offvalue=0)
c1.pack()

c2 = ttk.Checkbutton(window, text='numbers',variable=number, onvalue=1, offvalue=0)
c2.pack()

c3 = ttk.Checkbutton(window, text='symbols',variable=symbol, onvalue=1, offvalue=0)
c3.pack()

# set up slider and give it a width of 100%
slider = tk.Scale(window, from_=1, to=50, orient="horizontal")
slider.pack(fill="x")

# create button and place it
startbtn = ttk.Button(window, text = "GO", command = generate, width=10).place(relx=0.5, rely=0.8, anchor="center")

# start the main loop-di-loop
window.mainloop()