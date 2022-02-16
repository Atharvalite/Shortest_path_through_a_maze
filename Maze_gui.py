import tkinter
from tkinter import *
import numpy as np
import math
from Graph import *

root = Tk()
root.geometry('900x900')

#basic layout of gui
L = Label(root, text ="MAZE Solver")
L.grid(row=0,column=0,ipadx=100,pady=20,padx=10)


frame=LabelFrame(root,padx=10,pady=10)
frame.grid(row=1,column=0,padx=10,pady=10)

#grid formation
width=600
height=600
n=600//6
square=6
maze=Canvas(frame,width=600,height=600,bg='green')   
maze.pack()
for i in range(0,600,6):
    maze.create_line(i,0,i,600,fill='#164E90')
    maze.create_line(0,i,600,i,fill='#164E90')


#capturing the mouse event and forming a maze
global obstacles
obstacles=[]

def maze_form(event):
    x=event.x
    y=event.y
    x=x//6
    y=y//6
    obstacles.append((x,y))
    x*=6
    y*=6
    maze.create_rectangle(x,y,x+6,y+6,fill='#5411BF')

    return
#setting start point and end points
def Define(ex,ey,jx,jy,points):
    global sx,sy,gx,gy,Tup_points
    sx=int(ex.get())
    sy=int(ey.get())
    gx=int(jx.get())
    gy=int(jy.get())
    Tup_points=((sx,sy),(gx,gy))
    maze.create_rectangle(sx*6,sy*6,sx*6+6,sy*6+6,fill='red')
    maze.create_rectangle(gx*6,gy*6,gx*6+6,gy*6+6,fill='red')
    points.destroy()
    return

def Setpoints():
    points=Toplevel()
    points.geometry('400x400')
    Intro=Label(points,text='Enter the x and y co-ordinates of the start point and end point.',bg='cyan')
    Intro.grid(row=0,column=0,columnspan=10)
    start_lbl=Label(points,text='Start:')
    start_lbl.grid(row=1,column=0,pady=5,rowspan=2)
    x_lab=Label(points,text='X1')
    x_lab.grid(row=1,column=1,padx=25)
    y_lab=Label(points,text='Y1')
    y_lab.grid(row=1,column=4)

    ex=Entry(points,width=4,border=2)
    ey=Entry(points,width=4,border=2)

    x_la=Label(points,text='X2')
    x_la.grid(row=2,column=1,padx=25)
    y_la=Label(points,text='Y2')
    y_la.grid(row=2,column=4)
    ex.grid(row=1,column=3,pady=3,padx=3)
    ey.grid(row=1,column=5,pady=3,padx=3)
    end_lbl=Label(points,text='End: ')
    end_lbl.grid(row=2,column=0,pady=5,rowspan=2)
    jx=Entry(points,width=4,border=2)
    jy=Entry(points,width=4,border=2)
    jx.grid(row=2,column=3,pady=3,padx=3)
    jy.grid(row=2,column=5,pady=3,padx=3)
    ok=Button(points,text='SET',width=4,fg='pink',command=lambda: Define(ex,ey,jx,jy,points))
    ok.grid(row=4,column=2,columnspan=2,padx=2,pady=4)
    
set_button=Button(root,text='Set Points',width=8,padx=5,pady=5,command=Setpoints)
set_button.grid(row=1,column=2,padx=2,pady=5)
# Drawing the maze

global flag
flag=False
def Toggle():
    global flag
    flag=not(flag)

    if flag:
        maze.bind('<B1-Motion>',maze_form)
    else:
        maze.unbind('<B1-Motion>')
    return
form=Button(root,text='Draw Obstacles',width=10,padx=5,pady=5,command=Toggle)
form.grid(row=1,column=3,padx=2,pady=5,columnspan=2)

#Start Button # Maze Solver
def Solve():

    s=Tup_points[0]
    z=Tup_points[1]
    ans = Graph(s,z,obstacles)
    
    path=ans.Search()
    n=len(path)
    for i in range(2,n-1):
        x,y=path[i]
        x*=6 
        y*=6
        maze.create_rectangle(x,y,x+6,y+6,fill='yellow')

start=Button(root,text='Start',width=6,padx=5,pady=5,command=Solve)
start.grid(row=1,column=6,padx=2,pady=5,columnspan=2)


root.mainloop()
