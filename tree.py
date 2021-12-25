#!/usr/bin/python3
from turtle import *
bgcolor("white")
speed(0)
pen(shown=False, pencolor='black',
    pensize=4, outline=20)
pu()
goto(-30,-130)
pd()
ht()

# tree trunk
fillcolor('saddle brown')
begin_fill()
for i in range (2):
    fd(60)
    rt(90)
    fd(50)
    rt(90)
end_fill()

# tree branches
fillcolor('dark green')

# lower branch
pu()
goto(-150,-130)
pd()
begin_fill()
goto(150,-130)
goto(90,-40)
goto(-90,-40)
goto(-150,-130)
end_fill()

# middle branch
pu()
goto(-110,-40)
pd()
begin_fill()
goto(110,-40)
goto(50,50)
goto(-50,50)
goto(-110,-40)
end_fill()

# upper branch
pu()
goto(-70,50)
pd()
begin_fill()
goto(70,50)
goto(0,150)
goto(-70,50)
end_fill()

# color balls
centers=[(-110,-130), (110,-130), (-50,-90),
         (40,-80), (-30,-40), (90,-20),(-70,0),(40,60)]
colors=['yellow', 'purple', 'white', 'pink', 'yellow', 'white', 'red', 'blue']

i=0
for center in centers:
    pu()
    goto(center)
    pd()
    fillcolor(colors[i])
    begin_fill()
    circle(15)
    end_fill()
    i+=1

# top star
pu()
goto(-30,160)
pensize(3)
color('orange','yellow')
pd()
begin_fill()
for i in range (5):
    fd(50)
    rt(144)
end_fill()

# write message
def write_message(xcor,ycor):
    pu()
    goto(xcor,ycor)
    pd()
    pencolor('red')
    write("Merry Christmas!", font=['vladimir script', 50, 'bold'])
    return()

# gift box
pu()
goto(200,-180)
pd()
color('red','orange')
begin_fill()
for i in range(4):
    fd(40)
    lt(90)
end_fill()
pu()
goto(220,-140)
color('red')
pd()
goto(200,-130)
goto(210,-120)
goto(220,-140)
goto(240,-130)
goto(230,-120)
goto(220,-140)

onclick(write_message(-200,180))

mainloop()
