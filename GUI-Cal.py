from tkinter import *
from tkinter import ttk, messagebox

def Cal():
    try:
        quan = float(v_quan.get())
        calc =  quan * 10
        messagebox.showinfo('ราคารวม','{} บาท'.format(calc))
        v_quan.set('')
    except:
        messagebox.showwarning('กรอกผิด')
        v_quan.set('')

def Cal2():
    try:
        quan = float(v_quan.get())
        calc2 =  quan * 10 * 0.75
        dc =   quan * 10 * 0.25
        messagebox.showinfo('ราคาสมาชิก','{} บาท [ ถูกลง {} บาท ]'.format(calc2,dc))
        v_quan.set('')
    except:
        messagebox.showwarning('กรอกผิด')
        v_quan.set('')

GUI = Tk()
GUI.title('โปรแกรมคำนวณราคา')
GUI.geometry('700x500')

bg = PhotoImage(file = 'car1.png')
BG = Label(GUI,image=bg)
BG.pack()

L = Label(GUI,text = 'ร้านทุกอย่าง 10 บาท กรุณากรอกจำนวนสินค้า',font=(None,16))
L.pack()

v_quan = StringVar() #เก็บข้อความ
E1 = ttk.Entry(GUI, textvariable=v_quan, font=(None,20))
E1.pack()

B = ttk.Button(GUI, text='คำนวณราคา', command=Cal)
B.pack(ipadx=40, ipady=20)

B2 = ttk.Button(GUI, text='ราคาสมาชิก', command=Cal2)
B2.pack(ipadx=40, ipady=20)

GUI.mainloop()
