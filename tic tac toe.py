from tkinter import *
import tkinter.messagebox
root = Tk()
root.title("Tic Tac Toe")
root.resizable(False,False)
count = 0
k = 1

but1 = StringVar()        
but2 = StringVar()
but3 = StringVar()
but4 = StringVar()
but5 = StringVar()
but6 = StringVar()
but7 = StringVar()
but8 = StringVar()
but9 = StringVar()
v = []
for i in range(0, 10):
    v.append(0)

def game():
    global k
    k = 1
    button1 = Button(root, height=10, width=18, textvariable=but1, bd=0.75, bg="light green", command=lambda: enter(1,but1))
    button2 = Button(root, height=10, width=18, textvariable=but2, bd=0.75, bg="yellow", command=lambda: enter(2,but2))
    button3 = Button(root, height=10, width=18, textvariable=but3, bd=0.75, bg="light green", command=lambda: enter(3,but3))
    button4 = Button(root, height=10, width=18, textvariable=but4, bd=0.75, bg="yellow", command=lambda: enter(4,but4))
    button5 = Button(root, height=10, width=18, textvariable=but5, bd=0.75, bg="light green", command=lambda: enter(5,but5))
    button6 = Button(root, height=10, width=18, textvariable=but6, bd=0.75, bg="yellow", command=lambda: enter(6,but6))
    button7 = Button(root, height=10, width=18, textvariable=but7, bd=0.75, bg="light green", command=lambda: enter(7,but7))
    button8 = Button(root, height=10, width=18, textvariable=but8, bd=0.75, bg="yellow", command=lambda: enter(8,but8))
    button9 = Button(root, height=10, width=18, textvariable=but9, bd=0.75, bg="light green", command=lambda: enter(9,but9))
    button10 = Button(root, text="Clear", command=clear, bg="light yellow")
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)
    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)
    button10.grid(row=3, column=1)

def enter(pos,but):
    global k, count, v
    if k == 1 and v[pos] == 0:
        but.set("X")
        k = 0
        v[pos] = 1
        count = count+1
    elif k == 0 and v[pos] == 0:
        but.set("O")
        k = 1
        v[pos] = 1
        count = count+1
    win()

def clear():
    global count,i
    but1.set("")
    but2.set("")
    but3.set("")
    but4.set("")
    but5.set("")
    but6.set("")
    but7.set("")
    but8.set("")
    but9.set("")
    count=0
    for i in range(0,10):
        v[i]=0
    game()
def win():
    global k, count
    if(but1.get() == 'X' and but2.get() == "X" and but3.get() == 'X' or
       but1.get() == 'X' and but4.get() == "X" and but7.get() == 'X' or
       but1.get() == 'X' and but5.get() == "X" and but9.get() == 'X' or
       but2.get() == 'X' and but5.get() == "X" and but8.get() == 'X' or
       but3.get() == 'X' and but6.get() == "X" and but9.get() == 'X' or
       but4.get() == 'X' and but5.get() == "X" and but6.get() == 'X' or
       but3.get() == 'X' and but5.get() == "X" and but7.get() == 'X' or
       but7.get() == 'X' and but8.get() == "X" and but9.get() == 'X'):
        tkinter.messagebox.showinfo("tic tac toe", "X Wins")
        k = 1
        clear()
    if(but1.get() == 'O' and but2.get() == "O" and but3.get() == 'O' or
       but1.get() == 'O' and but4.get() == "O" and but7.get() == 'O' or
       but1.get() == 'O' and but5.get() == "O" and but9.get() == 'O' or
       but2.get() == 'O' and but5.get() == "O" and but8.get() == 'O' or
       but3.get() == 'O' and but6.get() == "O" and but9.get() == 'O' or
       but4.get() == 'O' and but5.get() == "O" and but6.get() == 'O' or
       but3.get() == 'O' and but5.get() == "O" and but7.get() == 'O' or
       but7.get() == 'O' and but8.get() == "O" and but9.get() == 'O'):
        tkinter.messagebox.showinfo("tic tac toe", "O Wins")
        k = 0
        clear()
    if count == 9:
        tkinter.messagebox.showinfo("tic tac toe", "Tie Game")
        k = 1
        clear()
game()
root.mainloop()
