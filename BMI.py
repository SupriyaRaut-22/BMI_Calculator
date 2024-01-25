#BMI Calculator Application
from tkinter import *
from tkinter.messagebox import *

#root configuration
root=Tk()
root.title("BMI Calulator by SP")
root.geometry("750x600+100+100")
root.configure(bg="#32cd32")
f=("Cambria",20,"bold")

#the calculation
def calculate():
    con=None
    n=entn.get()
    h=enth.get()
    w=entw.get()
    a=enta.get()
    try:
        if len(n)==0:
            raise Exception("Name cannot be Empty") 
         
        if len(h)==0:
            raise Exception("Height cannot be Empty") 
       
        if h.isspace():
           raise Exception("Height cannot be only spaces")
         
        if h.isalpha():
            raise Exception("Height cannot contain Text")
        
        if len(w)==0:
            raise Exception("Weight cannot be Empty") 
       
        if w.isspace():
           raise Exception("Weight cannot be only spaces")
         
        if w.isalpha():
            raise Exception("Weight cannot contain Text")
        
        if len(a)==0:
            raise Exception("Age cannot be Empty") 
        
        temp=float(h)
        if temp<0:
            raise Exception("Height cannot be negative")

        tem=float(w)
        if tem<0:
            raise Exception("Weight cannot be negative")
        
        age=float(a)
        if age<0 or age>100:
            raise Exception("Enter Valid Age between 0 to 100 ")
    
   
        kg = int(entw.get())
        m = int(enth.get())/100
        bmi = kg/(m*m)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            showinfo('Success', f'BMI = {bmi} is Underweight')
        elif (bmi > 18.5) and (bmi < 24.9):
            showinfo('Success', f'BMI = {bmi} is Normal')
        elif (bmi > 24.9) and (bmi < 29.9):
            showinfo('Success', f'BMI = {bmi} is Overweight')
        elif (bmi > 29.9):
            showinfo('Success', f'BMI = {bmi} is Obesity') 
        else:
            showerror('Issue', 'something went wrong!')   
    except Exception as e:
        showerror('Issue',e)
    finally:
        if con is not None:
            con.close()

def reset():
    entn.delete(0,END)
    enta.delete(0,END)
    enth.delete(0,END)
    entw.delete(0,END)
    entn.focus()


title=Label(root,text="BMI-CALCULATOR",font=("Arial",25,"bold","underline"),background="#32cd32",foreground="black")
title.pack(pady=20)

lab=Label(root,text="Enter your Name:",font=f,background="#32cd32",foreground="black")
entn=Entry(root,font=f)
lab.place(x=50,y=100)
entn.place(x=300,y=100)

lab=Label(root,text="Enter Age:",font=f,background="#32cd32",foreground="black")
enta=Entry(root,font=f)
lab.place(x=130,y=150)
enta.place(x=300,y=150)

#radio button
r=IntVar()
r.set(1)
lab_gender=Label(root,text="Gender:", font=f,background="#32cd32",foreground="black")
rb_1=Radiobutton(root,text="Male",font=f,variable=r,value=1)
rb_2=Radiobutton(root,text="Female",font=f,variable=r,value=2)
lab_gender.place(x=160,y=200)
rb_1.place(x=300,y=200)
rb_2.place(x=500,y=200)

lab=Label(root,text="Enter Height(cm):",font=f,background="#32cd32",foreground="black")
enth=Entry(root,font=f)
lab.place(x=40,y=265)
enth.place(x=300,y=265)

lab=Label(root,text="Enter Weight(kg):",font=f,background="#32cd32",foreground="black")
entw=Entry(root,font=f)
lab.place(x=40,y=320)
entw.place(x=300,y=320)

btn=Button(root,text="Calculate",background="black",foreground="white",font=f,command=calculate)
btn.place(x=385,y=380)

btn=Button(root,text="Reset",background="lightgray",font=f,command=reset)
btn.place(x=410,y=450)


root.mainloop()