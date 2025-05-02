# make a text file 
running = True
file_name = "questions.txt"

# make a function for adding questions and answers to the text file

def add_to_file(user_input):
    with open(file_name, "w") as text_file:
        text_file.write(user_input)

# ask user for a question, 4 possible answer (a, b, c, d) and the right answer (A), infinitely until saying exit

question = []

while running == True:
    user_question = input("Enter a question (type 'exit' to exit): ")
    if user_question == "exit":
        running = False
    else:
        question.append(user_question)

        for letter in range(0,4):
            user_choices = input("Enter a possible answer: ")
            question.append(user_choices)

        user_answer = input("Enter the letter of the right answer: ")
        question.append(user_answer)
        add_to_file(str(question))

# save the text file (It is auto save and auto reset every program run