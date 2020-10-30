from tkinter import *
from PIL import ImageTk,Image
from main import recognize

import os

root = Tk()
root.title('Voice control git management system')
root.iconbitmap('icon.ico')
root.geometry("790x700+380+50")


def openSetdirectory():
    root2 = Tk()
    root2.title('Voice control git management system')
    root2.iconbitmap('icon.ico')
    label_set_directory = Label(root2, text='Set Directory:', padx=10, pady=10)
    label_set_directory.grid(row=1, column=1)
    entry_set_directory = Entry(root2, width=50)
    entry_set_directory.grid(row=2, column=1, ipady=8, padx=10,  pady=10)
    button_set = Button(root2, text='Set', padx=10, pady=10)
    button_set.grid(row=3, column=1)



def openGithubaccount():
    global microphone
    root3 = Toplevel()
    root3.title('Voice control git management system')
    root3.iconbitmap('icon.ico')

    label_github_account = Label(root3, text='Enter your github repo:')
    label_github_account.grid(row=1, column=1, padx=10, pady=10)

    entry_github_account = Entry(root3, width=50)
    entry_github_account.grid(row=2, column=1, columnspan=4, ipady=8, padx=20, pady=10)

    def get_account():
        global label_entry
        label_entrty = Label(root3, text=entry_github_account.get())
        label_entrty.grid(row=4,column=1)
        satyam = entry_github_account.get()
        return satyam

    button_set_account = Button(root3, text='Set', padx=10, pady=10, command=get_account)
    button_set_account.grid(row=3, column=4, pady=20)

    microphone = ImageTk.PhotoImage(Image.open("account_image.png"))
    label_open_github_account = Label(root3, image=microphone)
    label_open_github_account.grid(row=3, column=1)

def saySomething():
    microphone_image = PhotoImage(file="microphone-mute.png")
    label_microphone = Button(root, image=microphone_image, command=saySomething)
    label_microphone.grid(row=2, column=2)

    print(recognize('google',1))

def setAccount():
    # git_account = lambda
    print('hi')

button_set_directory = Button(root, text="Set Directory", bg="white", fg="blue",  padx=10, pady=10,command=openSetdirectory)
button_set_directory.grid(row=0, column=0, padx=10, pady=20)
label1 = Label(root, text='   ')
label1.grid(row=0, column=1, pady=20)

entry_set_account = Entry(root, width=50)
entry_set_account.grid(row=0, column=2, ipady=8)
label2 = Label(root, text='   ')
label2.grid(row=0, column=3)

button_github_account = Button(root, text='github account', bg="white", fg="blue",  padx=10, pady=10,command=setAccount)
button_github_account.grid(row=0, column=4, padx=10,pady=20)

image = PhotoImage(file="github-main-image.png")
label_image_github = Label(root, image=image)
label_image_github.grid(row=2, column=2)

microphone_image_mute = PhotoImage(file="microphone.png")
label_microphone = Button(root, image=microphone_image_mute, command=saySomething)
label_microphone.grid(row=3, column=2, pady=10)

clicked = StringVar()
clicked.set("online")
drop = OptionMenu(root, clicked, "online","offline")
drop.grid(row=3, column=3)



mainloop()
