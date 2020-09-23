# import the tkinter framework
import tkinter as tk
from tkinter import messagebox 
from tkinter.scrolledtext import ScrolledText

# import ImageTk and Image from PIL library
from PIL import ImageTk,Image

root = tk.Tk()

#  set window title
root.title("Registration Form")

# set window size
root.geometry("1000x650")

# disable the minimize/maximize button
root.resizable(0,0)

# config window
BG = "#c8cbcf"
root.configure(bg=BG)


def Sgender():

    return var.get()
        
    
def submit():
    
    name = nameE.get()
    fatherName = fatherNameE.get()
    motherName = motherNameE.get()
    mobile = mobileE.get()
    address = addressE.get('1.0', 'end-1c')
    postOffice = postOfficeE.get()
    religion = religionE.get()
    gpa = gpaE.get()
    subject = subjectE.get()
    school = schoolE.get()
    email = emailE.get()

    if Sgender==1:

    	gender = "Male"
    else:

    	gender = "Female" 

    if name!="":

    	fileName = name.replace(" ", "")
    	file = open("students\\"+fileName+".txt","x")
    	file.write("Name: "+name+"\n\n")
    	file.write("Father Name: "+fatherName+"\n\n")
    	file.write("Mother Name: "+motherName+"\n\n")
    	file.write("Mobile Number: "+mobile+"\n\n")
    	file.write("Permanent Address: "+address+"\n\n")
    	file.write("PostOffice: "+postOffice+"\n\n")
    	file.write("Religion: "+religion+"\n\n")
    	file.write("GPA: "+gpa+"\n\n")
    	file.write("4th Subject: "+subject+"\n\n")
    	file.write("School: "+school+"\n\n")
    	file.write("Email: "+email+"\n\n")

    	# close file
    	file.close()

    	# show successfully message
    	messagebox.showinfo("Done", "Registration Succesfully Done!")
    else:

    	# show warning message
    	messagebox.showwarning("Failed", "Registration not succesfully!\nPlease enter your name") 

    	



# layout margine size
layoutMargine = 25
    


# header text
headar = tk.Label(root, text="Registration Form", font="bold, 24", bg=BG)
headar.pack()

# sub header
headar = tk.Label(root, text="Admission Going on via Online", font="bold, 13", bg=BG)
headar.pack()

# name 
nameL = tk.Label(root, text="Student's Name: ", font="bold, 12", bg=BG)
nameL.place(x=5, y=50+layoutMargine)

nameE = tk.Entry(root, width=30)
nameE.place(x=125, y=50+layoutMargine)

# gender
genderL = tk.Label(root, text="Select Gender: ", font="bold, 10", bg=BG)
genderL.place(x=320, y=50+layoutMargine)

var = tk.IntVar()

maleRB = tk.Radiobutton(root, text="Male", variable=var, value=1, command=Sgender)
maleRB.place(x=430, y=50+layoutMargine)

femaleRB = tk.Radiobutton(root, text="Female", variable=var, value=2, command=Sgender)
femaleRB.place(x=490, y=50+layoutMargine)

# father name 
fatherNameL = tk.Label(root, text="Father's Name: ", font="bold, 12", bg=BG)
fatherNameL.place(x=5, y=100+layoutMargine)

fatherNameE = tk.Entry(root, width=30)
fatherNameE.place(x=125, y=100+layoutMargine)

# mother name 
motherNameL = tk.Label(root, text="Mother's Name: ", font="bold, 12", bg=BG)
motherNameL.place(x=5, y=150+layoutMargine)

motherNameE = tk.Entry(root, width=30)
motherNameE.place(x=125, y=150+layoutMargine)

# mobile
mobileL = tk.Label(root, text="Mobile: ", font="bold, 12", bg=BG)
mobileL.place(x=5, y=200+layoutMargine)

mobileE = tk.Entry(root)
mobileE.place(x=70, y=200+layoutMargine)

# address
addressL = tk.Label(root, text="Permanent Address: ", font="bold, 12", bg=BG)
addressL.place(x=5, y=250+layoutMargine)

addressEL = tk.Label(root)
addressEL.place(x=160, y=250)

addressE = ScrolledText(addressEL, width=30, height=5)
addressE.pack()


# postOffice
postOfficeL = tk.Label(root, text="Post Office: ", font="bold, 12", bg=BG)
postOfficeL.place(x=5, y=350+layoutMargine)

postOfficeE = tk.Entry(root)
postOfficeE.place(x=95, y=350+layoutMargine)

# religion
religionL = tk.Label(root, text="Religion: ", font="bold, 12", bg=BG)
religionL.place(x=5, y=400+layoutMargine)

religionE = tk.Entry(root)
religionE.place(x=75, y=400+layoutMargine)


# gpa
gpaL = tk.Label(root, text="GPA: ", font="bold, 12", bg=BG)
gpaL.place(x=5, y=450+layoutMargine)

gpaE = tk.Entry(root)
gpaE.place(x=60, y=450+layoutMargine) 

# subject
subjectL = tk.Label(root, text="4th subject: ", font="bold, 12", bg=BG)
subjectL.place(x=5, y=500+layoutMargine)

subjectE = tk.Entry(root)
subjectE.place(x=90, y=500+layoutMargine)  

# school
schoolL = tk.Label(root, text="School: ", font="bold, 12", bg=BG)
schoolL.place(x=5, y=550+layoutMargine)

schoolE = tk.Entry(root, width=35)
schoolE.place(x=70, y=550+layoutMargine)

# email
emailL = tk.Label(root, text="Email: ", font="bold, 12", bg=BG)
emailL.place(x=5, y=600+layoutMargine)

emailE = tk.Entry(root, width=35)
emailE.place(x=70, y=600+layoutMargine)  

# registrar button
img = ImageTk.PhotoImage(Image.open("images\\button.png"))

button = tk.Button(root, image=img, height=50, width=200, command=submit)
button.place(x=650, y=550+layoutMargine)

# about image
aboutImg = ImageTk.PhotoImage(Image.open("images\\about.png"))

# show about image
about = tk.Label(root, image=aboutImg)
about.place(x=650, y=0)


root.mainloop()