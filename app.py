from tkinter import *


win = Tk()

win.title("calculate")
win.minsize(350, 600)
win.maxsize(350, 600)
text_input = StringVar()
# text_input2=StringVar()
operator = ""
history = []


text_display = Entry(
    win, bg="gray", textvariable=text_input, bd=25, font=("arial", "20", "italic")
)
text_display.grid(row=1, columnspan=5)

# text_display2 = Entry(
#     win, bg="gray", textvariable=text_input2,bd=25,font=("arial", "20", "italic")
# ).grid(row=0, columnspan=5)


btn_7 = Button(
    win,
    text="7",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("7"),
).grid(row=2, column=0)
btn_8 = Button(
    win,
    text="8",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("8"),
).grid(row=2, column=1)
btn_9 = Button(
    win,
    text="9",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("9"),
).grid(row=2, column=2)
btn_plus = Button(
    win,
    text="+",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("+"),
).grid(row=2, column=3)
#############
btn_4 = Button(
    win,
    text="4",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("4"),
).grid(row=3, column=0)
btn_5 = Button(
    win,
    text="5",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("5"),
).grid(row=3, column=1)
btn_6 = Button(
    win,
    text="6",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("6"),
).grid(row=3, column=2)
btn_mine = Button(
    win,
    text="-",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("-"),
).grid(row=3, column=3)
##########
btn_1 = Button(
    win,
    text="1",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("1"),
).grid(row=4, column=0)
btn_2 = Button(
    win,
    text="2",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("2"),
).grid(row=4, column=1)
btn_3 = Button(
    win,
    text="3",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("3"),
).grid(row=4, column=2)
btn_multiple = Button(
    win,
    text="*",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("*"),
).grid(row=4, column=3)
##############
btn_0 = Button(
    win,
    text="0",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("0"),
).grid(row=5, column=0)
btn_clear = Button(
    win,
    text="c",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_clear(),
).grid(row=5, column=1)
btn_divition = Button(
    win,
    text="/",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_click("/"),
).grid(row=5, column=2)
btn_equal = Button(
    win,
    text="=",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: btn_equal(),
).grid(row=5, column=3)
btn_show = Button(
    win,
    text="h",
    padx=16,
    pady=16,
    fg="black",
    font=("arial", "22", "italic"),
    bd=8,
    command=lambda: history_(),
).grid(row=6, columnspan=7, sticky="ew")




win.bind("1", lambda event: btn_click("1"))
win.bind("2", lambda event: btn_click("2"))
win.bind("3", lambda event: btn_click("3"))
win.bind("4", lambda event: btn_click("4"))
win.bind("5", lambda event: btn_click("5"))
win.bind("6", lambda event: btn_click("6"))
win.bind("7", lambda event: btn_click("7"))
win.bind("8", lambda event: btn_click("8"))
win.bind("9", lambda event: btn_click("9"))
win.bind("0", lambda event: btn_click("0"))
win.bind("+", lambda event: btn_click("+"))
win.bind("-", lambda event: btn_click("-"))
win.bind("*", lambda event: btn_click("*"))
win.bind("/", lambda event: btn_click("/"))
win.bind("<Return>", lambda event: btn_equal())  
win.bind("<Escape>", lambda event: btn_clear())  
win.bind("<BackSpace>", lambda event: btn_clear())




def btn_click(members):
    global operator
    operator += str(members)
    text_input.set(operator)
    history.append(members)


def btn_equal():
    global operator
    result = str(eval(operator))
    text_input.set(result)


def btn_clear():
    global operator
    operator = ""
    text_input.set("")


def history_():
    global history
    text_input.set("".join(history))
    history.clear()




win.mainloop()
