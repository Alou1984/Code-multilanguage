'''Tâche 1: Les classes en Python
1. Reprendre l’exemple du cours (le jeu de rôle) et simuler des combats.
(amusant, pas trop long, complexe).
On crée un combattant (représentant le joueur) qui affronte 3 autres combattants (des monstres) à tour
de rôle. A chaque tour le joueur combat chacun des monstres. Ensuite chacun d’eux réplique. Un
combat est représenté par la méthode « combattreContre() » qui combat un adversaire donné en
paramètre. La blessure infligée dépend de la force du combattant multiplié par le résultat d’un lancé de
dé. Les points de vie de l’adversaire sont diminuée de la valeur de la blessure. Si ces derniers
deviennent nul ou inférieur à 0, l’adversaire est hors de combat. On fait plusieurs « rounds » jusqu’à ce
que le joueur gagne ou soit hors de combat.
Tâche 2: Compléments (L’héritage, ...)
1. Faire fonctionner les exemples du cours
2. Créer un programme qui additionne des monnaies. (facile, rapide)
On additionne des monnaies de l’ancien temps (livres, sous, deniers). La méthode d’addition pourra
être remplacée par l’opérateur « + ». Une livre égale 20 sous et 1 sol égal à 12 deniers.'''

class Monnaie:
    def __init__(self, liv, sou, den ):
        self.liv = liv
        self.sou = sou
        self.den = den
    def __add__(self, autre):
        x = Monnaie(0,0,0)
        les_den = self.den + autre.den
        x.den = les_den % 12
        les_sou = self.sou + autre.sou + les_den // 12
        x.sou = les_sou % 20
        x.liv = self.liv + autre.liv + les_sou // 20
        return x
    def __str__(self):
        return f"<{self.liv} livres, " + f"{self.sou} sous, {self.den} deniers>" # f" methode d'introspection  qui vient du rubby
x1 = Monnaie(3,15,4)
x2 = Monnaie(2,10,11)
x3 = x1 + x2 # x3 = x1.__add__(x2)
print(x3.liv, x3.den, x3.sou)
print("x1 = ", x1) # ou print("x1 = ", str(x1) )
print("x2 = ", x2)
print("x3 = ", x3)