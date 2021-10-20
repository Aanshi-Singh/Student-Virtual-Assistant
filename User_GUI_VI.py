from tkinter import *
from PIL import ImageTk, Image
import mysql.connector as sql
#import time
import Faculty_GUI as Fac 
import final_time_table as tt
import Attendance_1 as attnd

import speech_recognition as sr

r=sr.Recognizer()

mysql=sql.connect(
                host="localhost",
                user="root",
                passwd="",
                database="rahul_db"
                )

class DataBase:
    def __init__(self):
        print("hello")
        '''
        self.mysql=sql.connect(
                                host="localhost",
                                user="root",
                                passwd="",
                                database="rahul_db"
                                )'''
    def fetchRow(self):
        query="SELECT * FROM salesfact"
        cur=mysql.cursor()
        cur.execute(query)
        rows=cur.fetchall()
        return rows

class UserUI(DataBase):
    def __init__(self,name=None):
        self.userUI=Tk()
        self.userUI.geometry("800x600")
        self.userUI.resizable(0, 0)
        self.userUI.title("Student Interface")
        self.name=name

        self.VI_Frame=Frame(self.userUI,relief="groove",borderwidth=7,bg='light coral')
        self.VI_Frame.place(x=0,y=0,width=799,height=599)

        
        self.body = Image.open('chat_robo.jpg')
        self.body=self.body.resize((780,550))
        self.bodyPic=ImageTk.PhotoImage(self.body)
        self.bgLabel=Label(self.VI_Frame,bd=0,image=self.bodyPic)
        self.bgLabel.place(x=2,y=31)
        #self.bgLabel.pack(expand=True,fill="both",side="left")

        self.c1Img = Image.open('Mic_pic2.png')
        self.c1Img=self.c1Img.resize((80,80))
        self.c1Pic=ImageTk.PhotoImage(self.c1Img)
       
        self.StdInfo=Label(self.bgLabel,bg='LightCyan2',font=('Comics Sans',17,'italic'))
        if name != None:
            self.StdInfo.config(text="Welcome {}".format(name))
        self.StdInfo.place(x=20,y=20,width=370,height=95)
        self.VoiceTerminal=Label(self.VI_Frame,bg='dim gray')
        self.VoiceTerminal.place(x=400,y=160,width=370,height=395)

        self.Std_Header=Label(self.VI_Frame,height=1,text="Student Virtual Assistant",fg="white",bg="maroon4" ,width=55 ,font=('times', 20, ' bold ')).pack()
        self.LogoutBtn=Button(self.Std_Header,text="Log-out",command=self.User_Logout).pack(pady=10,padx=10,anchor='e')
        #---------------------------------------------------------#
        self.UserVoiceTerminal=Label(self.VoiceTerminal,bg='LightBlue1',wraplength=200,font=('Constantia 13 italic'))
        #self.UserVoiceTerminal.pack(pady=10,anchor='e')
        self.AdminVoiceTerminal1=Label(self.VoiceTerminal,bg='OliveDrab1',wraplength=200,font=('Constantia 13 italic'))
        self.AdminVoiceTerminal2=Label(self.VoiceTerminal,bg='red',fg="white",wraplength=200,font=('Constantia 13 italic'))
        self.AdminVoiceTerminal3=Label(self.VoiceTerminal,bg='OliveDrab1',wraplength=200,font=('Constantia 13 italic'))
        #self.AdminVoiceTerminal.pack(pady=10,anchor='w')
        #---------------------------------------------------------#
        self.AdminVoiceTerminal1.config(text="Hello {}, how may I help you?".format(self.name))
        self.AdminVoiceTerminal1.pack(pady=10,anchor='w')

        self.btnVoice=Button(self.VI_Frame,text="Speak",image=self.c1Pic,command=self.record,borderwidth = 9)
        self.btnVoice.place(x=550,y=499,width=80,height=80)

        self.menubar=Menu(self.userUI,background='DarkOliveGreen1',relief="groove")
        self.userUI.config(menu=self.menubar)
        Menubar=Menu(self.menubar,background='DarkOliveGreen1',font=('Constantia 13 italic'),relief="groove")

        self.menubar.add_cascade(label="Start Menu",menu=Menubar)
        Menubar.add_command(label="Hello!",command=self.hello)
        Menubar.add_command(label="Open",command=self.open)
        Menubar.add_separator()
        Menubar.add_command(label="Exit",command=self.userUI.destroy)

    def hello(self):
        #self.FrameExist("OpenFrame",OpenFrame.winfo_exists()) #if true returns 1 else return 0
        self.HelloFrame=Frame(self.userUI,relief="raised",borderwidth=10)
        self.HelloFrame.place(x=0,y=0,width=890,height=650)
        self.HelloLabel=Label(self.HelloFrame,text="Hello users in Hello frame",bg="OliveDrab1",font=('Constantia 13 italic'))
        self.HelloLabel.pack() 
        self.BackBtn=Button(self.HelloFrame,text="Go Back",command=self.HelloFrame.destroy,font=('Helvetica 13 bold'),relief="raised",borderwidth=4, activebackground='LightCyan3').pack()
    def open(self):
        #self.FrameExist("HelloFrame",self.HelloFrame.winfo_exists())  #if true returns 1 else return 0
        self.OpenFrame=Frame(self.userUI,relief="raised",borderwidth=10)
        self.OpenFrame.place(x=0,y=0,width=890,height=650)
        self.OpenLabel=Label(self.OpenFrame,text="Hello users in Open frame",bg="orchid2",font=('Constantia 13 italic'))
        self.OpenLabel.pack() 
        self.BackBtn=Button(self.OpenFrame,text="Go Back",command=self.OpenFrame.destroy,font=('Helvetica 13 bold'),relief="raised",borderwidth=4, activebackground='LightCyan3').pack()
            
    def FrameExist(self,frameName,frame):
        print("Frame: ",frameName," Exist?= ",frame)

    '''def printVoice(self):
        self.lbl_StoTxt=Label(self.userUI,text="",textvariable=self.VOICE,bg="LightCyan2",font=('Constantia 13 italic'))
        self.lbl_StoTxt.place(x=200,y=100)'''

    def PopUp(self,Speech): #New PopUp window
        
        self.HelloFrame=Frame(self.userUI,relief="raised",borderwidth=10)
        #self.HelloFrame.place(x=0,y=0,width=810,height=610)
 
        speech=Speech
        #speech=list(speech)
        #print(speech)
        self.UserVoiceTerminal.pack(pady=10,anchor='e')
        self.UserVoiceTerminal.config(text="{}".format(speech))
        print("before time delay")
        #time.sleep(10)
        if("database" in speech):
            db=DataBase()
            ROW=db.fetchRow()
            for row in ROW:
                self.HelloLabel=Label(self.VoiceTerminal,text="-{}-{}-{}-{}-{}-".format(row[0],row[1],row[2],row[3],row[4],row[5]),bg="OliveDrab1",font=('Constantia 13 italic'),wraplength=300)
                self.HelloLabel.pack(anchor='w') 
            
        else:
            #time.sleep(5)
            self.AdminVoiceTerminal2.pack(pady=10,anchor='w')
            self.AdminVoiceTerminal2.config(text="{}".format(speech))

        print("after time delay")
        self.AdminVoiceTerminal2.pack(pady=10,anchor='w')
        self.AdminVoiceTerminal2.config(text="{}".format(speech))
        if("faculty" in speech):
            self.userUI.destroy()
            FacUI=Fac.FacultyDetail(self.name)
        elif("submission" in speech):
            self.userUI.destroy()
            FacUI=Fac.FacultyDetail(self.name)
            FacUI.Show_Submission()
        elif("time table" in speech):
            self.userUI.destroy()
            timetable=tt.TimeTable(self.name)
        elif("attendance" in speech):
            self.userUI.destroy()
            attendance=attnd.Show_Attendance(self.name)
        else:
            self.AdminVoiceTerminal2.pack(pady=10,anchor='w')
            self.AdminVoiceTerminal2.config(text = "Sorry couldn't get you".format(speech))
            self.AdminVoiceTerminal3.pack(pady=10,anchor='w')
            self.AdminVoiceTerminal3.config(text = "Can only help you with: FACULTY DETAITS, YOUR ATTENDANCE, TIME TABLE AND SUBMISSIONS".format(speech))

    def User_Logout(self):
        import Login_Student as login
        self.userUI.destroy()

    def record(self): #record our voice and give a text output of it
        with sr.Microphone() as src:
            self.audio=r.listen(src)
            self.voice_data=''
            try:
                self.voice_data=r.recognize_google(self.audio)
            except sr.UnknownValueError:
                print("Couldn't get you Sir/Madam")
            except sr.RequestError:
                print("Service got down, sorry!")
            #self.VOICE=StringVar()
            self.VOICE=self.voice_data
            self.PopUp(self.VOICE)

    def UI_mainloop(self):
        self.userUI.mainloop()

if __name__ == "__main__":
    DB=DataBase()
    voiceUI=UserUI()

    voiceUI.UI_mainloop()
#userUI.mainloop()






