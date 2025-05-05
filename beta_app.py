from tkinter import *
import csv
import random

main_window = Tk()
main_window.geometry("720x480")
main_window.title("Who Wants To Be A Millionaire")

logo = PhotoImage(file='logo.gif')

main_window.iconphoto(True, logo)
main_window.config(background="black")
question = []

def game():
    global quiz, choice_a, choice_b, choice_c, choice_d, correct_answer
    with open("data_questions.csv", "r") as file:
        reader = csv.reader(file)
        question_choice = random.choice(list(reader))
        quiz = question_choice[0]
        choice_a = question_choice[1]
        choice_b = question_choice[2]
        choice_c = question_choice[3]
        choice_d = question_choice[4]
        correct_answer = question_choice[5]

    quiz_label = Label(main_window, text=f"{quiz}",
                   font=("Times New Roman", 25))
    quiz_label.pack()

    letter_a = Button(main_window, text=f"{choice_a}")
    letter_a.place(x=100, y=400)

    letter_b = Button(main_window, text=f"{choice_b}")
    letter_b.place(x=100, y=500)

    letter_c = Button(main_window, text=f"{choice_c}")
    letter_c.place(x=400, y=400)

    letter_d = Button(main_window, text=f"{choice_d}")
    letter_d.place(x=400, y=500)


title = Label(main_window, text="Who Wants To Be A Millionaire", 
              font=("Times New Roman", 40),
              bg="blue")
title.pack()

start_button = Button(main_window, text="Start", command=game)
start_button.place(x=340, y=300)


main_window.mainloop()