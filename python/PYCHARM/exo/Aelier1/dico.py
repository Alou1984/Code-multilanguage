dico = { 'un':'ONE', 'deux':'TWO' }
print( dico['deux'] ) # TWO
print( dico ) # {'un': 'ONE', 'deux': 'TWO'}
del dico['deux']
dico['trois'] = 'THREE'
for x in sorted( dico.keys() ):
    print( x, dico[x] )
    if 'un' in dico : print(" la clé un est dans le dico") # vrai
for cle,valeur in dico.items():
     print( cle, valeur )