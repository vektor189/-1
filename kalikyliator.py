from tkinter import *

root = Tk()
root.title('Калькулятор')

n = 0
p = 0
m = 0
ym = 0
d = 0

def num(s):
    global n
    if n == 0:
        n += s
        label2.config(text = n)
    else:
        label2.config(text = str(n) + str(s))
        n = int(str(n) + str(s))

def plusing():
    global p
    global n
    p = n
    n = 0
    label2.config(text = n)

def ymnox():
    global ym
    global n
    ym = n
    n = 0
    label2.config(text = n)

def delenie():
    global d
    global n
    d = n
    n = 0
    label2.config(text = n)

def minus():
    global m
    global n
    m = n
    n = 0
    label2.config(text = n)

def ravno():
    global p
    global n
    global ym
    global d
    global m
    if ym > 0:
        n *= ym
        ym = 0
        label2.config(text = n)
    if d > 0:
        d /= n
        n = d
        d = 0
        label2.config(text = n)
    if m > 0:
        m -= n
        n = m
        m = 0
        label2.config(text = n)
    if p > 0:
        n += p
        p = 0
        label2.config(text = n)
        

def obnul():
    global p
    global n
    global ym
    global d
    p = 0
    d = 0
    n = 0
    ym = 0
    label2.config(text = n)

#фреймы для разделения на строки    
        
f_top = Frame(root)
f_meed1 = Frame(root)
f_bot = Frame(root)
f_meed = Frame(root)
f_meed2 = Frame(root)
f_top.pack()
f_meed1.pack()
f_meed.pack()
f_meed2.pack()
f_bot.pack()

label2 = Label(f_top, text = n, width = 45, height = 2, bg = 'white')
label2.pack()

#верхняя строка

seven_but = Button(f_meed1, text = '7', width = 10, height = 2, bg = 'white', command = lambda:num(7))
seven_but.pack(side="left")
eight_but = Button(f_meed1, text = '8', width = 10, height = 2, bg = 'white', command = lambda:num(8))
eight_but.pack(side="left")
nine_but = Button(f_meed1, text = '9', width = 10, height = 2, bg = 'white', command = lambda:num(9))
nine_but.pack(side="left")
ymnox_but = Button(f_meed1, text = '*', width = 10, height = 2, bg = 'white', command = ymnox)
ymnox_but.pack(side="right")

#верхняя центральная строка

four_but = Button(f_meed, text = '4', width = 10, height = 2, bg = 'white', command = lambda:num(4))
four_but.pack(side="left")
five_but = Button(f_meed, text = '5', width = 10, height = 2, bg = 'white', command = lambda:num(5))
five_but.pack(side="left")
six_but = Button(f_meed, text = '6', width = 10, height = 2, bg = 'white', command = lambda:num(6))
six_but.pack(side="left")
delenie_but = Button(f_meed, text = '/', width = 10, height = 2, bg = 'white', command = delenie)
delenie_but.pack(side="right")

#нижняя центральная строка

one_but = Button(f_meed2, text = '1', width = 10, height = 2, bg = 'white', command = lambda:num(1))
one_but.pack(side="left")
two_but = Button(f_meed2, text = '2', width = 10, height = 2, bg = 'white', command = lambda:num(2))
two_but.pack(side="left")
tree_but = Button(f_meed2, text = '3', width = 10, height = 2, bg = 'white', command = lambda:num(3))
tree_but.pack(side="left")
plus_but = Button(f_meed2, text = '+', width = 10, height = 2, bg = 'white', command = plusing)
plus_but.pack(side="right")

#нижняя строка

minus_but = Button(f_bot, text = '-', width = 10, height = 2, bg = 'white', command = minus)
minus_but.pack(side="right")
ravno_but = Button(f_bot, text = '=', width = 10, height = 2, bg = 'white', command = ravno)
ravno_but.pack(side="right")
zero_but = Button(f_bot, text = '0', width = 10, height = 2, bg = 'white', command = lambda:num(0))
zero_but.pack(side="right")
but4 = Button(f_bot, text = 'CE', width = 10, height = 2, bg = 'white', command = obnul)
but4.pack(side="right")

root.mainloop()
