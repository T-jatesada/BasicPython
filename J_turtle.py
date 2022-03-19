import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Rec(d=100):
    for i in range(4):
        tao.fd(d)
        tao.lt(90)
        
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Rec()
#tao.clear()
Go(200,200)
Rec(50)
Go(-200,100)
Rec(150)
Go(-200,-200)
Rec(200)
