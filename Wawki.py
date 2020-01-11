import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=400, height=400, bg='white')
root.title("Шашки")
canvas.pack()

color1=''
color2=''

def wvet1():
    global line
    if (line + 2) % 2 == 0:
        fill='white'
    else:
        fill='brown'
    return fill

def wvet2():
    global line
    if (line + 2) % 2 == 0:
        fill='brown'
    else:
        fill='white'
    return fill

#1
a1 = canvas.create_rectangle(0, 0, 50, 50, fill='brown')
a2 = canvas.create_rectangle(50, 0, 100, 50, fill='white')
a3 = canvas.create_rectangle(100, 0, 150, 50, fill='brown')
a4 = canvas.create_rectangle(150, 0, 200, 50, fill='white')
a5 = canvas.create_rectangle(200, 0, 250, 50, fill='brown')
a6 = canvas.create_rectangle(250, 0, 300, 50, fill='white')
a7 = canvas.create_rectangle(300, 0, 350, 50, fill='brown')
a8 = canvas.create_rectangle(350, 0, 400, 50, fill='white')
#2
def dva():
    global pole
    lst = []
    global line
    line = 0
    while line < 8:
        pole = canvas.create_rectangle((0 + line * 50), 50, (50 + line * 50), 100, fill=(wvet1()))
        line +=1
        lst.append(pole)
#3
def tri():
    global line
    line = 0
    while line < 8:
        canvas.create_rectangle((0 + line * 50), 100, (50 + line * 50), 150, fill=(wvet2()))
        line +=1
#4
def chetire():
    global line
    line = 0
    while line < 8:
        canvas.create_rectangle((0 + line * 50), 150, (50 + line * 50), 200, fill=(wvet1()))
        line +=1
#5
def piat():
    global line
    line = 0
    while line < 8:
        canvas.create_rectangle((0 + line * 50), 200, (50 + line * 50), 250, fill=(wvet2()))
        line +=1
#6
def west():
    global line
    line = 0
    while line < 8:
        canvas.create_rectangle((0 + line * 50), 250, (50 + line * 50), 300, fill=(wvet1()))
        line +=1
#7
def sem():
    global line
    line = 0
    while line < 8:
        canvas.create_rectangle((0 + line * 50), 300, (50 + line * 50), 350, fill=(wvet2()))
        line +=1
#8
def vosimaia():
    global line
    line = 0
    while line < 8:
        canvas.create_rectangle((0 + line * 50), 350, (50 + line * 50), 400, fill=(wvet1()))
        line +=1

class wawka():
    def __init__(self, x, y, r, color):
        self.color = color
        self.x = x
        self.y = y
        self.r = r
    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=BG_COLOR, outline=BG_COLOR)

def start():
    main_ball2 = wawka(25, 325, 20, 'white')
    main_ball3 = wawka(125, 325, 20, 'white')
    main_ball4 = wawka(225, 325, 20, 'white')
    main_ball5 = wawka(325, 325, 20, 'white')
    main_ball6 = wawka(75, 275, 20, 'white')
    main_ball7 = wawka(175, 275, 20, 'white')
    main_ball8 = wawka(275, 275, 20, 'white')
    main_ball9 = wawka(375, 275, 20, 'white')
    main_ball0 = wawka(75, 375, 20, 'white')
    main_ball21 = wawka(175, 375, 20, 'white')
    main_ball31 = wawka(275, 375, 20, 'white')
    main_ball41 = wawka(375, 375, 20, 'white')
    main_ball2.draw()
    main_ball3.draw()
    main_ball4.draw()
    main_ball5.draw()
    main_ball6.draw()
    main_ball7.draw()
    main_ball8.draw()
    main_ball9.draw()
    main_ball0.draw()
    main_ball21.draw()
    main_ball31.draw()
    main_ball41.draw()
    
    blac_ball2 = wawka(25, 25, 20, 'black')
    blac_ball3 = wawka(125, 25, 20, 'black')
    blac_ball4 = wawka(225, 25, 20, 'black')
    blac_ball5 = wawka(325, 25, 20, 'black')
    blac_ball6 = wawka(75, 75, 20, 'black')
    blac_ball7 = wawka(175, 75, 20, 'black')
    blac_ball8 = wawka(275, 75, 20, 'black')
    blac_ball9 = wawka(375, 75, 20, 'black')
    blac_ball0 = wawka(25, 125, 20, 'black')
    blac_ball21 = wawka(125, 125, 20, 'black')
    blac_ball31 = wawka(225, 125, 20, 'black')
    blac_ball41 = wawka(325, 125, 20, 'black')
    blac_ball2.draw()
    blac_ball3.draw()
    blac_ball4.draw()
    blac_ball5.draw()
    blac_ball6.draw()
    blac_ball7.draw()
    blac_ball8.draw()
    blac_ball9.draw()
    blac_ball0.draw()
    blac_ball21.draw()
    blac_ball31.draw()
    blac_ball41.draw()

vosimaia()
sem()
west()
piat()
chetire()
tri()
dva()
start()
canvas.bind('<Button-1>')
root.mainloop()
