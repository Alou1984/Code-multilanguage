class Combattant:
    def __init__(self, nom, vie, force ):
        self.nom = nom
        self.vie = vie
        self.force = force
    def getAttributs(self):
        return ( self.nom, self.vie, self.force )
    def blesser(self, ptvie ):
        self.vie = self.vie - ptvie
    def getEnVie(self):
        if self.vie > 0:
            return True # en Vie
        else:
            return False # mort
    def combattreContre(self, adversaire ):
        if self.vie < 0:
            return
        de = randint(1,6)
print("Blessure: ", de, self.force, de * self.force)
adversaire.blesser( de * self.force )
joueur = Combattant( "Prince", 15, 3 )
nom, ptvie, ptforce = joueur.getAttributs()
print("Nom du joueur : ", nom)
print("Points de vie : ", ptvie)
© JF Bouchaudy – Python - Module 2: - Programmation objet p 1
print("Points de force: ", ptforce)
lesMonstres = {
"Alien":Combattant( "Alien", 10, 2),
"Predator":Combattant( "Predator", 12, 3 ),
"Bamby":Combattant( "Bamby", 12,1 )
} tour =
0
for nom in list(lesMonstres.keys()):
    joueur.combattreContre( lesMonstres[nom] )
    print("Le monstre ", nom)
    lesMonstres[nom].combattreContre( joueur )
if not joueur.getEnVie() :
    print("AAAAAAAAARGH") ; exit(1)
nom, ptvie, ptforce = joueur.getAttributs() ; tour = tour + 1
print("====> apres le %d tour:" % (tour+1))
print("Points de vie : ", ptvie)
print("Points de force: ", ptforce)
print(">>>>>>>>> Je peux delivrer la princesse !!!")