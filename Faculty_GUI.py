from tkinter import *
from PIL import ImageTk, Image
import mysql.connector as sql
import User_GUI_VI as user 
import time

mysql=sql.connect(
                host="localhost",
                user="root",
                passwd="",
                database="rahul_db"
                )
class Database:
    def _init__(self):
        print("hello")
    def fetchFacultyRow(self,Query):
        query=Query                 
        self.cur=mysql.cursor()
        self.cur.execute(query)
        rows=self.cur.fetchall()
        return rows 

class FacultyDetail(Database):
    def __init__(self,name=None):
        self.facultyUI=Tk()
        self.facultyUI.geometry("820x650")
        self.facultyUI.resizable(False,False)
        self.facultyUI.title("Faculty Details")
        self.name=name
        print(self.name)
        
        self.Initial_Frame=Frame(self.facultyUI,relief="groove",borderwidth=7, ) 
        self.Init_Container=Canvas(self.Initial_Frame)
        self.YScroll=Scrollbar(self.Initial_Frame,orient="vertical",command=self.Init_Container.yview)
        self.ScrollFrame=Frame(self.Init_Container)
        self.ScrollFrame.bind(
                "<Configure>",
                lambda e:self.Init_Container.configure(
                        scrollregion=self.Init_Container.bbox("all")
                    )
            )
        self.Init_Container.create_window((200,100),window=self.ScrollFrame,anchor=NW)
        self.Init_Container.configure(yscrollcommand=self.YScroll.set)
         
        FacUI=Database()
        #----------------------------------------------------------------------#
        self.FacUI_rows=FacUI.fetchFacultyRow("SELECT * FROM faculty")        
        #----------------------------------------------------------------------#
        self.Lbl_F=Label(self.ScrollFrame,text="",relief="raised",background='burlywood1',height=2)
        self.Lbl_F.grid(row=0,column=0,sticky=E,padx=2,pady=2,columnspan=2)

        self.Lbl_Fac=['','','','','','']
        self.FacImg1=self.createFacImg(self.FacUI_rows[0])
        self.Lbl_Fac0=Button(self.ScrollFrame,text="",image=self.FacImg1,relief="raised",background='burlywood1',activebackground=None,command=lambda e=self.FacUI_rows[0]:self.Fac_Detail(e,self.FacImg1),height=265,width=285)
        self.Lbl_Fac0.grid(row=1,column=1,sticky=E,padx=2,pady=2)

        self.FacImg2=self.createFacImg(self.FacUI_rows[1])
        self.Lbl_Fac1=Button(self.ScrollFrame,text="",image=self.FacImg2,relief="raised",background='burlywood1',activebackground=None,command=lambda e=self.FacUI_rows[1]:self.Fac_Detail(e,self.FacImg2),height=265,width=285)
        self.Lbl_Fac1.grid(row=1,column=2,sticky=E,padx=2,pady=2)

        self.FacImg3=self.createFacImg(self.FacUI_rows[2])
        self.Lbl_Fac2=Button(self.ScrollFrame,text="",image=self.FacImg3,relief="raised",background='burlywood1',activebackground=None,command=lambda e=self.FacUI_rows[2]:self.Fac_Detail(e,self.FacImg3),height=265,width=285)
        self.Lbl_Fac2.grid(row=2,column=1,sticky=E,padx=2,pady=2)

        self.FacImg4=self.createFacImg(self.FacUI_rows[3])
        self.Lbl_Fac3=Button(self.ScrollFrame,text="",image=self.FacImg4,relief="raised",background='burlywood1',activebackground=None,command=lambda e=self.FacUI_rows[3]:self.Fac_Detail(e,self.FacImg4),height=265,width=285)
        self.Lbl_Fac3.grid(row=2,column=2,sticky=E,padx=2,pady=2)

        self.FacImg5=self.createFacImg(self.FacUI_rows[4])
        self.Lbl_Fac4=Button(self.ScrollFrame,text="",image=self.FacImg5,relief="raised",background='burlywood1',activebackground=None,command=lambda e=self.FacUI_rows[4]:self.Fac_Detail(e,self.FacImg5),height=265,width=285)
        self.Lbl_Fac4.grid(row=3,column=1,sticky=E,padx=2,pady=2)

        self.FacImg6=self.createFacImg(self.FacUI_rows[5])
        self.Lbl_Fac5=Button(self.ScrollFrame,text="",image=self.FacImg6,relief="raised",background='burlywood1',activebackground=None,command=lambda e=self.FacUI_rows[5]:self.Fac_Detail(e,self.FacImg6),height=265,width=285)
        self.Lbl_Fac5.grid(row=3,column=2,sticky=E,padx=2,pady=2)

        #---------------------------------------------------------#
        self.Fac_Header=Label(self.Init_Container,text="Faculty Tab",font=('Times New Roman',14,'bold'),relief="groove",bg='IndianRed1',height=2,width=71)
        self.Fac_Header.grid(row=0,column=0)
        self.Back=Button(self.Fac_Header,text="Close",command=self.Fac_exit).place(x=730,y=5)
        #-----------------------------------------------------------#

        self.Lbl_Fac0.bind('<Enter>', lambda e:self.Lbl_Fac0.config(background='MediumOrchid4'))
        self.Lbl_Fac1.bind('<Enter>', lambda e:self.Lbl_Fac1.config(background='MediumOrchid4'))
        self.Lbl_Fac2.bind('<Enter>', lambda e:self.Lbl_Fac2.config(background='MediumOrchid4'))
        self.Lbl_Fac3.bind('<Enter>', lambda e:self.Lbl_Fac3.config(background='MediumOrchid4'))
        self.Lbl_Fac4.bind('<Enter>', lambda e:self.Lbl_Fac4.config(background='MediumOrchid4'))
        self.Lbl_Fac5.bind('<Enter>', lambda e:self.Lbl_Fac5.config(background='MediumOrchid4'))

        self.Lbl_Fac0.bind('<Leave>', lambda e:self.Lbl_Fac0.config(background='wheat1'))
        self.Lbl_Fac1.bind('<Leave>', lambda e:self.Lbl_Fac1.config(background='wheat1'))
        self.Lbl_Fac2.bind('<Leave>', lambda e:self.Lbl_Fac2.config(background='wheat1'))
        self.Lbl_Fac3.bind('<Leave>', lambda e:self.Lbl_Fac3.config(background='wheat1'))
        self.Lbl_Fac4.bind('<Leave>', lambda e:self.Lbl_Fac4.config(background='wheat1'))
        self.Lbl_Fac5.bind('<Leave>', lambda e:self.Lbl_Fac5.config(background='wheat1'))
         #-------------------------------------------------------------------#
        self.SideSection=Label(self.Init_Container,relief="groove",bg='dodger blue',height=39,width=26) #height=30
        self.SideSection.grid(row=1,column=0,sticky=W,pady=2)
        self.Subm_Btn=Button(self.SideSection,text="See Submissions",relief="raised",command=self.Show_Submission)
        self.Subm_Btn.place(x=40,y=50,height=25,width=100)
        image1 = Image.open("roboo.jpg")
        test = ImageTk.PhotoImage(image1)
        self.label = Label(self.SideSection,image=test)
        self.label.image = test
        self.label.place(x=1, y=90,height=300,width=180)
        #--------------------------------------------------------------------#   
        #########################+++++++++++++++++++++++++#####################
        self.Initial_Frame.pack(fill=BOTH,expand=True)
        self.Init_Container.pack(side=LEFT, fill=BOTH, expand=True)
        self.YScroll.pack(side=RIGHT,fill=Y)

        self.facultyUI.protocol("WM_DELETE_WINDOW", self.Fac_exit) #exit button and open Student Interface

    def createFacImg(self,FacUI_row):
        IMGfac = Image.open(FacUI_row[1]) #FacUI_row[1]=self.FacUI_rows[i][1] from upper function
        IMGfac=IMGfac.resize((240,220))
        #IMGfac.thumbnail((300,300))
        IMGfacPic=ImageTk.PhotoImage(IMGfac)
        return IMGfacPic

    def Fac_Detail(self,FacUI_row,Fac_img):
        self.FacImg=Fac_img #Image of faculty
        self.Fac_Dept=FacUI_row[2] #department
        self.Fac_Name=FacUI_row[3] #Name of faculty
        self.Fac_Email=FacUI_row[4] #email of faculty
        self.Subject=FacUI_row[5] #Subject

        self.ShowFac=Toplevel(self.facultyUI)
        self.ShowFac.title("Faculty Detail: {}".format(self.Fac_Name))
        self.ShowFac.geometry("380x370")
        self.ShowFac.resizable(False,False)

        self.ShowFrame=Frame(self.ShowFac,relief="groove",borderwidth=3)
        self.ShowFrame.pack()

        self.Imglbl=Label(self.ShowFrame,image=self.FacImg,background='burlywood1',height=250,width=270).grid(row=0,column=0,columnspan=2)
        #self.Imglbl=Label(self.ShowFrame,image=self.FacImg,background='burlywood1',height=250,width=270).grid(row=0,column=1)
        Label_Name=['Department','Name','Email-ID','Subject']
        for i in range(4):
            Fac_Label=Label(self.ShowFrame,text=Label_Name[i],relief='groove',borderwidth=2).grid(row=i+1,column=0,padx=2,pady=2,sticky='ew')
            Fac_Show=Label(self.ShowFrame,text=FacUI_row[i+2],relief='groove',borderwidth=2).grid(row=i+1,column=1,padx=2,pady=2,sticky='ew')



    def Show_Submission(self):
        self.Initial_Frame.pack_forget(); 
        self.Submission_Frame=Frame(self.facultyUI,relief="groove",borderwidth=7)
        
        self.Subm_Container=Canvas(self.Submission_Frame)
        self.YScroll=Scrollbar(self.Submission_Frame,orient="vertical",command=self.Subm_Container.yview)

        self.Subm_ScrollFrame=Frame(self.Subm_Container)
        self.Subm_ScrollFrame.bind(
                "<Configure>",
                lambda e:self.Subm_Container.configure(
                        scrollregion=self.Subm_Container.bbox("all")
                    )
            )
        self.Subm_Container.create_window((200,100),window=self.Subm_ScrollFrame,anchor=NW)
        self.Subm_Container.configure(yscrollcommand=self.YScroll.set)
        #-------------------------------------#
        self.Fac_Header=Label(self.Subm_Container,text="Submissions",font=('Times New Roman',14,'bold'),relief="groove",fg="yellow",bg='SteelBlue',height=2,width=71)
        self.Fac_Header.grid(row=0,column=0)
        self.Back=Button(self.Fac_Header,text="Close",command=self.Fac_exit).place(x=730,y=5)
        #-------------------------------------#
        self.Subm_Lbl_F=Label(self.Subm_ScrollFrame,text="",relief="raised",background='burlywood1',height=1)
        self.Subm_Lbl_F.grid(row=0,column=0,sticky=E,padx=2,pady=2)
        #------------------------------------------------#
        self.SideSection=Label(self.Subm_Container,relief="groove",bg="tomato2",height=39,width=30) #height=30
        self.SideSection.grid(row=1,column=0,sticky=W,pady=2)  
        image1 = Image.open("write.png")
        test = ImageTk.PhotoImage(image1)
        self.label2 = Label(self.SideSection,image=test)
        self.label2.image = test
        self.label2.place(x=1, y=90,height=400,width=280)
        #--------------------------------------------------#
        self.Go_Back=Button(self.SideSection,text="Faculty Details",relief="raised",command=self.exitSubm)
        self.Go_Back.place(x=40,y=50,height=25,width=100)
        #--------------------------------------------------#
        
        FacUI=Database()
        self.Submission_rows=FacUI.fetchFacultyRow("SELECT * FROM subm_detail") 
        
        self.Lbl_F=Label(self.ScrollFrame,text="RRRRRRRRRRRR",font=('Comics Sans',17,'bold'),relief="raised",background='burlywood1',height=2)
        self.Lbl_F.grid(row=0,column=0,sticky=EW,padx=2,pady=2)
        for i in range(1,len(self.Submission_rows)+1):
            self.Subm_Tab=Frame(self.Subm_ScrollFrame,bg="IndianRed2",height=140,width=390) #Frame is more stable to show content in scrolling window                                      
            self.Subm_Tab.grid(row=i,column=0,sticky=EW,padx=100,pady=10)
            self.Subm_Name=Label(self.Subm_Tab,text="Submission Name : {}".format(self.Submission_rows[i-1][1]),font=('Times New Roman',14,'bold'),fg="white",bg="SlateBlue4").place(x=10,y=10)
            self.Subm_subj=Label(self.Subm_Tab,text="Subject : {}".format(self.Submission_rows[i-1][2]),bg="lightblue").place(x=10,y=40)
            self.Subm_Deadline=Label(self.Subm_Tab,text="Deadline : {}".format(self.Submission_rows[i-1][3]),bg="lightpink").place(x=10,y=70)
            self.Subm_Detail_Btn=Button(self.Subm_Tab,text="View",command=lambda e=self.Submission_rows[i-1]:self.Subm_Detail(e)).place(x=10,y=100)
                                                                 

        self.Submission_Frame.pack(fill=BOTH,expand=True)
        self.Subm_Container.pack(side=LEFT, fill=BOTH, expand=True)
        self.YScroll.pack(side=RIGHT,fill=Y)

    def Subm_Detail(self,Subm_row):
        self.Show_Subm=Toplevel(self.facultyUI)
        self.Show_Subm.title("Submission Detail: {}".format(Subm_row[2]))
        self.Show_Subm.geometry("380x370")
        self.Show_Subm.resizable(False,False)

        self.Subm_Frame=Frame(self.Show_Subm,relief="groove",borderwidth=3)
        self.Subm_Frame.pack()
        Subm_Label=['Submission Name','Subject','Due Date','Description']
        for i in range(4):
            Fac_Label=Label(self.Subm_Frame,text=Subm_Label[i],relief='groove',borderwidth=2).grid(row=i,column=0,padx=2,pady=2,sticky='ewns')
            Fac_Show=Label(self.Subm_Frame,text=Subm_row[i+1],relief='groove',borderwidth=2,wraplength=250).grid(row=i,column=1,padx=2,pady=2,sticky='ew')

    def exitSubm(self):
        self.Submission_Frame.pack_forget();
        self.Initial_Frame.pack(fill=BOTH,expand=True);

    def Fac_exit(self):
        self.facultyUI.destroy()
        print(self.name)
        std_user=user.UserUI(self.name)

    def UI_mainloop(self):
        self.facultyUI.mainloop()

if __name__ == "__main__":
    FacultyUI=FacultyDetail()

    FacultyUI.UI_mainloop()
    data=Database()
