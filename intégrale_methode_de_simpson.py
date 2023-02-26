# Importation de la bibliothèque mathématique
import math

# Fonction à intégrer
def f(x):
    return math.sin(x)

# Demander à l'utilisateur de saisir les bornes d'intégration et le nombre de segments
a = float(input("Entrez la borne inférieure : "))
b = float(input("Entrez la borne supérieure : "))
n = int(input("Entrez le nombre de segments : "))

# Calcul de la largeur de chaque segment
h = (b-a)/n

# Initialisation de la somme
somme = 0

# Calcul de la somme des aires des segments
for i in range(0, n):
    x1 = a + i*h
    x2 = x1 + h
    somme += f(x1) + 4*f((x1 + x2)/2) + f(x2)

# Calcul de l'intégrale
integrale = h*somme/6

# Affichage du résultat
print("L'intégrale de la fonction entre", a, "et", b, "est", integrale)
