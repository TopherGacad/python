# GACAD, CHRISTOPHER B. DICT 3-1
# CRUD OPERATION USING TKINTER AND MYSQL DB

from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def Insert():
    id = id_enter.get()
    name = name_enter.get()
    cpnum = cp_enter.get()

    if(id == "" or name == "" or cpnum == ""):
        MessageBox.showwarning("ALERT", "All fields are Required!")
    else:
        con = mysql.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="pydatabase")
        cursor = con.cursor()
        cursor.execute("INSERT INTO customer VALUES('" + id +"', '"+ name +"', '" + cpnum +"')")
        cursor.execute("commit")

        MessageBox.showinfo("Status","Info Successfully Inserted")
        con.close();

def Delete():
    if(id_enter.get() ==""):
        MessageBox.showwarning("ALERT","Please Enter ID to delete")
    else:
        con = mysql.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="pydatabase")
        cursor = con.cursor()
        cursor.execute("DELETE FROM customer WHERE id='"+ id_enter.get() +"'")
        cursor.execute("commit");
        id_enter.delete(0, 'end')
        name_enter.delete(0, 'end')
        cp_enter.delete(0, 'end')
  
        MessageBox.showinfo("Status", "Deleted Successfully")
        con.close();

def Update():
    id = id_enter.get()
    name = name_enter.get()
    cpnum = cp_enter.get()
    
    if(name_enter.get()=="" or cp_enter.get()==""):
        MessageBox.showwarning("ALERT","All fields are Required")
    else:
        con = mysql.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="pydatabase")
        cursor = con.cursor()
        cursor.execute("UPDATE customer SET name = '"+ name +"', cpnum='"+ cpnum +"' WHERE id ='"+ id +"'")
        cursor.execute("commit")

        MessageBox.showinfo("Status","Info Updated")
        con.close();
  
def Select():
  
   if(id_enter.get() == ""):
       MessageBox.showwarning("ALERT","ID is required to select Info!")
   else:
       con = mysql.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="pydatabase")
       cursor = con.cursor()
       cursor.execute("SELECT * FROM customer WHERE id= '" + id_enter.get() +"'")
       rows = cursor.fetchall()
  
       for row in rows:
           name_enter.insert(0, row[1])
           cp_enter.insert(0, row[2])
  
       con.close();
def Clear():
    id_enter.delete(0,'end')
    name_enter.delete(0,'end')
    cp_enter.delete(0,'end')
    
def Next():
    id = id_enter.get()
    name = name_enter.get()
    cpnum = cp_enter.get()

    if(id == "" or name == "" or cpnum == ""):
        MessageBox.showwarning("ALERT", "All fields are Required!")
    else:
        con = mysql.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="pydatabase")
        cursor = con.cursor()
        cursor.execute("INSERT INTO customer VALUES('" + id +"', '"+ name +"', '" + cpnum +"')")
        cursor.execute("commit")
        

        MessageBox.showinfo("Status","Info Successfully Inserted")
        con.close();
    
    id_enter.delete(0,'end')
    name_enter.delete(0,'end')
    cp_enter.delete(0,'end')


#GUI USING TKINTER
root = Tk()
root.title("CRUD OPERATION")
root.configure(bg='#36393F')
root.geometry('550x550')
root.resizable(0,0)

#WINDOW TITLE SYNTAX
title = Label(text="FILL OUT THE FOLLOWING", font='Consolas 15', bg='#36393F',fg='white')
title.place(x=160, y=0)

#ID LABEL AND INPUT TEXT BOX
id = Label(root, text="Enter ID #:", font=60, bg='#36393F',fg='white') 
id.place(x=70,y=70)
id_enter = Entry(root,font=('Consolas', 18)) 
id_enter.place(x=220, y=70)

#NAME LABEL AND INPUT TEXT BOX
name = Label(root, text="Enter the Name:", font=60, bg='#36393F',fg='white') 
name.place(x=70,y=110)
name_enter= Entry(root,font=('Consolas', 18)) 
name_enter.place(x=220, y=110)

#PHONE NUMBER LABEL AND INPUT TEXT BOX
cpnum = Label(root, text="Enter Phone #:", font=60,bg='#36393F',fg='white') 
cpnum.place(x=70,y=150)
cp_enter = Entry(root,font=('Consolas', 18)) 
cp_enter.place(x=220, y=150)

#BUTTON GUI
btnInsert = Button(root, text = 'Insert', command=Insert,bg='#ffb3fe', height=2, width=45)
btnInsert.place(x=120, y=210)
btnDelete = Button(root, text = 'Delete', command=Delete,bg='#ffb3fe', height=2, width=45)
btnDelete.place(x=120, y=260)
btnUpdate = Button(root, text = 'Update', command=Update, bg='#ffb3fe', height=2, width=45)
btnUpdate.place(x=120, y=310)
btnSelect = Button(root, text = 'Select', command=Select, bg='#ffb3fe', height=2, width=45)
btnSelect.place(x=120, y=360)

btnPrevious = Button(root, text = '<Previous',  bg='#ffb3fe', height=2, width=21)
btnPrevious.place(x=120, y=410)
btnNext = Button(root, text = 'Next>', command=Next, bg='#ffb3fe', height=2, width=21)
btnNext.place(x=290, y=410)

btnClear = Button(root, text = 'Clear', command=Clear,  bg='#ffb3fe', height=2, width=45)
btnClear.place(x=120, y=460)

root.mainloop()