from tkinter import *


root3 = Tk()
root3.title('Voice control git management system')
root3.iconbitmap('icon.ico')
def githubAccount():
    label_github_account = Label(root3, text='Enter your github repo:')
    label_github_account.grid(row=1, column=1, padx=10, pady=10)

    entry_github_account = Entry(root3, width=50)
    entry_github_account.grid(row=2, column=1, columnspan=4, ipady=8, padx=20, pady=10)

    button_set_account = Button(root3, text='Set', padx=10, pady=10)
    button_set_account.grid(row=3, column=4, pady=20)




