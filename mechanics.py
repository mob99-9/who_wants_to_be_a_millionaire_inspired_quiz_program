import random
print("Who Wants to be a Millionaire")
def main():
    user_input = input("A. Start or B. Exit")
    if user_input == "A":
        start()
    elif user_input == "B":
        exit

def start():
    with open("questions.txt") as file:
        questions = file.readline()
        print(questions)



if __name__ == "__main__":
    main()