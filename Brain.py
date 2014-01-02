#Mind.py - Pithon3

#Importations
import sys

class Mind(object):
    def __init__(self):
        """To initiate"""
        self.openfile()
        self.gather()
        self.Directions()
        self.Start()

    def openfile(self):
        """Open the memmory file"""
        file = open("Memmory.txt", "a")
        file.close()

    def Directions(self):
        """Print the directions"""
        print("Hello.  I am a very bad replica of the human brain.")
        print("Give me 10 questions so I can answer them.")
        print("I wil try to answer them as best as I can.\n")

    def Start(self):
        """Starts the questions"""
        print("Please enter the questions one by one.\n")

        for i in range(10):
            print("Enter question #", i + 1, ": ", sep = "", end = "")
            Question = input("")
            if "?" not in Question:
                Question += "?"
            self.evaluate(Question)

    def evaluate(self, Question):
        """Evaluates and answers the quetions"""
        if Question.upper() == "NO!!":
            sys.exit()

        if Question.upper() == "HOW MANY QUESTIONS CAN YOU ANSWER?" or Question.upper() == "COUNT?":
            count1 = 1
            for i in self.Dictionary:
                count1 += 1
            print("The answer is:", count1)

        else:
            try:
                answer = self.Dictionary[Question.upper()]
                print("The answer is:", answer)
            except:
                answer = input("I give up.  What's the answer? ")
                file = open("Memmory.txt", "a+")
                file.write(Question)
                file.write("\n")
                file.write(answer)
                file.write("\n")
                file.close()
                self.gather()

    def gather(self):
        """Updates the self.Dictionary dictionary"""
        self.Dictionary = {}
        file = open("Memmory.txt", "r")
        lines = file.readlines()
        file.close()
        loop = 1
        for line in lines:
            if loop == 1:
                save = line
                loop = 2

            elif loop == 2:
                compare1 = save.upper()
                compare1 = compare1.replace("\n", "")
                self.Dictionary[compare1] = line.replace("\n", "")
                loop = 1


def PowerUp():
    """Starts the application"""
    FakeMind = Mind()

PowerUp()
input("\nHit the enter key to exit.")
