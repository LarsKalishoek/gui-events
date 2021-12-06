import tkinter

window = tkinter.Tk()
window.title("Clicker")
window.config(bg = "grey")
window.geometry("350x200")
count = tkinter.IntVar()
count = 0


def f_add():
    global count, counter
    count += 1
    counter.configure(text= str(count))



add = tkinter.Button(
    window,
    text = "Up",
    width= 35,
    height=2,
    command=f_add
)
add.pack()
add.place(anchor= "center", x= 175, y= 50)

def f_minus():
    global count
    count -= 1
    counter.configure(text= str(count))

minus = tkinter.Button(
    window,
    text = "Down",
    width = 35,
    height= 2,
    command= f_minus
)
minus.pack()
minus.place(anchor= "center", x= 175 ,y= 150)

counter = tkinter.Label(
    window,
    text= count,
    width= 35,
    height= 2,
)
counter.pack()
counter.place(anchor="center", x = 175, y = 100)


def calc(event):
    if count > 0:
        window.config(bg = "green")
    elif count < 0 :
        window.config(bg= "red")
    else:
        window.config(bg= "grey")

def leave(event):
    window.config(bg= "grey")


counter.bind("<Enter>", calc)
counter.bind("<Leave>", leave)
window.mainloop()