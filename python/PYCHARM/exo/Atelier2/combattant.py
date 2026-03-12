'''
1. Reprendre l’exemple du cours (le jeu de rôle) et simuler des combats.
(amusant, pas trop long, complexe).
On crée un combattant (représentant le joueur) qui affronte 3 autres combattants (des monstres) à tour
de rôle. A chaque tour le joueur combat chacun des monstres. Ensuite chacun d’eux réplique. Un
combat est représenté par la méthode « combattreContre() » qui combat un adversaire donné en
paramètre. La blessure infligée dépend de la force du combattant multiplié par le résultat d’un lancé de
dé. Les points de vie de l’adversaire sont diminuée de la valeur de la blessure. Si ces derniers
deviennent nul ou inférieur à 0, l’adversaire est hors de combat. On fait plusieurs « rounds » jusqu’à ce
que le joueur gagne ou soit hors de combat.
'''


class Combattant:
    def __init__(self, vie, force, grade  ): # constructeur
        self.vie = vie     # attributs: vie
        self.force = force # attributs: force
        self.grade= grade  # Attributs :  Grade du combattant
        self.blessure= blessure  # Attributs :  nombre de blessures du combattant
    def getVie(self): # méthode 
        return self.vie
    def getForce(self):
        return self.force
    def getGrade (self):
        return self.grade 
    def getBlessure (self):
        return self.blessure     
    def combattreContre(Combattant a, Combattant b):
        de =randint(range (1,100,1))
        a.blessure= de*b.force
        de =randint(range (1,100,1))
        b.blessure= de*a.force
        return (b.blessure, a.blessure)
        
        
joueur1 = Combattant( 10, 2, 1, 0 ) # instanciation, créé joueur1
joueur2 = Combattant( 3, 2, 1, 0 ) # objet = Classe( …)
joueur3 = Combattant( 3, 2, 3 ,0) # objet = Classe( …)
joueur1Bis = joueur1 # crée une nouvelle référence

print ("Presentation de combattants ")
print(" joueur 1:")
print( Combattant.getVie( joueur1 ) ) # Classe.méthode(obj, …)
print( Combattant.getForce( joueur1 ) ) # Classe.méthode(obj, …)
print( Combattant.getGrade( joueur1 ) ) # Classe.méthode(obj, …)
print(" joueur 2:")
print( Combattant.getVie( joueur2 ) ) # Classe.méthode(obj, …)
print( Combattant.getForce( joueur2 ) ) # Classe.méthode(obj, …)
print( Combattant.getGrade( joueur2 ) ) # Classe.méthode(obj, …)
print(" joueur 3:")
print( Combattant.getVie( joueur3 ) ) # Classe.méthode(obj, …)
print( Combattant.getForce( joueur3 ) ) # Classe.méthode(obj, …)
print( Combattant.getGrade( joueur3 ) ) # Classe.méthode(obj, …)

#print( joueur1.getVie() ) # objet.méthode( … ) # notation usuelle

