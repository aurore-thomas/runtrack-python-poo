class Animal:
    def __init__(self):
        self.age = 0
        self.name = ""
    
    def vieillir(self):
        self.age += 1
        return self.age

    def nommer(self, name):
        self.name = name
        return self.name

print("L'age de l'animal est ", Animal().age, "ans.")
print("L'age de l'animal est ", Animal().vieillir(), "ans.")
print("L'animal se nomme ", Animal().nommer("Luna"))