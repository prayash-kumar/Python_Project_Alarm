from tkinter import *
import datetime
import time
from pygame import mixer
from tkinter import messagebox


root = Tk()
root.title("Alarm Clock")
root.geometry("530x330")

alarmtime = StringVar()
msgi = StringVar()

head = Label(root,text="Alarm Clock",font=('comic sas',20))
head.grid(row=0,columnspan=3,pady=10)

mixer.init()

def check_alarm():
    alarm_time = alarmtime.get()
    AlarmT = alarm_time
    CurrentTime = time.strftime("%H:%M")

    while AlarmT != CurrentTime:
        CurrentTime = time.strftime("%H:%M")

    if AlarmT == CurrentTime:
        mixer.music.load("E:\\Python_Project_Alarm\\ringtone.mp3")
        mixer.music.play()
        msg = messagebox.showinfo('info',f'{msgi.get()}')

        if msg == 'ok':
          mixer.stop()

Clockimg = PhotoImage(file="E:\\Python_Project_Alarm\\al.png")


img = Label(root,image=Clockimg)
img.grid(rowspan=4,column=0)

inputt = Label(root,text="Input time",font=('comic sans',18))
inputt.grid(row=1,column=2)

altime = Entry(root,textvariable=alarmtime,font=('comic sans',18),width=6)
altime.grid(row=1,column=1)

msg = Label(root,text="Massage",font=('comic sans',18))
msg.grid(row=2,column=1,columnspan=2)

msginput = Entry(root,textvariable=msgi,font=('comic sans',18))
msginput.grid(row=3,column=1,columnspan=2)

submit = Button(root,text="SUBMIT",font=('comic sans',18),command=check_alarm)
submit.grid(row=4,column=1,columnspan=2)

root.mainloop()