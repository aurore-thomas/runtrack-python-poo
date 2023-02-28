class Student:
    def __init__(self, name, firstame, number):
        self.__name = name
        self.__firstname = firstame
        self.__number = number
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()
        else:
            print("Error")

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits < 90 and self.__credits >= 80:
            return "Très Bien"
        elif self.__credits < 80 and self.__credits >= 70:
            return "Bien"
        elif self.__credits < 70 and self.__credits >= 60:
            return "Passable"
        elif self.__credits < 60:
            return "Insuffisant"

    def studentInfo(self):
        print("Nom = ", self.__name)
        print("Prénom = ", self.__firstname)
        print("ID = ", self.__number)
        print("Niveau = ", self.__level)


    def display(self):
        print("The student ", self.__firstname, self.__name, "has", self.__credits, "credits.")

p1 = Student("Doe", "John", 145)
p1.display()

p1.add_credits(30)
p1.add_credits(30)
p1.add_credits(15)
p1.display()

p1.studentInfo()