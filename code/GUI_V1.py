# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 12:02:43 2022

@author: Subrat Kishore Dutta
"""
import os
import tkinter
from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image,ImageTk
import cv2
import time
import warnings
warnings.filterwarnings('ignore')

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


win= Tk()


#win.state('zoomed')
win.title("QUASIM")
win.geometry("1420x1580")
win.configure(bg='#ffffff')

prj_home = "D:/DFKI"

fpath = os.path.join(prj_home, "simulate.png")
play= PhotoImage(file = fpath,master=win)      

spath = os.path.join(prj_home, "simulate.png")
stopimg= PhotoImage(file = spath,master=win)      





### scrollbar stuff

main_frame = Frame(win)


main_frame.pack(fill=BOTH,expand=1)



# Create Frame for X Scrollbar


sec = Frame(main_frame)


sec.pack(fill=X,side=BOTTOM)



# Create A Canvas


my_canvas = Canvas(main_frame)


my_canvas.pack(side=LEFT,fill=BOTH,expand=1)



# Add A Scrollbars to Canvas


x_scrollbar = ttk.Scrollbar(sec,orient=HORIZONTAL,command=my_canvas.xview)


x_scrollbar.pack(side=BOTTOM,fill=X)


y_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
y_scrollbar.pack(side=RIGHT,fill=Y)



# Configure the canvas


my_canvas.configure(xscrollcommand=x_scrollbar.set)


my_canvas.configure(yscrollcommand=y_scrollbar.set)


my_canvas.bind_all("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL)))


# Create Another Frame INSIDE the Canvas


second_frame = Frame(my_canvas)



# Add that New Frame a Window In The Canvas


my_canvas.create_window((0,0),window= second_frame, anchor="nw")


 

###scrollbar stuff




##functions         

def simulate():  
    par1=float(p1.get())
    par2=material.get()
    par3=model.get()
    
    
    if par2 =="Select Material":
        par2=None
    if par3 =="Select Model":
        par3=None
    time.sleep(1)
    if par3=='FEM':
        while im1==[] or im2 ==[]:
            start['state']='disabled'
    start['state']='normal'
    stop['state']='normal'

    print([par1,par2,par3])
              
def imgseq(file):
    cap = cv2.VideoCapture(os.path.join(prj_home,file))
    # creating list of PhotoImage objects for each frames
    im = []#PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    for i in range(length):
            ret, frame = cap.read()
            frame=Image.fromarray(frame)
            frame= frame.resize((448,398), Image.ANTIALIAS)
            im.append(ImageTk.PhotoImage(frame))
    return(im,length)

 
    
anim=None
def animation(mod,count1,count2,count3,count4,count5,count6,count7,count8,
length1,length2,length3,length4,length5,length6,length7,length8,
im1,im2,im3,im4,im5,im6,im7,im8):
    global anim
    try:
        im2_1 = im1[count1]
        im2_2 = im2[count2]
        im2_3 = im3[count3]
        im2_4 = im4[count4]
        im2_5 = im1[count5]
        im2_6 = im2[count6]
        im2_7 = im3[count7]
        im2_8 = im4[count8]
        gif_label1.configure(image=im2_1)
        gif_label2.configure(image=im2_2)
        gif_label3.configure(image=im2_3)
        gif_label4.configure(image=im2_4)
        gif_label5.configure(image=im2_5)
        gif_label6.configure(image=im2_6)
        gif_label7.configure(image=im2_7)
        gif_label8.configure(image=im2_8)

        count1 += 1
        count2 += 1
        count3 += 1
        count4 += 1
        count5 += 1
        count6 += 1
        count7 += 1
        count8 += 1

        if count1 == length1:
            count1 = 0
        if count2 == length2:
            count2 = 0
        if count3 == length3:
            count3 = 0
        if count4 == length4:
            count4 = 0
        if count5 == length5:
            count5 = 0
        if count6 == length6:
            count6 = 0
        if count7 == length7:
            count7 = 0
        if count8 == length8:
            count8 = 0

        maxlen=max(length1,length2,length3,length4,length5,length6,length7,length8)

        model.set("Select Model")
        p1.delete(0,END)
        material.set('select Material')
        start['state']='disabled'
        anim=win.after(maxlen+5,lambda :animation(mod,count1,count2,count3,count4,count5,count6,count7,count8,
length1,length2,length3,length4,length5,length6,length7,length8,im1,im2,im3,im4,im5,im6,im7,im8)) 

    except:
        pass             
              
def stop_animation():             
    win.after_cancel(anim)
    start['state']='normal'
              
##CONTROL Panel
              
CP=LabelFrame(second_frame,text="",padx=4,pady=2,bg="#ffffff",border=1)
CP.grid(row=0,column=0,columnspan=3)              


label0=Label(CP,text="Control Box",font=('Arial 16'),width=140,height=1,bg="#00005f",fg="#ffffff")
label0.grid(row=0,columnspan=8,padx=0)

label1=Label(CP,text="Laser flux",font=('Arial 12'),width=15,height=1,padx=7,pady=2)
label1.grid(row=1,column=0,padx=0,pady=20)
p1=Entry(CP,width=15,font=('Arial 16'),bg="#ffffff",fg="#000000",borderwidth=2)
p1.grid(row=1,column=1,padx=0,pady=20)


material= StringVar() 
material.set("Select Material") 
drop1 = OptionMenu(CP,material,"Aluminium","Steel")
drop1.config(width=15)
drop1.grid(row=1,column=2,padx=0,pady=20)


model= StringVar() 
model.set("Select Model") 
drop = OptionMenu(CP,model,"FEM","MGN","GCN",'Hy GCN')
drop.config(width=15)
drop.grid(row=1,column=3,padx=0,pady=20)


sim=Button(CP,text="simulate",font=('Arial 16'), padx=7,pady=0, command=simulate,fg="#000000",borderwidth=1,bg="#ffffff",width=9)
sim.grid(row=1,column=4,padx=0,pady=20)


start = Button(CP,image=play,state='disabled',command=lambda :animation(model.get(),count1,
count2,count3,count4,count5,count6,count7,count8,length1,length2,length3,length4,length5,length6,length7,length8,im1,im2,im3,im4,im5,im6,im7,im8))

start.grid(row=1,column=5,padx=0,pady=20)

stop = Button(CP,image=stopimg,state='disabled',command=stop_animation)
stop.grid(row=1,column=6,padx=0,pady=20)

##----------------end of control panel--------------------##





##--------------------start of model1----------------------##

FEMframe=LabelFrame(second_frame,text="",padx=0,pady=0,bg="#ffffff",border=1)
FEMframe.grid(row=1,column=0,columnspan=8,pady=10)              


FEMcap=Label(FEMframe,text="FEM",font=('Arial 16'),width=140,height=1,bg="#00005f",fg="#ffffff")
FEMcap.grid(row=0,column=0,columnspan=8,padx=0)

file1=os.path.join(prj_home, "video1.mp4")
im1,length1=imgseq(file1)   
count1 = 0
fpath = os.path.join(prj_home, "qc.png")
ini_pic1=PhotoImage(file = fpath, master=win)
gif_label1 = Label(FEMframe,image=ini_pic1,border=5,width=450,height=400)
gif_label1.grid(row=1,column=0,pady=2,padx=2)

fpath = os.path.join(prj_home, "plot.png")
img1=cv2.imread(fpath)
img1=cv2.resize(img1,(470,405))
cv2.imwrite(fpath,img1)
plot1 = PhotoImage(file=fpath,master=win)
plot1Label = Label(FEMframe,image=plot1)
plot1Label.grid(row=1,column=1,pady=1,padx=2)


file2=os.path.join(prj_home, "video1.mp4")
im2,length2=imgseq(file2)   
count2 = 0
fpath = os.path.join(prj_home, "qc.png")
ini_pic2=PhotoImage(file = fpath, master=win)
gif_label2 = Label(FEMframe,image=ini_pic2,border=5,width=450,height=400)
gif_label2.grid(row=1,column=2,pady=2,padx=2)



#start1 = Button(win,image=play,command=lambda :animation(count1,length1,im1,gif_label1))
#start1.place(x=30,y=453)


#start2 = Button(win,image=play,command=lambda :animation(count2,length2,im2,gif_label2))
#start2.place(x=30,y=1068)
##-----------------END of model 1-----------------#






##--------------start of model 2------------------#

CMLframe=LabelFrame(second_frame,text="",padx=0,pady=0,bg="#ffffff",border=1)
CMLframe.grid(row=2,columnspan=8,pady=10)              


CMLcap=Label(CMLframe,text="MGN",font=('Arial 16'),width=140,height=1,bg="#00005f",fg="#ffffff")
CMLcap.grid(row=0,column=0,columnspan=8,padx=0)

file3=os.path.join(prj_home, "video1.mp4")
im3,length3=imgseq(file3)   
count3 = 0
fpath = os.path.join(prj_home, "qc.png")
ini_pic3=PhotoImage(file = fpath, master=win)
gif_label3 = Label(CMLframe,image=ini_pic3,border=5,width=450,height=400)
gif_label3.grid(row=1,column=0,pady=2,padx=2)


fpath = os.path.join(prj_home, "plot1.png")
img2=cv2.imread(fpath)
img2=cv2.resize(img2,(470,405))
cv2.imwrite(fpath,img2)
plot2 = PhotoImage(file= fpath, master=win)
plot2Label = Label(CMLframe,image=plot2)
plot2Label.grid(row=1,column=1,pady=1,padx=2)



file4=os.path.join(prj_home, "video1.mp4")
im4,length4=imgseq(file4)   
count4 = 0
fpath = os.path.join(prj_home, "qc.png")
ini_pic4=PhotoImage(file = fpath, master=win)
gif_label4 = Label(CMLframe,image=ini_pic4,border=5,width=450,height=400)
gif_label4.grid(row=1,column=2,pady=2,padx=2)




##-----------------END of model 2-----------------#



##--------------start of model 3------------------#

QMLframe=LabelFrame(second_frame,text="",padx=0,pady=0,bg="#ffffff",border=1)
QMLframe.grid(row=3,columnspan=8,pady=10)              


QMLcap=Label(QMLframe,text="GCN",font=('Arial 16'),width=140,height=1,bg="#00005f",fg="#ffffff")
QMLcap.grid(row=0,column=0,columnspan=8,padx=0)

file5=os.path.join(prj_home, "video1.mp4")
im5,length5=imgseq(file5)   
count5 = 0
fpath = os.path.join(prj_home, "qc.png")   
ini_pic5=PhotoImage(file = fpath, master=win)
gif_label5 = Label(QMLframe,image=ini_pic5,border=5,width=450,height=400)
gif_label5.grid(row=1,column=0,pady=2)



fpath = os.path.join(prj_home, "plot2.png")
img3=cv2.imread(fpath)
img3=cv2.resize(img3,(470,405))
cv2.imwrite(fpath,img3)
plot3 = PhotoImage(file= fpath, master=win)
plot3Label = Label(QMLframe,image=plot3)
plot3Label.grid(row=1,column=1,padx=2,pady=1)


file6=os.path.join(prj_home, "video1.mp4")
im6,length6=imgseq(file6)   
count6 = 0
fpath = os.path.join(prj_home, "qc.png")
ini_pic6=PhotoImage(file = fpath, master=win)
gif_label6 = Label(QMLframe,image=ini_pic6,border=5,width=450,height=400)
gif_label6.grid(row=1,column=2,pady=2,padx=2)




##-----------------END of model 3-----------------#







##--------------start of model 4------------------#

hyQMLframe=LabelFrame(second_frame,text="",padx=0,pady=0,bg="#ffffff",border=1)
hyQMLframe.grid(row=4,columnspan=8,pady=10)              


hyQMLcap=Label(hyQMLframe,text="hybrid GCN",font=('Arial 16'),width=140,height=1,bg="#00005f",fg="#ffffff")
hyQMLcap.grid(row=0,column=0,columnspan=8,padx=0)

file7=os.path.join(prj_home, "video1.mp4")
im7,length7=imgseq(file7)   
count7 = 0
fpath = os.path.join(prj_home, "qc.png")   
ini_pic7=PhotoImage(file = fpath, master=win)
gif_label7 = Label(hyQMLframe,image=ini_pic7,border=5,width=450,height=400)
gif_label7.grid(row=1,column=0,pady=2)



fpath = os.path.join(prj_home, "plot2.png")
img4=cv2.imread(fpath)
img4=cv2.resize(img4,(470,405))
cv2.imwrite(fpath,img4)
plot4 = PhotoImage(file= fpath, master=win)
plot4Label = Label(hyQMLframe,image=plot4)
plot4Label.grid(row=1,column=1,padx=2,pady=1)


file8=os.path.join(prj_home, "video1.mp4")
im8,length8=imgseq(file8)   
count8 = 0
fpath = os.path.join(prj_home, "qc.png")
ini_pic8=PhotoImage(file = fpath, master=win)
gif_label8 = Label(hyQMLframe,image=ini_pic8,border=5,width=450,height=400)
gif_label8.grid(row=1,column=2,pady=2,padx=2)




##-----------------END of model 4-----------------#



##----------------TABLE---------------------------#

parent_table=LabelFrame(second_frame,padx=0,pady=0,bg="#EBEBEB",border=0)
parent_table.grid(row=5,column=0,columnspan=3)
  
tabcap=Label(parent_table,text="Comparison Table",font=('Arial 16'),width=140,height=2,bg="#00005f",fg="#ffffff")
tabcap.grid(row=0,column=0)

tableframe=LabelFrame(parent_table,padx=2,pady=2,bg="#EBEBEB",border=1)
tableframe.grid(row=1,column=0)                 
                      
s=ttk.Style() 
s.configure('Treeview', rowheight=25)               
tree = ttk.Treeview(tableframe,height=5)

tree['columns']=('Model',"RMSE","Time")

tree.column('#0',width=0)
tree.column('Model',width=450)
tree.column('RMSE',width=475)            
tree.column('Time',width=450)

tree.heading('#0',text="")
tree.heading('Model',text="Model")
tree.heading('RMSE',text="RMSE")
tree.heading('Time',text="Time")             

tree.grid(row=0,column=0,pady=25)

tree.insert(parent='',index='end',iid = 0, text="",values=("MGN","22.3","55sec"))
tree.insert(parent='',index='end',iid = 1, text="",values=("GCN","2.3","5sec"))
tree.insert(parent='',index='end',iid = 2, text="",values=("Hybrid GCN","0.3","0.5sec"))


win.mainloop()