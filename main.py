from tkinter import *
import smtplib
import re

def login():
    if validate_login():
        global username
        global password
        username = str(entry1.get())
        password=str(entry2.get())
        global server
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        f2.pack()
        btn2.grid()
        label3['text']="Logged In!"
        root.after(10,root.grid)
        f1.pack_forget()
        root.after(10,root.grid)
        f3.pack()
        label8.grid_remove()
        root.after(10, root.grid)

def hide_login_label():
    f2.pack_forget()
    f3.pack_forget()
    root.after(10,root.grid)

def send_mail():
    if validate_message():
        label8.grid_remove()
        root.after(10,root.grid)
        receiver = str(entry3.get())
        subject= str(entry4.get())
        msgbody= str(entry5.get())
        msg= "From: "+ username +"\n" + "To: "+ receiver + "\n" + "Subject: "+ subject + "\n" + msgbody
        try:
            server.sendmail(username,receiver,msg)
            label8.grid()
            label8['text'] = "Mail Sent!"
            root.after(10,label8.grid)
        except Exception as e:
            label8.grid()
            label8['text']= "Error in Sending Your Email"
            root.after(10, label8.grid)

def logout():
    try:
        server.quit()
        f3.pack_forget()
        f2.pack()
        label3.grid()
        label3['text']= "Logged Out Successfully.."
        btn2.grid_remove()
        f1.pack()
        entry2.delete(0, END)
        root.after(10, root.grid)
    except Exception as e:
        label3['text'] = "Error in Logout"

def validate_login():
    email_text=str(entry1.get())
    pass_text=str(entry2.get())
    if(email_text == "") or (pass_text == ""):
        f2.pack()
        label3.grid()
        label3['text']= "Fill all the Fields"
        btn2.grid_remove()
        root.after(10,root.grid)
        return False
    else:
        EMAIL_REGX=re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
        if not EMAIL_REGX.match(email_text):
            f2.pack()
            label3.grid()
            label3['text'] = "Enter valid Email address"
            btn2.grid_remove()
            root.after(10, root.grid)
            return False
        else:
            return True

def validate_message():
    email_text = str(entry3.get())
    sub_text = str(entry4.get())
    msg_text = str(entry5.get())

    if (email_text == "") or (sub_text == "") or (msg_text == ""):
        label8.grid()
        label8['text']= "Fill in all the Places"
        root.after(10,root.grid)
        return False
    else:
        EMAIL_REGX = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
        if not EMAIL_REGX.match(email_text):
            label8.grid()
            label8['text'] = "Enter a Valid Email Address"
            root.after(10, root.grid)
            return False
        elif(len(sub_text)<3) or (len(msg_text)<3):
            label8.grid()
            label8['text'] = "Enter atleast 3 Characters"
            root.after(10, root.grid)
            return False
        else:
            return True

root=Tk()
root.title('Email Application')

f1=Frame(root,height=10000, width=10000)
f1.pack(side=TOP)

label=Label(f1,width=40,height=2,text="Enter your Credential",font=("Calibri 18 bold"))
label.grid(row=0, columnspan=3, pady=10,padx=10)

label1= Label(f1,text="Email").grid(row=1, sticky=E,pady=5,padx=10)
label2= Label(f1,text="Password").grid(row=2, sticky=E,pady=5,padx=10)

entry1=Entry(f1)
entry2=Entry(f1, show="*")

entry1.grid(row=1,column=1,pady=5)
entry2.grid(row=2, column=1)

btn1=Button(f1,text="Login", width=10,bg="black", fg="white", command= lambda: login())
btn1.grid(row=3, columnspan=3, pady=10)
#root.mainloop()

f2=Frame(root)
f2.pack(side=TOP,expand=NO, fill=NONE)

label3= Label(f2, width=20, bg="cyan", fg="red", text="LOGIN SUCCESS!!!", font=("calibri 12 bold"))
label3.grid(row=0, column=0, columnspan=2, pady=5)

btn2= Button(f2, text="LOGOUT", bg="black", fg="white", command= lambda : logout())
btn2.grid(row=0, column=4, sticky=E, pady=10, padx=(5,0))

f3= Frame(root)
f3.pack(side=TOP, expand=NO, fill=NONE)
label4=Label(f3, width=20, text="Compose Email", font=("Calibri 18 bold"))
label4.grid(row=0, columnspan=3, pady=10)

label5= Label(f3, text="TO").grid(row=1, sticky=E, pady=5)
label6= Label(f3, text="Subject").grid(row=2, sticky=E)
label7= Label(f3, text="Message").grid(row=3, sticky=E)

entry3= Entry(f3)
entry4= Entry(f3)
entry5= Entry(f3)

entry3.grid(row=1, column=1, pady=5)
entry4.grid(row=2, column=1, pady=5)
entry5.grid(row=3, column=1, pady=5, rowspan=3, ipady=10)

btn3= Button(f3, text="Send Mail", width=10, bg="black", fg="white", command= lambda : send_mail())
btn3.grid(row=6, columnspan=3, pady=10)

label8= Label(f3, width=20, fg="white", bg="black", font=("Calibri 18 bold"))
label8.grid(row=7, columnspan=3, pady=5)

hide_login_label()

root.mainloop()

