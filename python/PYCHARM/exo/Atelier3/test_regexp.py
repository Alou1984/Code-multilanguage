'''
1. Tester/créer des expressions régulières
a) En se basant sur les slides du cours, écrire un programme qui permet de tester une expression
régulière : 
    1) Elle saisie l’expression, 
    2) Le programme boucle. A chaque tour de boucle, 
        2a) on saisie une chaîne de caractères
        2b) On teste si il y a une correspondance entre la RegExp et la chaine et selon
            on affiche un message adéquat (« il y a correspondance » / « il n’y a pas de correspondance »). 2c) On
            sort du programme (de la boucle) si la chaîne saisie est vide.
b) Utiliser ce programme pour créer/tester une expression qui valide une heure : 10h30 04:30 …
^([01][0-9]|2[0-3])[h:][0-5][0-9]$
'''
# test_regexp.py
# tester une RegExp
import re
#Saisie une expression régulière
regexp = input("RegExp ? ")
#boucler tant que vrai # boucle infinie :-)
while True:
    # -- saisir une chaine
    chaine = input("Une chaine SVP ? ")
    # -- si l’expression régulière est vrai pour la chaine alors
    if re.search( regexp, chaine ):
    # afficher « il y a correspondance »
        print("il y a correspondance")
    else:
    # afficher « PAS de correspondance »
        print("<<<IL N'Y A PAS DE CORRESPONDANCE>>>")
    # -- si la chaine saisie est vide :
    if chaine == "":
    # sortir de la boucle
        break
    #fin de la boucle