from turtle import *

def draw_cloud():
    import turtle as t
    bgcolor("lightblue")
    t.setup(800, 500, 300, 300)
    t.penup()
    t.fd(-200)
    t.pendown()
    t.seth(-40)
    t.pensize(25)
    t.color("white","white")
    t.begin_fill()
    for i in range(3):
        t.circle(50, 80)
        t.circle(-50, 80)
    t.circle(50, 180)
    for i in range(3):
        t.circle(50, 80)
        t.circle(-50, 80)
    t.circle(50, 270)
    t.end_fill()
    t.penup()
    t.fd(-60)
    t.right(90)
    t.fd(40)
    t.pendown()
    t.color("white","white")
    t.begin_fill()
    for i in range(3):
        t.circle(50, 80)
        t.circle(-50, 80)
    t.circle(50, 180)
    for i in range(3):
        t.circle(50, 80)
        t.circle(-50, 80)
    t.circle(50, 270)
    t.end_fill()
   
    t.done()

def draw_bone():
    import turtle as t
    t.setup(800, 500, 300, 300)
    t.penup()
    t.fd(-200)
    t.pendown()
    t.seth(180)
    t.pensize(25)
    t.color("white", "white")
    t.bgcolor("black")
    t.begin_fill()
    t.circle(-45, 220)
    t.circle(45, 40)
    t.fd(200)        
    t.circle(45, 40)
    t.circle(-45, 220)
    t.penup()
    t.right(170)
    t.pendown()
    t.circle(-44, 270)
    t.left(80)
    t.fd(220)
    t.left(90)
    t.circle(-45, 230)
    t.end_fill()
    t.done()

print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for cloud, 2 for bone)\n"
              "Your selection is: ")
    try:
        a = eval(a)
        if a == 1:
            draw_cloud()
        elif a == 2:
            draw_bone()
        else:
            print("Please input the value in [1,2]")
    except:
        print("Please input the value in [1,2]")