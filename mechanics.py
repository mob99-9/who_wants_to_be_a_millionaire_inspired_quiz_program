import random
import csv

print("Who Wants to be a Millionaire")
def main():
    user_input = input("A. Start or B. Exit: ")
    if user_input == "A":
        game()
    elif user_input == "B":
        exit

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

if "B" == "B":
    print("true")
else:
    print("false")