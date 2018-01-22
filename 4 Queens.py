

from tkinter import *
from tkinter import messagebox
import random

count = 0
count1 = 0
x=0
y=0
root = Tk()

frame=Frame(root)

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

def s1():
  global count
  count+=1
  btn1.configure(bg="red")
  btn1.configure(state="disabled")
  btn2.configure(state="disabled")
  btn3.configure(state="disabled")
  btn4.configure(state="disabled")
  btn5.configure(state="disabled")
  btn6.configure(state="disabled")
  btn9.configure(state="disabled")
  btn13.configure(state="disabled")
  btn11.configure(state="disabled")
  btn16.configure(state="disabled")
  check()

  
def s2():

  global count
  count+=1
  btn2.configure(bg="red")
  btn2.configure(state="disabled")
  btn1.configure(state="disabled")
  btn3.configure(state="disabled")
  btn4.configure(state="disabled")
  btn6.configure(state="disabled")
  btn10.configure(state="disabled")
  btn14.configure(state="disabled")
  btn5.configure(state="disabled")
  btn7.configure(state="disabled")
  btn12.configure(state="disabled")
  check()

def s3():

  global count
  count+=1
  btn3.configure(bg="red")
  btn3.configure(state="disabled")
  btn1.configure(state="disabled")
  btn2.configure(state="disabled")
  btn4.configure(state="disabled")
  btn7.configure(state="disabled")
  btn11.configure(state="disabled")
  btn15.configure(stat="disabled")
  btn8.configure(state="disabled")
  btn6.configure(state="disabled")
  btn9.configure(state="disabled")
  check()

def s4():

  global count
  count+=1
  btn4.configure(bg="red")
  btn4.configure(state="disabled")
  btn1.configure(state="disabled")
  btn2.configure(state="disabled")
  btn3.configure(state="disabled")
  btn8.configure(state="disabled")
  btn12.configure(state="disabled")
  btn16.configure(state="disabled")
  btn7.configure(state="disabled")
  btn10.configure(state="disabled")
  btn13.configure(state="disabled")
  check()

def s5():

  global count
  count+=1
  btn5.configure(bg="red")
  btn5.configure(state="disabled")
  btn1.configure(state="disabled")
  btn6.configure(state="disabled")
  btn7.configure(state="disabled")
  btn8.configure(state="disabled")
  btn9.configure(state="disabled")
  btn13.configure(state="disabled")
  btn2.configure(state="disabled")
  btn10.configure(state="disabled")
  btn15.configure(state="disabled")
  check()
  
def s6():

  global count
  count+=1
  btn6.configure(bg="red")
  btn6.configure(state="disabled")
  btn5.configure(state="disabled")
  btn2.configure(state="disabled")
  btn10.configure(state="disabled")
  btn14.configure(state="disabled")
  btn5.configure(state="disabled")
  btn7.configure(state="disabled")
  btn8.configure(state="disabled")
  btn1.configure(state="disabled")
  btn9.configure(state="disabled")
  btn11.configure(state="disabled")
  btn16.configure(state="disabled")
  btn3.configure(state="disabled")
  check()

def s7():

  global count
  count+=1
  btn7.configure(bg="red")
  btn7.configure(state="disabled")
  btn3.configure(state="disabled")
  btn5.configure(state="disabled")
  btn6.configure(state="disabled")
  btn2.configure(state="disabled")
  btn4.configure(state="disabled")
  btn8.configure(state="disabled")
  btn11.configure(state="disabled")
  btn15.configure(state="disabled")
  btn10.configure(state="disabled")
  btn13.configure(state="disabled")
  btn12.configure(state="disabled")
  check()

def s8():

  global count
  count+=1
  btn8.configure(bg="red")
  btn8.configure(state="disabled")
  btn3.configure(state="disabled")
  btn4.configure(state="disabled")
  btn5.configure(state="disabled")
  btn6.configure(state="disabled")
  btn7.configure(state="disabled")
  btn12.configure(state="disabled")
  btn16.configure(state="disabled")
  btn11.configure(state="disabled")
  btn14.configure(state="disabled")
  check()

def s9():

  global count
  count+=1
  btn9.configure(bg="red")
  btn9.configure(state="disabled")
  btn1.configure(state="disabled")
  btn3.configure(state="disabled")
  btn5.configure(state="disabled")
  btn13.configure(state="disabled")
  btn6.configure(state="disabled")
  btn3.configure(state="disabled")
  btn8.configure(state="disabled")
  btn10.configure(state="disabled")
  btn11.configure(state="disabled")
  btn12.configure(state="disabled")
  btn6.configure(state="disabled")
  btn3.configure(state="disabled")
  btn14.configure(state="disabled")
  check()

def s10():

  global count
  count+=1
  btn10.configure(bg="red")
  btn10.configure(state="disabled")
  btn2.configure(state="disabled")
  btn4.configure(state="disabled")
  btn5.configure(state="disabled")
  btn6.configure(state="disabled")
  btn7.configure(state="disabled")
  btn14.configure(state="disabled")
  btn9.configure(state="disabled")
  btn11.configure(state="disabled")
  btn12.configure(state="disabled")
  btn12.configure(state="disabled")
  btn13.configure(state="disabled")
  btn15.configure(state="disabled")
  check()

def s11():

  global count
  count+=1
  btn11.configure(bg="red")
  btn11.configure(state="disabled")
  btn3.configure(state="disabled")
  btn7.configure(state="disabled")
  btn15.configure(state="disabled")
  btn9.configure(state="disabled")
  btn10.configure(state="disabled")
  btn12.configure(state="disabled")
  btn1.configure(state="disabled")
  btn6.configure(state="disabled")
  btn16.configure(state="disabled")
  btn8.configure(state="disabled")
  btn14.configure(state="disabled")
  check()
  
def s12():

  global count
  count+=1
  btn12.configure(bg="red")
  btn12.configure(state="disabled")
  btn4.configure(state="disabled")
  btn8.configure(state="disabled")
  btn16.configure(state="disabled")
  btn9.configure(state="disabled")
  btn10.configure(state="disabled")
  btn11.configure(state="disabled")
  btn2.configure(state="disabled")
  btn7.configure(state="disabled")
  btn15.configure(state="disabled")
  check()
  
def s13():

  global count
  count+=1
  btn13.configure(bg="red")
  btn13.configure(state="disabled")
  btn1.configure(state="disabled")
  btn3.configure(state="disabled")
  btn9.configure(state="disabled")
  btn14.configure(state="disabled")
  btn15.configure(state="disabled")
  btn16.configure(state="disabled")
  btn4.configure(state="disabled")
  btn7.configure(state="disabled")
  btn10.configure(state="disabled")
  check()

def s14():

  global count
  count+=1
  btn14.configure(bg="red")
  btn14.configure(state="disabled")
  btn2.configure(state="disabled")
  btn6.configure(state="disabled")
  btn10.configure(state="disabled")
  btn13.configure(state="disabled")
  btn15.configure(state="disabled")
  btn16.configure(state="disabled")
  btn9.configure(state="disabled")
  btn11.configure(state="disabled")
  btn8.configure(state="disabled")
  check()

def s15():

  global count
  count+=1
  btn15.configure(bg="red")
  btn15.configure(state="disabled")
  btn3.configure(state="disabled")
  btn7.configure(state="disabled")
  btn11.configure(state="disabled")
  btn13.configure(state="disabled")
  btn14.configure(state="disabled")
  btn16.configure(state="disabled")
  btn5.configure(state="disabled")
  btn10.configure(state="disabled")
  btn12.configure(state="disabled")
  check()

def s16():

  global count
  count+=1
  btn16.configure(bg="red")
  btn16.configure(state="disabled")
  btn4.configure(state="disabled")
  btn8.configure(state="disabled")
  btn12.configure(state="disabled")
  btn13.configure(state="disabled")
  btn14.configure(state="disabled")
  btn15.configure(state="disabled")
  btn1.configure(state="disabled")
  btn6.configure(state="disabled")
  btn11.configure(state="disabled")
  check()

def s17():
  reset()


btn1 = Button(frame,text="1",command=s1)
btn1.grid(column=0, row=0, sticky=N+S+E+W)
orig_color = btn1.cget("background")
btn2 = Button(frame,text="2",command=s2)
btn2.grid(column=1, row=0, sticky=N+S+E+W)
btn3 = Button(frame,text="3",command=s3)
btn3.grid(column=2, row=0, sticky=N+S+E+W)
btn4 = Button(frame,text="4",command=s4)
btn4.grid(column=3, row=0, sticky=N+S+E+W)
btn5 = Button(frame,text="5",command=s5)
btn5.grid(column=0, row=1, sticky=N+S+E+W)
btn6 = Button(frame,text="6",command=s6)
btn6.grid(column=1, row=1, sticky=N+S+E+W)
btn7 = Button(frame,text="7",command=s7)
btn7.grid(column=2, row=1, sticky=N+S+E+W)
btn8 = Button(frame,text="8",command=s8)
btn8.grid(column=3, row=1, sticky=N+S+E+W)
btn9 = Button(frame,text="9",command=s9)
btn9.grid(column=0, row=2, sticky=N+S+E+W)
btn10 = Button(frame,text="10",command=s10)
btn10.grid(column=1, row=2, sticky=N+S+E+W)
btn11 = Button(frame,text="11",command=s11)
btn11.grid(column=2, row=2, sticky=N+S+E+W)
btn12= Button(frame,text="12",command=s12)
btn12.grid(column=3, row=2, sticky=N+S+E+W)
btn13= Button(frame,text="13",command=s13)
btn13.grid(column=0, row=3, sticky=N+S+E+W)
btn14= Button(frame,text="14",command=s14)
btn14.grid(column=1, row=3, sticky=N+S+E+W)
btn15= Button(frame,text="15",command=s15)
btn15.grid(column=2, row=3, sticky=N+S+E+W)
btn16= Button(frame,text="16",command=s16)
btn16.grid(column=3, row=3, sticky=N+S+E+W)
btn17= Button(frame,text="reset",command=s17)
btn17.grid(column=0, row=4, sticky=N+S+E+W)


def check():
  if count==4:
    messagebox.showinfo("you won ")
    reset()
    
def reset():
  btn1.configure(state="normal")
  btn2.configure(state="normal")
  btn3.configure(state="normal")
  btn4.configure(state="normal")
  btn5.configure(state="normal")
  btn6.configure(state="normal")
  btn7.configure(state="normal")
  btn8.configure(state="normal")
  btn9.configure(state="normal")
  btn10.configure(state="normal")
  btn11.configure(state="normal")
  btn12.configure(state="normal")
  btn13.configure(state="normal")
  btn14.configure(state="normal")
  btn15.configure(state="normal")
  btn16.configure(state="normal")
  btn1.configure(background=orig_color)
  btn2.configure(background=orig_color)
  btn3.configure(background=orig_color)
  btn4.configure(background=orig_color)
  btn5.configure(background=orig_color)
  btn6.configure(background=orig_color)
  btn7.configure(background=orig_color)
  btn8.configure(background=orig_color)
  btn9.configure(background=orig_color)
  btn10.configure(background=orig_color)
  btn11.configure(background=orig_color)
  btn12.configure(background=orig_color)
  btn13.configure(background=orig_color)
  btn14.configure(background=orig_color)
  btn15.configure(background=orig_color)
  btn16.configure(background=orig_color)




for x in range(10):
  Grid.columnconfigure(frame, x, weight=1)

for y in range(5):
  Grid.rowconfigure(frame, y, weight=1)

root.mainloop()




