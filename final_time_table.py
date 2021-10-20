from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

import User_GUI_VI as user

mydb = mysql.connector.connect(host="localhost",
  user="root", 
  passwd="",
  database="rahul_db")

cursor = mydb.cursor()
sql = "SELECT * from student_timetable" 
cursor.execute(sql)
rows = cursor.fetchall()
total = cursor.rowcount
print("total data entries: "+str(total))

def TimeTable(name=None):
	root = Tk()
	root.title("aanshi")
	root.geometry("800x500")
	root.resizable(False, False)
	Uname=name
	label = Label(root, text = "TE TIME TABLE", font =("Comic Sans MS", 18, "bold")).pack()


	style = ttk.Style()
	style.theme_use("default")

	style.configure("Treeview", 
		background="#D3D3D3",
		foreground="black",
		rowheight=30,
		fieldbackground="#D3D3D3"
		)

	style.map('Treeview', 
		background=[('selected', 'blue')])

	# Create Treeview Frame
	tree_frame = Frame(root)
	tree_frame.pack(pady=30,padx=20)

	my_tree = ttk.Treeview(tree_frame, height =5)
	my_tree.pack()


	# Define Our Columns
	my_tree['columns'] = ("TIME","MONDAY", "TUESDAY", "WEDNESDAY","THURSDAY", "FRIDAY")

	# Formate Our Columns
	my_tree.column("#0", width=0, stretch=NO)
	my_tree.column("TIME", anchor=CENTER, width=135)
	my_tree.column("MONDAY", anchor=CENTER, width=135)
	my_tree.column("TUESDAY", anchor=CENTER, width=90)
	my_tree.column("WEDNESDAY", anchor=CENTER, width=135)
	my_tree.column("THURSDAY", anchor=CENTER, width=135)
	my_tree.column("FRIDAY", anchor=CENTER, width=135)

	# Create Headings 
	my_tree.heading("#0", text="", anchor=W)
	my_tree.heading("TIME", text="TIME", anchor=CENTER)
	my_tree.heading("MONDAY", text="MONDAY", anchor=CENTER)
	my_tree.heading("TUESDAY", text="TUESDAY", anchor=CENTER)
	my_tree.heading("WEDNESDAY", text="WEDNESDAY", anchor=CENTER)
	my_tree.heading("THURSDAY", text="THURSDAY", anchor=CENTER)
	my_tree.heading("FRIDAY", text="FRIDAY", anchor=CENTER)


	my_tree.tag_configure('oddrow', background="white")
	my_tree.tag_configure('evenrow', background="lightblue")
	my_tree.tag_configure('lunchrow', background="pink")


	global count
	count=1

	for i in rows:
		if count % 2 == 0:
			my_tree.insert(parent='', index='end', iid=count, text="", values=i, tags=('evenrow',))
		elif count==3:
			my_tree.insert(parent='', index='end', values=["13:15-14:00","L","U","N","C","H"], tags=('lunchrow',))
			my_tree.insert(parent='', index='end', iid=count, text="", values=i, tags=('oddrow',))

		else:
			my_tree.insert(parent='', index='end', iid=count, text="", values=i, tags=('oddrow',))

		count += 1

	blue_block = Label(root, bg='lightblue')  
	blue_block.place(x=20,y=260,width=300,height=210)
	title = Label(blue_block,text = "Faculty Abbreviation",font =("Comic Sans MS", 12, "bold"), bg='hotpink') 
	title.grid(row = 0, column = 1)

	sp_lable = Label(blue_block, text = "SP : ", font =("Comic Sans MS", 12, "bold") ,bg='lightblue') 
	sp_lable.grid(row = 1, column = 0)
	sp_lable1 = Label(blue_block, text = "Saurabh Patil ", font =("Comic Sans MS", 12, "bold") ,bg='lightblue') 
	sp_lable1.grid(row = 1, column = 1)
	km_lable = Label(blue_block, text = "KM : ", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	km_lable.grid(row = 2, column = 0)
	km_lable1 = Label(blue_block, text = "Kunal Mehra", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	km_lable1.grid(row = 2, column = 1)
	kj_lable = Label(blue_block, text = "KJ : ", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	kj_lable.grid(row = 3, column = 0)
	kj_lable1 = Label(blue_block, text = "Kavita Jain", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	kj_lable1.grid(row = 3, column = 1)
	sk_lable = Label(blue_block, text = "SK : ", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	sk_lable.grid(row = 4, column =0)
	sk_lable1 = Label(blue_block, text = "Sushama Khanvilkar", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	sk_lable1.grid(row = 4, column =1)
	sk_lable = Label(blue_block, text = "BJ : ", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	sk_lable.grid(row = 5, column =0)
	sk_lable1 = Label(blue_block, text = "Beatrice Jeevaraj", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	sk_lable1.grid(row = 5, column =1)
	sk_lable = Label(blue_block, text = "SG : ", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	sk_lable.grid(row = 6, column =0)
	sk_lable1 = Label(blue_block, text = "Saniya Gonsalves", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	sk_lable1.grid(row = 6, column =1)


	blue_block = Label(root, bg='lightblue') 
	blue_block.place(x=360,y=260,width=350,height=210)

	title = Label(blue_block,text = "Subject Abbreviation",font =("Comic Sans MS", 12, "bold"), bg='hotpink') 
	title.grid(row = 0, column = 1)

	sp_lable = Label(blue_block, text = "CN : ", font =("Comic Sans MS", 12, "bold") ,bg='lightblue') 
	sp_lable.grid(row = 1, column = 0)
	sp_lable1 = Label(blue_block, text = "Computer Networking ", font =("Comic Sans MS", 12, "bold") ,bg='lightblue') 
	sp_lable1.grid(row = 1, column = 1)
	km_lable = Label(blue_block, text = "IP : ", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	km_lable.grid(row = 2, column = 0)
	km_lable1 = Label(blue_block, text = "Internet Programming", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	km_lable1.grid(row = 2, column = 1)
	kj_lable = Label(blue_block, text = "DWM : ", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	kj_lable.grid(row = 3, column = 0)
	kj_lable1 = Label(blue_block, text = "Data Warehouse and Mining", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	kj_lable1.grid(row = 3, column = 1)
	sk_lable = Label(blue_block, text = "TCS : ", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	sk_lable.grid(row = 4, column =0)
	sk_lable1 = Label(blue_block, text = "Theorotical Computer Science ", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	sk_lable1.grid(row = 4, column =1)
	sk_lable = Label(blue_block, text = "SE : ", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	sk_lable.grid(row = 5, column =0)
	sk_lable1 = Label(blue_block, text = "Software Engineering ", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	sk_lable1.grid(row = 5, column =1)
	sk_lable = Label(blue_block, text = "BCE : ", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	sk_lable.grid(row = 6, column =0)
	sk_lable1 = Label(blue_block, text = "Business Communication & Ethics ", font =("Comic Sans MS", 12, "bold"),bg='lightblue') 
	sk_lable1.grid(row = 6, column =1)
	root.protocol("WM_DELETE_WINDOW", lambda e="exit_TT":exit_timetable(root,Uname))

	return root,Uname

def exit_timetable(root,name):
	root.destroy()
	UserUI=user.UserUI(name)

if __name__ == "__main__":
	window,name=TimeTable()
	
	window.mainloop()