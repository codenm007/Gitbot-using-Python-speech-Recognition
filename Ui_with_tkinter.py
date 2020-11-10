from tkinter import *
from PIL import ImageTk,Image
from main import recognize
from tkinter import messagebox
from tkinter import filedialog

#choose directory
import os

root = Tk()
root.title('Voice control git management system')
root.iconbitmap('icon.ico')
#root.geometry("790x800+380+50")

real_github_account = '';
folder_path = ''
def setDirectory():
    global folder_path
    folder_path = filedialog.askdirectory()

def openGithubaccount():
    global microphone
    root3 = Toplevel()
    root3.title('Voice control git management system')
    root3.iconbitmap('icon.ico')

    microphone = ImageTk.PhotoImage(Image.open("icons8-account-100.png"))
    label_open_github_account = Label(root3, image=microphone)
    label_open_github_account.grid(row=1, column=1)

    label_github_account = Label(root3, text='Enter your github repo:')
    label_github_account.grid(row=2, column=1, padx=10, pady=10)

    entry_github_account = Entry(root3, width=50)
    entry_github_account.grid(row=3, column=1, columnspan=4, ipady=8, padx=20, pady=10)

    def get_account():
        global label_entry
        global real_github_account
        global entry_set_account
        repo= entry_github_account.get()
        if(repo == ''):
            messagebox.showinfo("warning!","Please enter your github account !")
            root3.destroy()
        else:
            real_github_account  = repo
            entry_set_account.insert(0,repo)
            root3.destroy()
            os.system('git init')
            os.system('git remote add origin ' + real_github_account)
            print(real_github_account)

    button_set_account = Button(root3, text='Set', padx=10, pady=10, command=get_account)
    button_set_account.grid(row=4, column=4, pady=20)



modeValue = 1
sexType = 1

def saySomething():
    global modeValue
    global sexType
    global folder_path
    if(folder_path == ''):
        setDirectory()
    else:
        os.chdir(folder_path)
    if(modeValue == 1):
        recognize('google', sexType)
    else:
        recognize('offline', sexType)


def setAccount():
    # git_account = lambda
    openGithubaccount()


label0 = Label(root, text='   ')
label0.grid(row=0, column=0)
# label1 = Label(root, text='   ')
# label1.grid(row=0, column=1, pady=20)

directory_image = ImageTk.PhotoImage(Image.open("directory.png"))
button_set_directory = Button(root, image=directory_image,padx=3, pady=3, command= setDirectory)
button_set_directory.grid(row=0, column=1)


entry_set_account = Entry(root, width=50)
entry_set_account.grid(row=0, column=2, ipady=8)
entry_set_account.insert(0,real_github_account)

# label2 = Label(root, text='   ')
# label2.grid(row=0, column=3)

button_github_account = Button(root, text='github account', bg="white", fg="blue",  padx=10, pady=10,command=setAccount)
button_github_account.grid(row=0, column=4, padx=10,pady=20)

image = PhotoImage(file="github-main-image.png")
label_image_github = Label(root, image=image)
label_image_github.grid(row=2, column=2)

microphone_image_mute = PhotoImage(file="microphone.png")
label_microphone = Button(root, image=microphone_image_mute, command=saySomething)
label_microphone.grid(row=3, column=2, pady=10)

label_mode1 = Label(root, text="Select mode")
label_mode1.grid(row=4, column=1)

label_mode2 = Label(root, text="Select voice")
label_mode2.grid(row=4, column=3)

m = IntVar()
m.set(1)
def chooseMode(value):
    global modeValue
    if(value == 1):
        modeValue = 1
    else:
        modeValue = 0


choose_mode1 = Radiobutton(root, text="online", variable=m, value=1, command= lambda: chooseMode(m.get()))
choose_mode1.grid(row=5, column=1)

choose_mode2 = Radiobutton(root, text="offline", variable=m, value=0, command= lambda: chooseMode(m.get()))
choose_mode2.grid(row=6, column=1)

s = IntVar()
s.set(1)
def chooseSex(value):
    global sexType
    if(value == 1):
        sexType = 1
    elif(value == 0):
        sexType = 0


choose_voice2 = Radiobutton(root, text="Male", variable=s, value=0, command= lambda: chooseSex(s.get()))
choose_voice2.grid(row=6, column=3)

choose_voice1 = Radiobutton(root, text="Female", variable=s, value=1, command= lambda: chooseSex(s.get()))
choose_voice1.grid(row=5, column=3)




mainloop()
