from tkinter import*
import tkinter.messagebox as tkMessageBox
import random
root=Tk()
menu=Menu(root)
root.config(menu=menu)


class tic:
    c='D'
    def start(self):
        res=['a','b','c','d','e','f','g','h','i']
        list1=[0,0,0,0,0,0,0,0,0]

        can1=Canvas(root,width=100,height=100,bg='black')
        def NW(event):
            if list1[0]==0:
                list1[0]=1
                can1.create_line(20,20,80,80,fill='orange')
                can1.create_line(80,20,20,80,fill='orange')
                res[0]='U'
                comp()
            else:
                tkMessageBox.showinfo("Wrong Choice", "The box is already selected")
            
        def NW1():
            can1.create_oval(10, 10, 90, 90,outline="cyan")

        can1.bind("<Button-1>",NW)
        can1.grid(row=0,column=0)

        def N(event):
            if list1[1]==0:
                list1[1]=1
                can2.create_line(20,20,80,80,fill='orange')
                can2.create_line(80,20,20,80,fill='orange')
                res[1]='U'
                comp()
            else:
                tkMessageBox.showinfo("Wrong Choice", "The box is already selected")
        def N1():
            can2.create_oval(10, 10, 90, 90,outline="cyan")

        can2=Canvas(root,width=100,height=100,bg='black')
        can2.bind("<Button-1>",N)
        can2.grid(row=0,column=1)


        def NE(event):
            if list1[2]==0:
                list1[2]=1
                can3.create_line(20,20,80,80,fill='orange')
                can3.create_line(80,20,20,80,fill='orange')
                res[2]='U'
                comp()
            else:
                tkMessageBox.showinfo("Wrong Choice", "The box is already selected")
        def NE1():
            can3.create_oval(10, 10, 90, 90,outline="cyan")
            
        can3=Canvas(root,width=100,height=100,bg='black')
        can3.bind("<Button-1>",NE)
        can3.grid(row=0,column=2)


        def W(event):
            if list1[3]==0:
                list1[3]=1
                can4.create_line(20,20,80,80,fill='orange')
                can4.create_line(80,20,20,80,fill='orange')
                res[3]='U'
                comp()
            else:
                tkMessageBox.showinfo("Wrong Choice", "The box is already selected")
        def W1():
            can4.create_oval(10, 10, 90, 90,outline="cyan")
            
        can4=Canvas(root,width=100,height=100,bg='black')
        can4.bind("<Button-1>",W)
        can4.grid(row=1,column=0)


        def M(event):
            if list1[4]==0:
                list1[4]=1
                can5.create_line(20,20,80,80,fill='orange')
                can5.create_line(80,20,20,80,fill='orange')
                res[4]='U'
                comp()
            else:
                tkMessageBox.showinfo("Wrong Choice", "The box is already selected")
        def M1():
            can5.create_oval(10, 10, 90, 90,outline="cyan")
            
        can5=Canvas(root,width=100,height=100,bg='black')
        can5.bind("<Button-1>",M)
        can5.grid(row=1,column=1)


        def E(event):
            if list1[5]==0:
                list1[5]=1
                can6.create_line(20,20,80,80,fill='orange')
                can6.create_line(80,20,20,80,fill='orange')
                res[5]='U'
                comp()
            else:
                tkMessageBox.showinfo("Wrong Choice", "The box is already selected")
        def E1():
            can6.create_oval(10, 10, 90, 90,outline="cyan")
            
        can6=Canvas(root,width=100,height=100,bg='black')
        can6.bind("<Button-1>",E)
        can6.grid(row=1,column=2)


        def SW(event):
            if list1[6]==0:
                list1[6]=1
                can7.create_line(20,20,80,80,fill='orange')
                can7.create_line(80,20,20,80,fill='orange')
                res[6]='U'
                comp()
            else:
                tkMessageBox.showinfo("Wrong Choice", "The box is already selected")
        def SW1():
            can7.create_oval(10, 10, 90, 90,outline="cyan")
            
        can7=Canvas(root,width=100,height=100,bg='black')
        can7.bind("<Button-1>",SW)
        can7.grid(row=2,column=0)


        def S(event):
            if list1[7]==0:
                list1[7]=1
                can8.create_line(20,20,80,80,fill='orange')
                can8.create_line(80,20,20,80,fill='orange')
                res[7]='U'
                comp()
            else:
                tkMessageBox.showinfo("Wrong Choice", "The box is already selected")
        def S1():
            can8.create_oval(10, 10, 90, 90,outline="cyan")
            
            
        can8=Canvas(root,width=100,height=100,bg='black')
        can8.bind("<Button-1>",S)
        can8.grid(row=2,column=1)


        def SE(event):
            if list1[8]==0:
                list1[8]=1
                can9.create_line(20,20,80,80,fill='orange')
                can9.create_line(80,20,20,80,fill='orange')
                res[8]='U'
                comp()
            else:
                tkMessageBox.showinfo("Wrong Choice", "The box is already selected")
        def SE1():
            can9.create_oval(10, 10, 90, 90,outline="cyan")
            
        can9=Canvas(root,width=100,height=100,bg='black')
        can9.bind("<Button-1>",SE)
        can9.grid(row=2,column=2)

        list2=[NW1,N1,NE1,W1,M1,E1,SW1,S1,SE1]
        def comp():
            a=0
            x=1
            global c
            for i in list1:
                a+=i
            for i in [0,3,6]:
                if res[i]==res[i+1]==res[i+2]:
                    a=9
                    x=0
                    c=res[i]
            for i in range(3):
                if res[i]==res[i+3]==res[i+6]:
                    a=9
                    x=0
                    c=res[i]
            if res[0]==res[4]==res[8]:
                    a=9
                    x=0
                    c=res[0]
            if res[2]==res[4]==res[6]:
                    a=9
                    x=0
                    c=res[2]
            if a<9:
                a=random.randint(0,8)
                while(list1[a]!=0):
                    a=random.randint(0,8)
                list2[a]()
                list1[a]=1
                res[a]='C'
                for i in [0,3,6]:
                    if res[i]==res[i+1]==res[i+2]:
                        c=res[i]
                        endgame()
                for i in range(3):
                    if res[i]==res[i+3]==res[i+6]:
                        c=res[i]
                        endgame()
                if res[0]==res[4]==res[8]:
                        c=res[0]
                        endgame()
                if res[2]==res[4]==res[6]:
                        c=res[2]
                        endgame()
            elif x==0:
                endgame()
            else:
                c='D'
                endgame()
        def endgame():
            global c
            if c=='U':
                c='You have won the game!'
            if c=='C':
                c='Computer has won the game!'
            if c=='D':
                c='Game is tied!'
            tkMessageBox.showinfo("Game Over!", c)

obj=tic()

obj.start()

ab="""This is a python GUI project  based on TIC-TAC-TOE game
done under Ankit Sir from Nielit institution"""
h="""Tic-Tac-Toe (also known as noughts and crosses or
Xs and Os) is a paper-and-pencil game for two players,
X and O, whotake turns marking the spaces in a 3x3 grid.
The player who succeds first in placing 3 of his mark
in a horizontal,vertical, or diagonal row wins the game.
We bring to you this game in electronic media. Hope you
enjoy. Good luck!!"""
def helpuser():
    tkMessageBox.showinfo("Help", h)
submenu=Menu(menu)
def aboutthis():
    tkMessageBox.showinfo("About", ab)
menu.add_cascade(label='File', menu=submenu)
submenu.add_command(label="New game",command=obj.start)
submenu.add_command(label="Help",command=helpuser)
submenu.add_separator()
submenu.add_command(label="About",command=aboutthis)

root.mainloop()
