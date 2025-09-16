import random
# using shuffle function from random

class UIC_Quiz_Game:
    question = ["What is UIC's oldest college?", "What are UIC's school colors?", "What is UIC's team name?",
                "Where was UIC's original campus?"] # i can add a couple more questions if needed
    multChoice = [
        "\n1.) College of Engineering \n2.) College of Education \n3.) College of Pharmacy \n4.) College of Dentistry",
        "\n1.) Red and Blue \n2.) Red and White \n3.) Orange and Blue \n4.) Blue and White",
        "\n1.) Illini \n2.) Flames \n3.) Prairie Stars \n4.) Ramblers",
        "\n1.) Bolingbrook \n2.) Hyde Park \n3.) Brookfield \n4.) Navy Pier"]
    answer = [3, 1, 2, 4] # the questions and answers will line up since they all have the same index

    def __init__(self, _name, _age, _profession): # declares name, age, and profession as variables to answer as soon as the code is started
        self.name = _name
        self.age = _age
        self.profession = _profession

    def welcome_to_game(self): # simple input questions about yourself and introduces you to the quiz
        print("Welcome to a simple quiz about UIC!")
        self.name = input("What is your name?: ")
        self.age = input("What is your age?: ")
        self.profession = input("What is your profession?: ")
        print(f"\nWelcome to UIC, {self.name}. As a(n) {self.age} year old, you may be able to solve this quiz! Maybe your profession as a(n) {self.profession} may help you.")

    def ask_questions(self): # utilizes the random.shuffle function to give the questions in a random order. displays the number of questions that you get correct and kicks you out if you don't solve all of them
        numberOfQuestions = [1, 2, 3, 4]
        random.shuffle(numberOfQuestions)
        status = True
        questionsCorrect = 0

        while status and questionsCorrect != 4:
            for i in range(len(numberOfQuestions)):
                print(f"\n{UIC_Quiz_Game.question[numberOfQuestions[i]-1]}")
                print(f"\n{UIC_Quiz_Game.multChoice[numberOfQuestions[i]-1]}")
                yourAnswer = int(input("\nWhat is your answer? (Select 1-4): "))
                if yourAnswer == UIC_Quiz_Game.answer[numberOfQuestions[i]-1]:
                    print("\nYou got it right!")
                    status = True
                    questionsCorrect += 1
                else:
                    input(f"\nYou got it wrong! Thanks for playing. You got {questionsCorrect} out of 4 questions.")
                    status = False
                    break

        if questionsCorrect == 4:
            input(f"\nThank you {self.name} for playing! You passed the quiz. Welcome to UIC!")

name = "Name"
age = "Age"
profession = "Profession"
game = UIC_Quiz_Game(name, age, profession)
game.welcome_to_game()
game.ask_questions()