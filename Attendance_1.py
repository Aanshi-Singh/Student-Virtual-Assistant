from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk

import User_GUI_VI as user

import mysql.connector
my_connect = mysql.connector.connect(
host="localhost",
user="root", 
passwd="",
database="rahul_db"
)
my_conn = my_connect.cursor()

def Show_Attendance(name=None):
	window=tk.Tk()
	window.geometry("600x600")
	window.title(" Attendance ")
	frame = Frame(window, borderwidth=7)
	frame.place(x=0,y=0,width=700,height=700)

	Uname=name

	lable = Label(frame, bg='lightblue')
	lable.place(x=0,y=0,width=599,height=599)

	Std_Header=Label(lable,height=1,text="ATTENDANCE",fg="white",bg="maroon4" ,width=55 ,font=('times', 20, ' bold ')).pack()

	sum =0
	name = tk.Label(lable, text = "Name: ",font =("Comic Sans MS", 16, "bold"),bg='light blue')
	name.place(x = 0, y = 230, height = 100, width = 100)

	my_conn.execute("SELECT Name FROM attendance WHERE Name='Aanshi'")
	records = my_conn.fetchone()
	query_label = Label(lable, text=records,font =("Comic Sans MS", 16, "bold"),bg='light blue')
	query_label.place(x = 150, y = 263)



	pink_block = Label(lable, bg='hotpink1',)  
	pink_block.place(x=10,y=320,width=450,height=160)

	CN = tk.Label(pink_block, text = "Computer Networking : ",font =("Comic Sans MS", 12, "bold"),bg='hotpink1')
	CN.place(x = 10 , y = 2)
	my_conn.execute("SELECT CN FROM attendance WHERE Name='Aanshi'")
	records = my_conn.fetchone()
	sum+=int(''.join(map(str, records)))
	query_label = Label(pink_block, text = ''.join(map(str, records))+"%",font =("Comic Sans MS", 12, "bold"),bg='hotpink1')
	query_label.place(x = 270 , y = 2)

	ip = tk.Label(pink_block, text = "Internet Programming : ",font =("Comic Sans MS", 12, "bold"),bg='hotpink1')
	ip.place(x = 10 , y = 50)
	my_conn.execute("SELECT IP FROM attendance WHERE Name='Aanshi'")
	records = my_conn.fetchone()
	sum+=int(''.join(map(str, records)))
	query_label = Label(pink_block, text=''.join(map(str, records))+"%",font =("Comic Sans MS", 12, "bold"),bg='hotpink1')
	query_label.place(x = 270 , y = 50)

	dwm = tk.Label(pink_block, text = "Data Warehouse and Mining : ",font =("Comic Sans MS", 12, "bold"),bg='hotpink1')
	dwm.place(x = 10 , y = 90)
	my_conn.execute("SELECT DWM FROM attendance WHERE Name='Aanshi'")
	records = my_conn.fetchone()
	sum+=int(''.join(map(str, records)))
	query_label = Label(pink_block, text=''.join(map(str, records))+"%",font =("Comic Sans MS", 12, "bold"),bg='hotpink1')
	query_label.place(x = 270 , y = 90)

	tcs = tk.Label(pink_block, text = "Theorotical Computer Science : ",font =("Comic Sans MS", 12, "bold"),bg='hotpink1')
	tcs.place(x = 10 , y = 130)
	my_conn.execute("SELECT DWM FROM attendance WHERE Name='Aanshi'")
	records = my_conn.fetchone()
	sum+=int(''.join(map(str, records)))
	query_label = Label(pink_block, text=''.join(map(str, records))+"%",font =("Comic Sans MS", 12, "bold"),bg='hotpink1')
	query_label.place(x = 270 , y = 130)

	dwm = tk.Label(pink_block, text = "Theorotical Computer Science : ",font =("Comic Sans MS", 12, "bold"),bg='hotpink1')
	dwm.place(x = 10 , y = 180)
	my_conn.execute("SELECT DWM FROM attendance WHERE Name='Aanshi'")
	records = my_conn.fetchone()
	sum+=int(''.join(map(str, records)))
	query_label = Label(pink_block, text=''.join(map(str, records))+"%",font =("Comic Sans MS", 12, "bold"),bg='hotpink1')
	query_label.place(x = 270 , y = 180)



	atten_label=Label(lable,text="As per the calcutation your Attendance is: "+str(sum/5)+"%",bg="pink", padx = 20, pady =15)
	atten_label.place(x=150, y= 500)

	image1 = Image.open("download.png")
	image1.thumbnail((1000,1000),Image.ANTIALIAS)
	test = ImageTk.PhotoImage(image1)
	label2 = Label(lable,image=test, background = "red")
	label2.image = test
	label2.place(x=0, y=50, width = 600)
	window.protocol("WM_DELETE_WINDOW", lambda e="exit_Attendance":exit_Attendance(window,Uname))
	return window,Uname

def exit_Attendance(window,name):
	window.destroy()
	UserUI=user.UserUI(name)

if __name__ == "__main__":
	window,name=Show_Attendance()
	
	window.mainloop()