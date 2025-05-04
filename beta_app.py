from tkinter import *

main_window = Tk()
main_window.geometry("720x480")
main_window.title("Who Wants To Be A Millionaire")

logo = PhotoImage(file='logo.gif')

main_window.iconphoto(True, logo)
main_window.config(background="black")

main_window.mainloop()