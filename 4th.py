from tkinter import *
mickey=Tk()
c=Canvas(mickey,bg="white",height=300,width=350)
#ears
left=c.create_oval(50,50,140,140,fill="black")
right=c.create_oval(210,50,300,140,fill="black")
#face
f=c.create_oval(98,100,252,262,fill="black")
f=c.create_polygon(100,195,250,195,230,240,175,265,120,240,100,195,fill="navajo white",smooth=True)
leftcheek=c.create_oval(105,182,145,220,fill="navajo white",outline="navajo white")
rightcheek=c.create_oval(205,182,245,220,fill="navajo white",outline="navajo white")
#eyes
leftspace=c.create_oval(130,110,180,200,fill="navajo white",outline="navajo white")
rightspace=c.create_oval(170,110,220,200,fill="navajo white",outline="navajo white")
lefteye=c.create_oval(155,130,173,176,fill="white",outline="black",width=2)
righteye=c.create_oval(177,130,195,176,fill="white",outline="black",width=2)
lefteyeball=c.create_oval(160,155,170,176,fill="black")
righteyeball=c.create_oval(179,155,189,176,fill="black")
#nose
n=c.create_oval(155,180,195,208,fill="black")
n=c.create_line(166,175,185,175,width=3)
n=c.create_line(150,180,166,175,width=3)
n=c.create_line(185,175,201,180,width=3)
#mouth
leftarc=c.create_line(115,205,130,195,width=3)
rightarc=c.create_line(220,195,235,205,width=3)
mouth=c.create_arc(148,190,203,255,start=180,extent=180,fill="black")
mouth=c.create_arc(149,190,200,230,start=180,extent=180,fill="navajo white",outline="navajo white")
rightm=c.create_line(230,200,200,222,width=3)
leftm=c.create_line(125,200,152,222,width=3)
#tongue
t=c.create_oval(164,243,178,254,fill="red",outline="red")
t=c.create_oval(177,241,189,253,fill="red",outline="red")
t=c.create_oval(173,248,180,255,fill="red",outline="red")
c.pack()
mickey.mainloop()