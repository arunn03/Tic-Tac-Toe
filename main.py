from tkinter import *  # importing for gui
from tkinter import ttk  # importing for themed button
import os  # importing for getting the directory from where the program is called

def put_img(btn):
    global count
    if btn['image'] == 'pyimage1' and not finished:
        count += 1
        if count % 2 != 0:
            btn['image'] = x_img  # inserting the image of x
        else:
            btn['image'] = o_img  # inserting the image of o
    chk_win()

def chk_win():
    global finished
    img1 = btn1['image']
    img2 = btn2['image']
    img3 = btn3['image']
    img4 = btn4['image']
    img5 = btn5['image']
    img6 = btn6['image']
    img7 = btn7['image']
    img8 = btn8['image']
    img9 = btn9['image']

    x_win_cond = [img1 == img2 == img3 == 'pyimage2',
                  img1 == img4 == img7 == 'pyimage2',
                  img1 == img5 == img9 == 'pyimage2',
                  img2 == img5 == img8 == 'pyimage2',
                  img3 == img5 == img7 == 'pyimage2',
                  img4 == img5 == img6 == 'pyimage2',
                  img3 == img6 == img9 == 'pyimage2',
                  img7 == img8 == img9 == 'pyimage2']

    o_win_cond = [img1 == img2 == img3 == 'pyimage3',
                  img1 == img4 == img7 == 'pyimage3',
                  img1 == img5 == img9 == 'pyimage3',
                  img2 == img5 == img8 == 'pyimage3',
                  img3 == img5 == img7 == 'pyimage3',
                  img4 == img5 == img6 == 'pyimage3',
                  img3 == img6 == img9 == 'pyimage3',
                  img7 == img8 == img9 == 'pyimage3']

    if any(x_win_cond) and not finished:
        lbl_result['text'] = 'X Wins'
        finished = True
    elif any(o_win_cond) and not finished:
        lbl_result['text'] = 'O Wins'
        finished = True
    else:
        if count == 9 and not finished:
            lbl_result['text'] = 'Match tied'
            finished = True

def restart_match(event=None):
    global count, finished
    btn1['image'] = blk_img
    btn2['image'] = blk_img
    btn3['image'] = blk_img
    btn4['image'] = blk_img
    btn5['image'] = blk_img
    btn6['image'] = blk_img
    btn7['image'] = blk_img
    btn8['image'] = blk_img
    btn9['image'] = blk_img
    finished = False
    count = 0
    lbl_result['text'] = 'Match in Progress'

root = Tk()
root.title('Tic Tac Toe')
root.resizable(0, 0)
root.config(bg='white')

# setting path for icons and images
cur_path = sys.argv[0].split('\\')
if len(cur_path) > 1:
    cur_path = cur_path[:-1]
    if ':' not in sys.argv[0]:
        cur_path = os.getcwd() + '\\' + '\\'.join(cur_path) + '\\'
    else:
        cur_path = '\\'.join(cur_path) + '\\'
else:
    cur_path = ''

blk_img = PhotoImage(width=80, height=80)  # blank image for pixel sizing
x_img = PhotoImage(file=cur_path + 'res\\x.png')  # image of x
o_img = PhotoImage(file=cur_path + 'res\\o.png')  # image of o
root.iconbitmap(cur_path + 'icon.ico')  # icon for root window

# Variables
count = 0  # No. of boxes filled
finished = False

# Board Frame
btn_frame = Frame(root, bg='white')
btn_frame.pack()

# Play Area
btn1 = Button(btn_frame, bd=.5, image=blk_img, bg='white', activebackground='white', command=lambda: put_img(btn1))
btn1.grid(row=0, column=0)

btn2 = Button(btn_frame, bd=.5, image=blk_img, bg='white', activebackground='white', command=lambda: put_img(btn2))
btn2.grid(row=0, column=1)

btn3 = Button(btn_frame, bd=.5, image=blk_img, bg='white', activebackground='white', command=lambda: put_img(btn3))
btn3.grid(row=0, column=2)

btn4 = Button(btn_frame, bd=.5, image=blk_img, bg='white', activebackground='white', command=lambda: put_img(btn4))
btn4.grid(row=1, column=0)

btn5 = Button(btn_frame, bd=.5, image=blk_img, bg='white', activebackground='white', command=lambda: put_img(btn5))
btn5.grid(row=1, column=1)

btn6 = Button(btn_frame, bd=.5, image=blk_img, bg='white', activebackground='white', command=lambda: put_img(btn6))
btn6.grid(row=1, column=2)

btn7 = Button(btn_frame, bd=.5, image=blk_img, bg='white', activebackground='white', command=lambda: put_img(btn7))
btn7.grid(row=2, column=0)

btn8 = Button(btn_frame, bd=.5, image=blk_img, bg='white', activebackground='white', command=lambda: put_img(btn8))
btn8.grid(row=2, column=1)

btn9 = Button(btn_frame, bd=.5, image=blk_img, bg='white', activebackground='white', command=lambda: put_img(btn9))
btn9.grid(row=2, column=2)

# Match Progress label
lbl_result = Label(root, text='Match in Progress', bg='white', font=('arial', 13, 'bold'))
lbl_result.place(x=10, y=256)

# Button for resetting the game
btn_restart = ttk.Button(root, text='Reset', command=restart_match)
btn_restart.pack(side=RIGHT, pady=5, padx=10)

# Shortcut key for resetting
root.bind('<Control-Key-r>', restart_match)
root.mainloop()
