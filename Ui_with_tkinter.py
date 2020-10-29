from tkinter import *
from PIL import ImageTk,Image
from main import recognize
root = Tk()
root.title('Voice control git management system')
root.iconbitmap('icon.ico')

def openSetdirectory():
    root2 = Tk()
    root2.title('Voice control git management system')
    root2.iconbitmap('icon.ico')
    label1 = Label(root2, text='Set Directory:')
    label1.grid(row=1, column=1)
    entry1 = Entry(root2, width=50)
    entry1.grid(row=2, column=1)
    button1 = Button(root2, text='Set')
    button1.grid(row=3, column=1)

def openGithubaccount():
    root3 = Tk()
    root3.title('Voice control git management system')
    root3.iconbitmap('icon.ico')
    label1 = Label(root3, text='Enter your github repo:')
    label1.grid(row=1, column=1)
    entry1 = Entry(root3, width=50)
    entry1.grid(row=2, column=1, columnspan=4)
    button1 = Button(root3, text='Set')
    button1.grid(row=3, column=4)

button1 = Button(root, text="Set Directory", bg="white", fg="blue",command=openSetdirectory)
button1.grid(row=0, column=0)
label1 = Label(root, text='   ')
label1.grid(row=0, column=1, pady=20)

entry1 = Entry(root, width=50)
entry1.grid(row=0, column=2)
label2 = Label(root, text='   ')
label2.grid(row=0, column=3)

button2 = Button(root, text='github account', bg="white", fg="blue",command=openGithubaccount)
button2.grid(row=0, column=4, pady=20)


button4 = Button(root, text='Say something', bg="white", fg="blue", command=lambda: recognize('google',0))
#, command=lambda: recognize('google',0)
button4.grid(row=2, column=2)

mainloop()
