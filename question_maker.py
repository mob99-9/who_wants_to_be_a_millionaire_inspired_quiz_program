import csv

file_name = "data_questions.csv"

def add_to_file(user_inputs):
    with open(file_name, "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(user_inputs)

question = []

def question_maker():
    question_set = []
    while True:
        user_question = input("Please enter a question (type exit if none): ")
        if user_question.lower() == "exit":
            exit()
        else:
            question_set.append(user_question)
            for choice in range(0,4):
                user_choice = input(f"Please enter choice no. {choice + 1}: ")
                question_set.append(user_choice)
            user_answer = input("Please enter the corret answer (A, B, C, D): ")
            question_set.append(user_answer)
            question.append(question_set)
            add_to_file(question)

if __name__ == '__main__':
    question_maker()