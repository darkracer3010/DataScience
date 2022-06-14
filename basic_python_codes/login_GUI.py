import tkinter as tk
m = tk.Tk()
'''
widgets are added here
'''
def submit():
    h=log.get()
    g=pas.get()
    if(h=="vce"):
        if(g=="root"):
            det.insert("end","Correct Credentials")
        else:
            det.insert("end","Incorrect Password")
    else:
        det.insert("end","Invalid Credentials")
    log.set("")
    pas.set("")

m.geometry("500x400")
log=tk.StringVar()
pas=tk.StringVar()
name_label = tk.Label(m, text = 'Username')
login=tk.Entry(m,textvariable=log,bd=5)
pwd_label = tk.Label(m, text = 'Password')
pwd=tk.Entry(m,textvariable=pas,bd=5)
sub_btn=tk.Button(m,text="Submit",command=submit)
det=tk.Text(m,height=5,width=10)
name_label.grid(row=0,column=0)
login.grid(row=0,column=1)
pwd_label.grid(row=1,column=0)
pwd.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
det.grid(row=3,columnspan=3)

m.mainloop()
