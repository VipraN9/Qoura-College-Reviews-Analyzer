from tkinter import *

master = Tk()
master.title("Sentiment-Analysis for College Reviews")
master.geometry('800x800')

master.configure(bg='#81C6E8') 

l=Label(master,text='Choose the college below',bg='#81C6E8',font=("Times New Roman bold",25))
l.pack()
l.place(relx=0.5,rely=0.2,anchor='center')

options=[
    "IIIT Nagpur",
    "IIT Delhi",
    "IIT Madras",
    "BITS Pilani"
]

clicked=StringVar()
d=OptionMenu(master,clicked,*options)
d.pack()
d.place(relx=0.5,rely=0.3,anchor='center')

def main():
    input = clicked.get()
    






btn = Button(master,text="Process..",command=main)
btn.pack()
btn.place(relx=0.5,rely=0.6,anchor='center')
mainloop()