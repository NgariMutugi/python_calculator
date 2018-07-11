import tkinter as tk

root = tk.Tk()
w = 300  # set the width for TK root
h = 340  # set the height for Tk root

# get screen width and height
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('Calculator')

top_frame = tk.Frame(width=300, height=20, bd=4, relief='raise')
top_frame.pack(side=tk.TOP)

bottom_frame = tk.Frame(width=300, height=300, bd=4, relief='raise')
bottom_frame.pack(side=tk.BOTTOM)


# =================================================================================================================


def btn_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btn_clears():
    global operator
    operator = ""
    text_input.set("")


def btn_equals():
    global operator
    sum_up = str(eval(operator))
    text_input.set(sum_up)
    operator = ""


operator = ""
text_input = tk.StringVar()

# =================================================================================================================

txtDisplay = tk.Entry(top_frame, font=('arial', 18, 'bold'), textvariable=text_input, width=21, bd=4, justify='right')
txtDisplay.grid(row=0, column=0)

btn7 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                 text='7', command=lambda: btn_click(7)).grid(row=0, column=0)
btn8 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                 text='8', command=lambda: btn_click(8)).grid(row=0, column=1)
btn9 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                 text='9', command=lambda: btn_click(9)).grid(row=0, column=2)
btn_add = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                    text='+', command=lambda: btn_click('+')).grid(row=0, column=3)

btn4 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                 text='4', command=lambda: btn_click(4)).grid(row=1, column=0)
btn5 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                 text='5', command=lambda: btn_click(5)).grid(row=1, column=1)
btn6 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                 text='6', command=lambda: btn_click(6)).grid(row=1, column=2)
btn_subtraction = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2,
                            height=2,
                            text='-', command=lambda: btn_click('-')).grid(row=1, column=3)

btn1 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                 text='1', command=lambda: btn_click(1)).grid(row=2, column=0)
btn2 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                 text='2', command=lambda: btn_click(2)).grid(row=2, column=1)
btn3 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                 text='3', command=lambda: btn_click(3)).grid(row=2, column=2)
btn_multiplication = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2,
                               height=2, text='*', command=lambda: btn_click('*')).grid(row=2, column=3)

btn_clear = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                      text='C', command=lambda: btn_clears()).grid(row=3, column=0)

btn0 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                 text='0', command=lambda: btn_click(0)).grid(row=3, column=1)
btn_divide = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                       text='÷', command=lambda: btn_click('/')).grid(row=3, column=3)

btn_equal = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=2, height=2,
                      text='=', command=lambda: btn_equals()).grid(row=3, column=2)


root.mainloop()
