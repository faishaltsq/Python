import tkinter as tk



#create a window
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

#label
var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)
l.pack()

#button
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')
b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
b.pack()

#entry
e = tk.Entry(window, show='*')
e.pack()

#text
t = tk.Text(window, height=2)
t.pack()

#listbox
var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(window, listvariable=var2)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

#radiobutton
var3 = tk.StringVar()
r1 = tk.Radiobutton(window, text='Option A', variable=var3, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var3, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var3, value='C', command=print_selection)
r3.pack()

#scale
def print_selection(v):
    l.config(text='you have selected ' + v)
s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

#checkbutton
var4 = tk.StringVar()
c = tk.Checkbutton(window, text='check me', variable=var4, onvalue='on', offvalue='off', command=print_selection)
c.pack()

#canvas
canvas = tk.Canvas(window, bg='blue', height=100, width=200)
image_file = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(10, 10, anchor='nw', image=image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
canvas.pack()

#menu
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command= do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label='Submenu1', command=do_job)

#frame
frame = tk.Frame(window)
frame.pack()
frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')

#messagebox
def hit_me():
    tk.messagebox.showinfo(title='Hi', message='hahahaha')
    tk.messagebox.showwarning(title='Hi', message='nononono')
    tk.messagebox.showerror(title='Hi', message='No!! never')
    print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))
    print(tk.messagebox.askyesno(title='Hi', message='hahahaha'))
    print(tk.messagebox.askretrycancel(title='Hi', message='hahahaha'))
    print(tk.messagebox.askokcancel(title='Hi', message='hahahaha'))
b = tk.Button(window, text='hit me', command=hit_me)
b.pack()

#pack
tk.Label(window, text='P', fg='red').pack(side='top')
tk.Label(window, text='P', fg='red').pack(side='bottom')
tk.Label(window, text='P', fg='red').pack(side='left')
tk.Label(window, text='P', fg='red').pack(side='right')

#grid
for i in range(4):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
        
#place
tk.Label(window, text=1).place(x=10, y=100, anchor='nw')

#bind
def printcoords(event):
    print(event.x, event.y)
tk.Label(window, text=1).bind('<Button-1>', printcoords)

#mouse
def mouse_move(event):
    tk.Label(window, text='(' + str(event.x) + ', ' + str(event.y) + ')').pack()
window.bind('<Motion>', mouse_move)

#keyboard
def key(event):
    print('pressed', repr(event.char))
def callback(event):
    frame.focus_set()
    print('clicked at', event.x, event.y)
frame = tk.Frame(window, width=100, height=100)
frame.bind('<Key>', key)
frame.bind('<Button-1>', callback)
frame.pack()

#canvas
def moveit():
    canvas.move(rect, 0, 2)
b = tk.Button(window, text='move', command=moveit).pack()

#animation
def moveit():
    canvas.move(rect, 2, 2)
    canvas.move(oval, 2, 1)
    canvas.after(10, moveit)
b = tk.Button(window, text='move', command=moveit).pack()

#image
canvas = tk.Canvas(window, bg='blue', height=200, width=300)
image_file = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
canvas.pack()

#tkinter
window.mainloop()


    
    

