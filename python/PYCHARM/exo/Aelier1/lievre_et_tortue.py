'''Le lièvre et la tortue (facile, amusant)
On joue au dé. A chaque coup, si le 6 sort, le lièvre a gagné, autrement la tortue avance d’autant de case
que la valeur du dé. Si au bout de 2 à plusieurs coups, la tortue arrive (ou dépasse) sur la 6ième case,
elle gagne. Simuler par un programme ce jeu.'''
import random
total= 0
while True:
    de=random.randint(1,6)
    print("Valeur du lance: ", de )
    if de == 6 :
        print("Le lievre a gagne")
    break
    total = total + de
    if total >= 6:
        print("La tortue a gagne")
    break