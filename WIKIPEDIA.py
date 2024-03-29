from tkinter import * 
import wikipedia
root = Tk()
root.geometry('200x200')
root.resizable(0,0)
root.title('WIKIPEDIA')

frame_1 = Frame(root, height=179,width=334)


entered = StringVar()

entry = Entry(frame_1, width=17,font=('calibri',15), textvariable = entered)
entry.grid(row=0)

def search():
    text.delete(1.0, END)
    searched = entered.get()
    try:
        wiki = wikipedia.summary(searched)
        text.insert(INSERT, wiki)

    except:
        text.insert(INSERT, 'Try typing something else or check your internet connection.')


search = Button(frame_1, text='SEARCH',font=('calibri',10), command=search )
search.grid(row=2,padx=10)



frame_2 = Frame(root, height=338,width=262)

scroll = Scrollbar(frame_2)
scroll.pack(side=RIGHT,fill=Y)

text = Text(frame_2,height=8,width=20,yscrollcommand=scroll.set, wrap=WORD)
text.pack()
scroll.configure(command=text.yview)





frame_1.pack(side=TOP)
frame_2.pack()

root.mainloop()
