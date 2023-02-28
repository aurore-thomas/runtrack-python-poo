class Commande:
    def __init__(self, number, list, status):
        self.__number = number
        self.__list = list
        self.__status = status

    def add(self):
        food = input("Entrez le nom du plat : ")
        price = input("Entrez son prix : ")
        self.__list.update({food : [price, "En cours"]})

    def delete(self):
        pass

    def total(self):
        total = 0
        for i in range(0, 1):
            price = self.__list[i][0]
            print(price)
            total += price
        return total
    
    def display(self):
        print(self.__list)
    
c1 = Commande(1, {"Salade" : [15, "En cours"]}, "En cours")
c1.add()
c1.display()
print(c1.total())


