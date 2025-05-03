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
    with open("data_questions.csv", "r") as file:
        reader = csv.reader(file)
        question_choice = random.choice(list(reader))
        quiz = question_choice[0]
        choice_a = f"A. {question_choice[1]}"
        choice_b = f"B. {question_choice[2]}"
        choice_c = f"C. {question_choice[3]}"
        choice_d = f"D. {question_choice[4]}"
        correct_answer = question_choice[5]
        print(quiz, choice_a, choice_b, choice_c, choice_d)


if __name__ == "__main__":
    main()