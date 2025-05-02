import random

print("Who Wants to be a Millionaire")
def main():
    user_input = input("A. Start or B. Exit: ")
    if user_input == "A":
        game()
    elif user_input == "B":
        exit

def game():
    with open("questions.txt") as file:
        questions = file.readlines()
        question = random.choice(questions)
        print(list(question))


if __name__ == "__main__":
    main()