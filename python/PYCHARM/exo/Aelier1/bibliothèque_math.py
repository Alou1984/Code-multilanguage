'''Les fonctions, les modules
1. Écrire un programme qui, grâce à la bibliothèque math, calcule les cosinus, sinus et tangente d’un
angle. L’angle est saisie en degrés. On écrit une fonction de conversion de degrés en radian.

'''
import math
import 

angle_deg = float( input("angle en degres ? ") )
angle_rd = deg2rd( angle_deg )
print("Cosinus : %5.2f" % (cos( angle_rd )) )
print("Sinus : %5.2f" % (sin( angle_rd )) )
print("Tangente: %5.2f" % (tan( angle_rd )) )