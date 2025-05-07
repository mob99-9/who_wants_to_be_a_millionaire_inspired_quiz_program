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

def select_answer(user_answer):
    global answer
    answer = ""
    answer = user_answer

def restart_game():
    restart_button.destroy()
    exit_button.destroy()
    submit_button.destroy()
    main_window.config(bg="black")
    game()

def submit():
    global restart_button, exit_button
    if correct_answer == answer:
        quiz_label.destroy()
        letter_a.destroy()
        letter_b.destroy()
        letter_c.destroy()
        letter_d.destroy()
        submit_button.destroy()
        main_window.config(bg="black")
        game()
    else:
        main_window.config(bg="red")
        quiz_label.destroy()
        letter_a.destroy()
        letter_b.destroy()
        letter_c.destroy()
        letter_d.destroy()
        submit_button.destroy()
        restart_button = Button(main_window, text="Restart", command=restart_game)
        restart_button.place(x=340, y=300)
        exit_button = Button(main_window, text="Exit", command=exit)
        exit_button.place(x=340, y=330)

def game():
    start_button.destroy()
    exit_button.destroy()
    global quiz, choice_a, choice_b, choice_c, choice_d, correct_answer, submit_button, quiz_label, letter_a,letter_b,letter_c,letter_d
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

    letter_a = Button(main_window, text=f"{choice_a}", command=lambda: select_answer("A"),
                      activebackground="black")
    letter_a.place(x=100, y=200)

    letter_b = Button(main_window, text=f"{choice_b}", command=lambda: select_answer("B"),
                      activebackground="black")
    letter_b.place(x=100, y=300)

    letter_c = Button(main_window, text=f"{choice_c}", command=lambda: select_answer("C"),
                      activebackground="black")
    letter_c.place(x=500, y=200)

    letter_d = Button(main_window, text=f"{choice_d}", command=lambda: select_answer("D"),
                      activebackground="black")
    letter_d.place(x=500, y=300)

    submit_button = Button(main_window, text="Submit", command=submit)
    submit_button.place(x=340,y=340)

title = Label(main_window, text="Who Wants To Be A Millionaire", 
              font=("Times New Roman", 40),
              bg="blue")
title.pack()

start_button = Button(main_window, text="Start", command=game)
start_button.place(x=340, y=300)

exit_button = Button(main_window, text="Exit", command=exit)
exit_button.place(x=340, y=330)

main_window.mainloop()