import sys
import time
class Quiz:
    def __init__(self,
                 easy_c = None,
                 medium_c = None,
                 hard_c = None,
                 easy_a = None,
                 medium_a = None,
                 hard_a = None,
                 easy_s = 0,
                 medium_s = 0,
                 hard_s = 0
                 ):
        # Initialize quiz categories, answers, scores, and name
        self.easy_s = easy_s
        self.medium_s = medium_s
        self.hard_s = hard_s
        self.easy_c = easy_c  # Easy category questions
        self.medium_c = medium_c  # Medium category questions
        self.hard_c = hard_c  # Hard category questions
        self.easy_a = easy_a  # Easy category answers
        self.medium_a = medium_a  # Medium category answers
        self.hard_a = hard_a  # Hard category answers
        self.easy_c = { # Initialize questions and answers for each category
    1: {
        "question": "What symbol is used for single-line comments in Python?",
        "options": {
            "A": "//",
            "B": "#",
            "C": "--"
        },
        "answer": "B"
    },
    2: {
        "question": "Which of the following is not a valid data type in Python?",
        "options": {
            "A": "float",
            "B": "string",
            "C": "array"
        },
        "answer": "C"
    },
    3: {
        "question": "True or False: Python is a case-sensitive language.",
        "options": {
            "A": "True",
            "B": "False"
        },
        "answer": "A"
    },
    4: {
        "question": "What is the result of the expression `5 + 2 * 3`?",
        "options": {
            "A": "21",
            "B": "11",
            "C": "15"
        },
        "answer": "C"
    },
    5: {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "func",
            "B": "define",
            "C": "def"
        },
        "answer": "C"
    },
    6: {
        "question": "What will be the output of `print('Hello' + 'World')`?",
        "options": {
            "A": "HelloWorld",
            "B": "Hello World",
            "C": "HelloWorld"
        },
        "answer": "A"
    },
    7: {
        "question": "True or False: Lists in Python are mutable.",
        "options": {
            "A": "True",
            "B": "False"
        },
        "answer": "A"
    },
    8: {
        "question": "What is the correct way to write an if statement in Python?",
        "options": {
            "A": "if x = 5:",
            "B": "if x == 5:",
            "C": "if x != 5:"
        },
        "answer": "B"
    },
    9: {
        "question": "Which data structure in Python stores elements in key-value pairs?",
        "options": {
            "A": "List",
            "B": "Tuple",
            "C": "Dictionary"
        },
        "answer": "C"
    },
    10: {
        "question": "What is the output of `print(len('Python'))`?",
        "options": {
            "A": "6",
            "B": "5",
            "C": "7"
        },
        "answer": "A"
    }
}
        self.medium_c = {  # Medium questions and their details
    1: {
        "question": "What is the output of `3 ** 2`?",
        "options": {
            "A": "9",
            "B": "6",
            "C": "27"
        },
        "answer": "A"
    },
    2: {
        "question": "True or False: Python uses indentation to indicate blocks of code.",
        "answer": "True"
    },
    3: {
        "question": "Which method is used to add an item to the end of a list in Python?",
        "options": {
            "A": "append()",
            "B": "add()",
            "C": "insert()"
        },
        "answer": "A"
    },
    4: {
        "question": "What will be the output of `print('Python'[2:4])`?",
        "options": {
            "A": "Py",
            "B": "th",
            "C": "thon"
        },
        "answer": "B"
    },
    5: {
        "question": "What is the result of `5 // 2`?",
        "options": {
            "A": "2",
            "B": "2.5",
            "C": "3"
        },
        "answer": "A"
    },
    6: {
        "question": "True or False: A tuple can be modified after it is created.",
        "options": {
            "A": "True",
            "B": "False"
        },
        "answer": "B"
    },
    7: {
        "question": "Which keyword is used to exit from a loop prematurely in Python?",
        "options": {
            "A": "break",
            "B": "stop",
            "C": "exit"
        },
        "answer": "A"
    },
    8: {
        "question": "What is the correct way to access the value associated with a key in a dictionary?",
        "options": {
            "A": "dict[key]",
            "B": "dict.value(key)",
            "C": "dict[key].value"
        },
        "answer": "A"
    },
    9: {
        "question": "What is the output of `print('Hello, {0}!'.format('Alice'))`?",
        "options": {
            "A": "Hello, Alice!",
            "B": "Hello, {0}!",
            "C": "Hello, !"
        },
        "answer": "A"
    },
    10: {
        "question": "How do you import a module named 'math' in Python?",
        "options": {
            "A": "import math",
            "B": "include math",
            "C": "from math import *"
        },
        "answer": "A"
    }
}
        
        self.hard_c = {  # Hard questions and their details
    1: {
        "question": "What does the '__init__' method do in a Python class?",
        "options": {
            "A": "It initializes the class object.",
            "B": "It defines the constructor of the class.",
            "C": "It is used to delete objects."
        },
        "answer": "B"
    },
    2: {
        "question": "True or False: A lambda function can have multiple expressions.",
        "answer": "False"
    },
    3: {
        "question": "What is the result of `list(range(1, 10, 2))`?",
        "options": {
            "A": "[1, 3, 5, 7, 9]",
            "B": "[2, 4, 6, 8]",
            "C": "[1, 4, 7]"
        },
        "answer": "A"
    },
    4: {
        "question": "How do you raise a custom exception in Python?",
        "options": {
            "A": "raise Exception('Message')",
            "B": "throw Exception('Message')",
            "C": "except Exception('Message')"
        },
        "answer": "A"
    },
    5: {
        "question": "What will be the output of the code `print(3 / 2)` in Python 3?",
        "options": {
            "A": "1",
            "B": "1.5",
            "C": "2"
        },
        "answer": "B"
    },
    6: {
        "question": "True or False: The 'with' statement in Python is used for exception handling.",
        "answer": "True"
    },
    7: {
        "question": "What is the purpose of the `finally` block in a try-except-finally statement?",
        "options": {
            "A": "To handle exceptions",
            "B": "To ensure execution of code whether an exception occurs or not",
            "C": "To define a custom exception class"
        },
        "answer": "B"
    },
    8: {
        "question": "What is the output of `bool('False')`?",
        "options": {
            "A": "True",
            "B": "False"
        },
        "answer": "A"
    },
    9: {
        "question": "Which module in Python provides support for working with dates and times?",
        "options": {
            "A": "time",
            "B": "datetime",
            "C": "calendar"
        },
        "answer": "B"
    },
    10: {
        "question": "What is the correct way to create a virtual environment in Python?",
        "options": {
            "A": "python -m venv myenv",
            "B": "virtualenv myenv",
            "C": "venv myenv"
        },
        "answer": "A"
    }
    
}
        # Extract correct answers from questions
        self.easy_a = [(key, question_info["answer"]) for key, question_info in self.easy_c.items()]
        self.medium_a = [(key, question_info["answer"]) for key, question_info in self.medium_c.items()]
        self.hard_a = [(key, question_info["answer"]) for key, question_info in self.hard_c.items()]
        
    def menu(self):
        # Display the main menu and handle user choices
        print()
        print("Welcome to Quiz Program")
        print("Available Category")
        print("1.Easy")
        print("2.Medium") 
        print("3.Hard")
        print("4.View Score")
        print("5.Reset Record")
        print("6.Exit")
        user = input("Enter your choice! (1-4):") 
        if user == '1':
            self.easy()
        elif user == '2':
            self.medium()
        elif user == '3':
            self.hard()
        elif user == '4':
            self.view_score()
        elif user == '5':
            self.reset()
        elif user == '6':
            sys.exit()
        else:
            print("In((valid Syntax! Try Again!")
            self.menu()      
    def easy(self):
        # Start the easy quiz
        start_time = time.time()  # Get the current time when the quiz starts
        end_time = start_time + 5 * 60  # Calculate the end time (5 minutes later)
        for q_number, question_info in self.easy_c.items():  # Iterate over each question in the easy category
            question = question_info["question"]  # Extract the question from the question_info dictionary
            options = question_info["options"]  # Extract the options for the question
            choices = ", ".join(f"{choice}: {option}" for choice, option in options.items())  # Format options for display
            print(f"Question {q_number}: {question}")  # Print the question number and the question itself
            print(f"Choices: {choices}")  # Print the available choices/options
            print()  # Print an empty line for better readability
            user_answer = input(f"Your answer for question {q_number}: ").strip().upper()  # Get user's answer
            correct_answer = question_info["answer"]  # Get the correct answer from question_info
            if user_answer == correct_answer:  # Check if user's answer is correct
                print("Correct!")  # Print "Correct!" if the answer is correct
                self.easy_s += 1  # Increment the easy score if the answer is correct
                print()  # Print an empty line for better readability
            else:
                print("Incorrect!")  # Print "Incorrect!" if the answer is incorrect
                print()  # Print an empty line for better readability
            if time.time() >= end_time:  # Check if time limit is reached
                print(f"Time's up for Easy quiz!")  # Print a message indicating time's up
                print(f"Your Score in Easy Quiz is {self.easy_s}")  # Print the user's score in the easy quiz
                self.menu()  # Go back to the main menu if time's up

        print(f"Your Score in Easy Quiz is {self.easy_s}")  # Print the user's score in the easy quiz
        self.menu()  # Go back to the main menu after completing the quiz

    def medium(self):
        # Start the medium quiz
        start_time = time.time()  # Get the current time when the quiz starts
        end_time = start_time + 7 * 60  # Calculate the end time (7 minutes later)
        for q_number, question_info in self.medium_c.items():  # Iterate over each question in the medium category
            question = question_info["question"]  # Extract the question from the question_info dictionary
            if 'options' in question_info:  # Check if options are available for the question
                options = question_info['options']  # Extract the options for the question
                choices = ", ".join(f"{choice}: {option}" for choice, option in options.items())  # Format options for display
                print(f"Question {q_number}: {question}")  # Print the question number and the question itself
                print(f"Choices: {choices}")  # Print the available choices/options
            else:
                print(f"Question {q_number}: {question}")  # Print the question number and the question itself

            print()  # Print an empty line for better readability
            user_answer = input(f"Your answer for question {q_number}: ").strip().upper()  # Get user's answer
            correct_answer = question_info["answer"].upper()  # Get the correct answer from question_info (converted to uppercase)
            if user_answer == correct_answer:  # Check if user's answer is correct
                print("Correct!")  # Print "Correct!" if the answer is correct
                self.medium_s += 1  # Increment the medium score if the answer is correct
                print()  # Print an empty line for better readability
            else:
                print("Incorrect!")  # Print "Incorrect!" if the answer is incorrect
                print()

            if time.time() >= end_time:  # Check if time limit is reached
                print(f"Time's up for Medium quiz!")  # Print a message indicating time's up
                print(f"Your Score in Medium Quiz is {self.medium_s}")  # Print the user's score in the medium quiz
                self.menu()  # Go back to the main menu if time's up

        print(f"Your Score in Medium Quiz is {self.medium_s}")  # Print the user's score in the medium quiz
        self.menu()  # Go back to the main menu after completing the quiz

    def hard(self):
        # Start the hard quiz
        start_time = time.time()  # Get the current time when the quiz starts
        end_time = start_time + 10 * 60  # Calculate the end time (10 minutes later)
        for q_number, question_info in self.hard_c.items():  # Iterate over each question in the hard category
            question = question_info["question"]  # Extract the question from the question_info dictionary
            options = question_info.get("options")  # Use .get() to handle cases where 'options' may not exist
            if options:  # Check if options are available for the question
                choices = ", ".join(f"{choice}: {option}" for choice, option in options.items())  # Format options for display
                print(f"Question {q_number}: {question}")  # Print the question number and the question itself
                print(f"Choices: {choices}")  # Print the available choices/options
            else:
                print(f"Question {q_number}: {question}")  # Print the question number and the question itself

            print()  # Print an empty line for better readability
            user_answer = input(f"Your answer for question {q_number}: ").strip().upper()  # Get user's answer
            correct_answer = question_info["answer"].upper()  # Get the correct answer from question_info (converted to uppercase)
            if user_answer == correct_answer:  # Check if user's answer is correct
                print("Correct!")  # Print "Correct!" if the answer is correct
                self.hard_s += 1  # Increment the hard score if the answer is correct
                print()  # Print an empty line for better readability
            else:
                print("Incorrect!")  # Print "Incorrect!" if the answer is incorrect
                print()  # Print an empty line for better readability

            if time.time() >= end_time:  # Check if time limit is reached
                print(f"Time's up for Hard quiz!")  # Print a message indicating time's up
                print(f"Your Score in Hard Quiz is {self.hard_s}")  # Print the user's score in the hard quiz
                self.menu()  # Go back to the main menu if time's up

        print(f"Your Score in Hard Quiz is {self.hard_s}")  # Print the user's score in the hard quiz
        self.menu()  # Go back to the main menu after completing the quiz

    def view_score(self):
        # Display the user's scores
        print()  # Print an empty line for better readability
        print("User Scores:")  # Print a header indicating user scores
        print(f"Easy Category:{self.easy_s}")  # Print the user's score in the easy category
        print(f"Medium Category:{self.medium_s}")  # Print the user's score in the medium category
        print(f"Hard Category:{self.hard_s}")  # Print the user's score in the hard category
        total = self.easy_s + self.medium_s + self.hard_s  # Calculate the total score
        print(f"Your Total Score is {total}.")  # Print the user's total score
        self.menu()  # Go back to the main menu

    def reset(self):
        # Reset the user's scores
        print()  # Print an empty line for better readability
        self.easy_s = 0  # Reset the user's score in the easy category to 0
        self.medium_s = 0  # Reset the user's score in the medium category to 0
        self.hard_s = 0  # Reset the user's score in the hard category to 0
        print("Reseting Record Successful!")  # Print a message indicating successful record reset
        self.menu()  # Go back to the main menu
        print()  # Print an empty line for better readability

# Create an instance of the Quiz class and start the program
quiz = Quiz()
quiz.menu()