
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time

import User_GUI_VI as user
import Register_Student as reg_std
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

#def tick():
 #   time_string = time.strftime('%H:%M:%S')
 #   clock.config(text=time_string)
 #   clock.after(200,tick)

def contact():
    mess._show(title='Contact us', message="Please contact us on : 'shubhamkumar8180323@gmail.com' ")
def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()
def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    op = (old.get())
    newp= (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("TrainingImageLabel\psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return
    mess._show(title='Password Changed', message='Password changed successfully!!')
    master.destroy()
def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False,False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master,text='    Enter Old Password',bg='white',font=('times', 12, ' bold '))
    lbl4.place(x=10,y=10)
    global old
    old=tk.Entry(master,width=25 ,fg="black",relief='solid',font=('times', 12, ' bold '),show='*')
    old.place(x=180,y=10)
    lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black",relief='solid', font=('times', 12, ' bold '),show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid',font=('times', 12, ' bold '),show='*')
    nnew.place(x=180, y=80)
    cancel=tk.Button(master,text="Cancel", command=master.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()


def disable_exit():
    pass


###########################################################################################
def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Login/")
    assure_path_exists("StudentDetails/")

    msg = ''
    i = 0
    j = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
    if exists3:
        recognizer.read("TrainingImageLabel\Trainner.yml")
    else:
        mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
        return
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists1:
        df = pd.read_csv("StudentDetails\StudentDetails.csv")
    else:
        mess._show(title='Details Missing', message='Students details are missing, please check!')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)
                ID = ID[1:-1]
                bb = str(aa)
                bb = bb[2:-2]
                attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]

            else:
                Id = 'Unknown'
                bb = str(Id)
            cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('Facial Log-In', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    exists = os.path.isfile("Login\LoginRec_" + date + ".csv")
    if bb!='Unknown': #### new added: "bb!='Unknown' " and a big if loop
        Correct_Login=tk.Label(frame1,text="Recognized student: {}".format(bb),bg="green").grid(row=2,column=0,padx=(80,0),pady=(150,0))##################
        
        if exists:
            with open("Login\LoginRec_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(attendance)
            csvFile1.close()
        else:
            with open("Login\LoginRec_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)
            csvFile1.close()
        with open("Login\LoginRec_" + date + ".csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for lines in reader1:
                i = i + 1
                if (i > 1):
                    if (i % 2 != 0):
                        iidd = str(lines[0]) + '   '
                        #tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
        csvFile1.close()
        #tv.destroy()#####################
        #scroll.destroy()#########################
        cam.release()
        window.destroy()
        cv2.destroyAllWindows()
        #import User_GUI_VI as user
        std_user=user.UserUI(bb) #passing student name
    else: #### new added: "bb!='Unknown' " and a big if loop [this is the 'else' of that 'if' loop]
        #tv.destroy()#####################
        #scroll.destroy()#####################
        cam.release()
        Unknown_Login=tk.Label(frame1,text="Sorry!, Not recognized",fg='white',bg="red",font=('Times New Roman',16)).grid(row=2,column=0,padx=(130,0),pady=(70,0)) #pady=(150,0)
        cv2.destroyAllWindows()



global key
key = ''
ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")
mont={'01':'January',
      '02':'February',
      '03':'March',
      '04':'April',
      '05':'May',
      '06':'June',
      '07':'July',
      '08':'August',
      '09':'September',
      '10':'October',
      '11':'November',
      '12':'December'
      }
######################################## GUI FRONT-END ###########################################
if __name__ == "__main__":
    #window=open_login()
    window = tk.Tk()
    window.geometry("760x450")
    window.resizable(False,False)
    window.title("Student GUI   -   Log-in ")
    window.configure(background='IndianRed1')####
    
    frame1 = tk.Frame(window, bg="khaki1") ##Attendance acceptance part of GUI
    frame1.place(x=140,y=105,width=480,height=300)
    
    #frame2 = tk.Frame(window, bg="#00aeff") #Image taking/ registering part of GUI
    #frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)
    
    message3 = tk.Label(window, text="Student Login Page" ,fg="white",bg="maroon4" ,width=55 ,height=1,font=('times', 18, ' bold '))
    message3.pack()
    
    #frame3 = tk.Frame(window, bg="#c4c6ce")
    #frame3.pack()
    #frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)
    
    frame4 = tk.Frame(window, bg="#c4c6ce")
    frame4.pack()
    #frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)
    
    datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"   ", fg="yellow",bg="maroon4" ,width=55 ,height=1,font=('times', 17, ' bold '))
    datef.pack(fill='both',expand=1)
    
    
    
    head1 = tk.Label(frame1, text="                          Try Logging-In !                           ", fg="black",bg="HotPink1" ,font=('times', 17, ' bold ') )
    head1.place(x=0,y=0)

    #lbl = tk.Label(frame2, text="Enter ID",width=20  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
    #lbl.place(x=80, y=55)

    #txt = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold '))
    #txt.place(x=30, y=88)

    #lbl2 = tk.Label(frame2, text="Enter Name",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
    #lbl2.place(x=80, y=140)

    #txt2 = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
    #txt2.place(x=30, y=173)

    #message1 = tk.Label(frame2, text="1)Take Images  >>>  2)Save Profile" ,bg="#00aeff" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
    #message1.place(x=7, y=230)

    #message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
    #message.place(x=7, y=450)

    lbl3 = tk.Label(frame1, text="Attendance",width=20  ,fg="black"  ,bg="#00aeff"  ,height=1 ,font=('times', 17, ' bold '))
    #lbl3.place(x=100, y=115)

    res=0
    exists = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                res = res + 1
        res = (res // 2) - 1
        csvFile1.close()
    else:
        res = 0
    #message.configure(text='Total Registrations till now  : '+str(res))

    

    trackImg = tk.Button(frame1, text="Log-In", command=TrackImages  ,fg="khaki1"  ,bg="maroon4"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
    trackImg.place(x=30,y=120)

    quitWindow = tk.Button(frame1, text="Quit", command=window.destroy  ,fg="khaki1"  ,bg="maroon4"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
    quitWindow.place(x=30, y=180)
    window.protocol("WM_DELETE_WINDOW", disable_exit)
    window.mainloop()
