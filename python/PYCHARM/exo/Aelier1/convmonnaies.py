# convmonnaies.py : convertit une somme exprimee en euros en dollars, livre, yen

euros2dollars = 1.0723
euros2livres  = 0.9020
euros2yens    = 118.7672 

saisie  = input("Une somme en euros ? ")
euros = float( saisie )

print("Euros -> Dollars  :", euros * euros2dollars)
print("Euros -> Livres   :", euros * euros2livres)
print("EUros -> Yens     :", euros * euros2yens)


