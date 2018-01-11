from tkinter import *

root = Tk()
root.wm_title('Bar Graph')
root.option_readfile('styles.txt')

near_white = '#F2F2F2'

root.configure(background = near_white)

this_var = 25

def inc_up():
    global this_var
    if (this_var + 1) < 31:
        this_var += 1
        bar_graph.config(width = this_var)
        num_show.config(text = this_var)

def inc_dn():
    global this_var
    if (this_var -1) > 0:
        this_var -= 1
        bar_graph.config(width = this_var)
        num_show.config(text = this_var)

bar_graph = Label(root, background = 'blue', width = this_var)
btn_left = Button(root, text = '<', command = inc_dn)
num_show = Label(root, text = this_var, width = 8, background = near_white)
btn_right = Button(root, text = '>', command = inc_up)


bar_graph.grid(column = 0, row = 0, columnspan = 3, sticky = W)
btn_left.grid(row = 1, column = 0, sticky = W)
num_show.grid(row = 1, column = 1)
btn_right.grid(row = 1, column = 2, sticky = E)


root.mainloop()
