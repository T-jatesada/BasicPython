from tkinter import *
from tkinter import ttk
import pyautogui as pg
import webbrowser

GUI = Tk()
GUI.title('GUI by Jatesada.p')
GUI.geometry('500x300')
GUI.resizable(False, False)
web = 'www.google.com'

def Calendar():
    pg.click(1806,1056)

def Web():
    webbrowser.open(web)

B1 = Button(GUI,text='Calender1', bg="purple", fg="white",command=Calendar)
B1.pack(ipadx = 30, ipady = 10, pady = 15)

B2 = ttk.Button(GUI,text='Calender2',command=Calendar)
B2.pack(ipadx = 30, ipady = 10, pady = 15)

B3 = ttk.Button(GUI,text='Link',command=Web)
B3.pack(ipadx = 30, ipady = 10, pady = 15)

B4 = Button(GUI,text='EXIT', bg="black", fg="white",command=lambda: GUI.quit())
B4.pack(ipadx = 10, ipady = 6)

GUI.mainloop()