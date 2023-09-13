from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES


#DRIVER CODE
def change(text,src,dest):                #function to translate the sentence
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():                               #function to retrieve and change the given sentence to a translated one
    s=comb1.get()
    d=comb2.get()                     
    msg=sor_txt.get(1.0,END)
    textget=change(msg,s,d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)




#GUI USING TKINTER
root = Tk()                                 #gui structure
root.title("Translator")
root.geometry("735x500")
root.config(bg='Yellow')

lab_txt=Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg="Cyan")    #Text
lab_txt.place(x=230,y=20,height=50,width=270)

frame=Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text:",font=("Time New Roman",20,"bold"),bg="Yellow",fg="Red")  #creating the first text box
lab_txt.place(x=70,y=88,height=50,width=175)
sor_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=155,height=200,width=325)


lst=list(LANGUAGES.values())                          #combo box 1 to choose languanges
comb1=ttk.Combobox(frame,value=lst)
comb1.place(x=10,y=130,height=25,width=325)
comb1.set("English")

button_change=Button(frame,text="Translate",relief=RAISED,command=data)            # translate button 
button_change.place(x=320,y=375,height=20,width=100)

comb2=ttk.Combobox(frame,value=lst)                     #combo box 1 to choose languanges
comb2.place(x=400,y=130,height=25,width=325)
comb2.set("English")

lab_txt=Label(root,text="Translated Text:",font=("Time New Roman",20,"bold"),bg="Yellow",fg="Red")         # creating second text box that will display the translated sentencee
lab_txt.place(x=440,y=90,height=40,width=250)
dest_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=400,y=155,height=200,width=325)

root.mainloop()