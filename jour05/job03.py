compteur_initial = 0

def function(string, compteur):
    if string == "":
        return compteur
    else:
        compteur += 1
        return function(string[:-1], compteur)

print(function("Hello", compteur_initial))
    