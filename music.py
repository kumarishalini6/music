import os
from tkinter import *

from pygame import mixer
import tkinter.messagebox as mb 
from tkinter import filedialog
from ttkthemes import themed_tk as tk
from tkinter import   ttk


def aboutus():
    mb.showinfo("welcome","This is the information you want")
def file():
    global filename
    filename=filedialog.askopenfilename()
    print(filename)


root=tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")
menubar=Menu(root)
root.config(menu=menubar)

subMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Open",command=file)
subMenu.add_command(label="Exit",command=root.destroy)

subMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label="About Us",command=aboutus)



mixer.init()
root.title("Music player")
root.iconbitmap(r'C:\Users\Asus\Desktop\project1\music.ico')
root.geometry("650x410")
root.resizable(0,0)

Label(root,text="Let's make some noice",fg="darkorange",font=("arial",30,'bold','italic')).pack()

def Play():
    global paused
    if paused:
        mixer.music.unpause()
        statusbar['text']="music resumed"
        paused=FALSE
    else:
        
        try:
            selected_song = lab.curselection()
            selected_song= int(selected_song[0])
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text']="Music is playing"+ '      '+os.path.basename(play_it)
        
        except:
            mb.showerror("error file not found","music could not find the file. please check again ")
      
    
def Stop():
   
    mixer.music.stop()
    statusbar['text']="music is stop"

paused=FALSE
def Pause():
    global paused
    paused=True 
    mixer.music.pause()
    statusbar['text']="music paused"     

def volume(val):
    volume= float(val)/100
    mixer.music.set_volume(volume)

def rewind():
    Play()
    mixer.music.play()
    statusbar['text']="Music Rewinded"   

def mute():
    global muted
    
    mixer.music.set_volume(0)
    scale.set(0)

def volume2():

    mixer.music.set_volume(0.5)
    scale.set(50)
    





photo1=PhotoImage(file="Stopbtn.png")
ttk.Button(root,image=photo1,command=Stop).place(x=427,y=140)
photo2=PhotoImage(file="Playbtn.png")
ttk.Button(root,image=photo2,command=Play).place(x=323,y=140)
photo3=PhotoImage(file="pausebtn.png")
ttk.Button(root,image=photo3,command=Pause).place(x=530,y=140)
photo4=PhotoImage(file="5tgh.png")
ttk.Button(root,image=photo4,command=rewind).place(x=300,y=250)
photo5=PhotoImage(file="mutebtn.png")
ttk.Button(root,image=photo5,command=mute).place(x=380,y=250)
photo6=PhotoImage(file="volume.png")
ttk.Button(root,image=photo6,command=volume2).place(x=560,y=250)

scale=ttk.Scale(root,from_=0,to_=100,orient=HORIZONTAL,command=volume)
scale.set(50)
mixer.music.set_volume(0.5)
scale.place(x=456,y=268)

playlist = []

def browser():
    global filename
    filename=filedialog.askopenfilename()
    add_to_playlist(filename)

def add_to_playlist(f):
    f=os.path.basename(f)
    index=0
    lab.insert(index,f)
    playlist.insert(index,filename)
    index +=1 
    
def delete():
    selected_song = lab.curselection()
    selected_song= int(selected_song[0])
    lab.delete(selected_song)        

    
       

lab=Listbox(root,width=30,height=14)
lab.insert(0)
lab.insert(1)
lab.place(x=40,y=75)
Button(root,text="+ADD",bd=10,font=("arial",10,'bold'),width=14,command=browser).place(x=20,y=333)
Button(root,text="- DEL",bd=10,font=("arial",10,'bold'),width=14,command=delete).place(x=165,y=333)

statusbar=ttk.Label(root,text="Welcome to music player",relief=SUNKEN,anchor=W,font="times 12 bold italic")
statusbar.pack(side=BOTTOM,fill=X)

root.mainloop()