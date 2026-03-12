'''
2. Créer un programme en Python qui simule le fonctionnement de la commande « grep » d’Unix. Pour
simplifier l’écriture du programme on ne fait aucun contrôle (par exemple si on a bien fourni le bon
nombre de paramètres, ...)
'''
# grep.py: simule la commande grep Unix
import sys
import re
regexp = sys.argv[1]
fichier= sys.argv[2]
fic = open(fichier)
while True:
    ligne = fic.readline()
    ligne = ligne.rstrip('\n')
    if ligne == "":
        break
    #print(ligne)
    if re.search( regexp, ligne):
        print(ligne)