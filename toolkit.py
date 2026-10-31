import random

# Number Guessing Game: the user guesses a secret number from 1-10
def guessing_game():
    secret = random.randint(1, 10)
    attempts = 0
    print("I'm thinking of a number between 1 and 10.")

    while True:
        guess = input("Your guess: ")
        if not guess.isdigit():
            print("Please enter a whole number.")
            continue
        guess = int(guess)
        attempts += 1
        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"You got it in {attempts} attempts!")
            break

# To-Do List: lets the user add, view, and remove tasks
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Back to main menu")
        option = input("Choose an option: ")

        if option == "1":
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Added: {task}")
        elif option == "2":
            if len(tasks) == 0:
                print("Your list is empty.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        elif option == "3":
            if len(tasks) == 0:
                print("Nothing to remove.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                number = input("Number to remove: ")
                if number.isdigit() and 1 <= int(number) <= len(tasks):
                    removed = tasks.pop(int(number) - 1)
                    print(f"Removed: {removed}")
                else:
                    print("That's not a valid task number.")
        elif option == "4":
            break
        else:
            print("Sorry, please choose 1, 2, 3, or 4.")

# Simple Calculator: does basic math on two numbers
def calculator():
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    op = input("Operation (+, -, *, /): ")

    if op == "+":
        print(f"{a} + {b} = {a + b}")
    elif op == "-":
        print(f"{a} - {b} = {a - b}")
    elif op == "*":
        print(f"{a} * {b} = {a * b}")
    elif op == "/":
        if b == 0:
            print("Sorry, you can't divide by zero.")
        else:
            print(f"{a} / {b} = {a / b}")
    else:
        print("Sorry, that's not a valid operation.")

        

            

        
print("Welcome to your Personal Mini-Toolkit!")

while True:
    print("\n=== Personal Mini-Toolkit ===")
    print("1. Number Guessing Game")
    print("2. To-Do List")
    print("3. Simple Calculator")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        guessing_game()
    elif choice == "2":
        todo_list()
    elif choice == "3":
        calculator()
    elif choice == "4":
        print("Goodbye! Thanks for using the toolkit.")
        break
    else:
        print("Sorry, that's not a valid choice. Please enter 1, 2, 3, or 4.")






        










