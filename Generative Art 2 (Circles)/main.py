#generative Art 2
import turtle
import random

t=turtle.Turtle()
t.speed(0)
t.ht()
t.screen.bgcolor("black")
colours = ["cyan2", "DarkOrchid1", "blue", "plum1", "SpringGreen"]
t.color("cyan2")
#t.pencolor(0.9,0.9,0.9)
rtdeg=46
turndir=-1

for i in range(360*16):
  for i in range (100):
    t.fd(10)
    t.rt(rtdeg)
    if rtdeg>46:
        rtdeg=46
        turndir=-1
    elif rtdeg<-45:
        rtdeg=-45
        turndir=1
    rtdeg+=turndir
  t.color(random.choice(colours))
