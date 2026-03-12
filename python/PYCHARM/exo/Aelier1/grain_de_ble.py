'''Calculer le nombre de grains de blés sur chaque case de l’échiquier. (facile)
[ALGORITHME donné à la fin du document]
Sur la première case: 1 grains de blé, sur la 2ième: 2 grains, sur la 3ième: 4 grains (on double à chaque
fois), …. sur la case 64: ….'''
grains = 1 ; case = 1
while case <= 64:
    print("%2d %20d" % (case, grains) )
    case += 1
    grains *= 2