import turtle
from turtle import *

colors = ["blue", "plum1", "violet", "HotPink", "white", "cyan2"]
bgcolor ("black")
speed (0)

for i in range (200):
  pencolor(colors[i%6])
  width(i/100+1)
  forward(i)
  left(59)


hideturtle()
done()