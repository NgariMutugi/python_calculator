import tkinter as tk

root = tk.Tk()
w = 300 #set the width for TK root
h = 340 # set the height for Tk root

# get screen width and height
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('Calculator')

top_frame = tk.Frame(width=300, height=20, bd=4, relief='raise')
top_frame.pack(side=tk.TOP)

bottom_frame = tk.Frame(width=300, height=300, bd=4, relief='raise')
bottom_frame.pack(side=tk.BOTTOM)


root.mainloop()