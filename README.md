# Simple-UIC-Quiz-Game
This is a simple project I made that is just a 4 question quiz about the University of Illinois at Chicago.

# How it's made:
Tech Used: Python, PyCharm

This Python code defines a class named UIC_Quiz_Game that creates a simple, text-based quiz about the University of Illinois Chicago (UIC). The class holds four pre-defined quiz questions, corresponding multiple-choice options, and the correct answers in separate lists. 

When the program runs, it first creates an instance of the class and calls the welcome_to_game method, which prompts the user for their name, age, and profession. It then prints a personalized welcome message. After the introduction, the ask_questions method starts the quiz. It uses random.shuffle to present the four questions in a random order. The program checks the user's input against the correct answer. If the user answers correctly, their score increases and the game continues. However, if they get a question wrong, the game immediately ends and displays their final score. If the user successfully answers all four questions, they are congratulated and a final welcome message is displayed.
