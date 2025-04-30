# make a text file with questions and possible answers from the user

# make a text file 
running = True
file_name = "questions.txt"

# make a function for adding questions and answers to the text file

def add_to_file(user_input):
    with open(file_name, "a") as text_file:
        text_file.write(f"{user_input}")

# ask user for a question, 4 possible answer (a, b, c, d) and the right answer (A), infinitely until saying exit

choices = ["a", "b", "c", "d"]

while running == True:
    user_question = input("Enter a question (type 'exit' to exit): ")
    if user_question == "exit":
        running = False
    else:
        add_to_file(f'\n{user_question.capitalize()} ')

        for letter in choices:
            user_choices = input(f"{letter}. Enter a possible answer: ")
            add_to_file(f"{letter}. {user_choices} ")

        user_answer = input("Enter the letter of the right answer: ")
        add_to_file(f"Answer: {user_answer.capitalize()}")

# save the text file (It is auto save and auto reset every program run)