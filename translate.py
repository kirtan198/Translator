from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1= src
    dest1=dest
    trans = Translator()
    trans1 =  trans.translate(text,src=src1,dest=dest1)
    return trans1.text


def data():
    s = comb_source.get()
    d = comb_dest.get()
    msg = source_text.get(1.0,END)
    textget = change(text= msg, src=s, dest=d)
    dest_text.delete(1.0,END)
    dest_text.insert(END,textget)














root = Tk()
root.title("translator")
root.geometry("500x700")
root.config(bg="red")
lab_txt=Label(root,text="translator",font=("Time New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)
frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="SOURCE TEXT",font=("Time New Roman",20,"bold"),fg="black",bg="red")
lab_txt.place(x=100,y=100,height=20,width=300)
source_text= Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
source_text.place(x=10,y=120,height=150,width=480)

List_text = list(LANGUAGES.values())
comb_source = ttk.Combobox(frame,value=List_text)
comb_source.place(x=10,y=300,height=40,width=100)
comb_source.set("english")


button_change = Button(frame,text="translate",relief=RAISED,command=data)
button_change.place(x=120,y=300,height=40,width=100)


comb_dest = ttk.Combobox(frame,value=List_text)
comb_dest.place(x=230,y=300,height=40,width=100)
comb_dest.set("english")


lab_txt=Label(root,text="destination TEXT",font=("Time New Roman",20,"bold"),fg="black",bg="red")
lab_txt.place(x=100,y=360,height=20,width=300)
dest_text= Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_text.place(x=10,y=400,height=150,width=480)










root.mainloop()