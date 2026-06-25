'''
cat passwd
root:x:0:0:root:/root:/bin/bash
albert:x:1009:1010::/home/albert:/bin/bash
lambda:x:1012:1013::/home/lambda:/bin/bash
stage01:x:3001:3001::/home/stage01:/bin/bash
stage02:x:3002:3002::/home/stage02:/bin/bash
mysql:x:27:27:MariaDB Server:/var/lib/mysql:/sbin/nologin
git:x:3003:3003::/home/git:/bin/bash
On affiche les champs Login (le 1er champ), l’UID (le 3ième champ) et le Shell (le 7ième champ).
'''
# 1. ouverture du fichier
f = open("password.txt", "r")
# 2. Boucle de lecture des enregistrements
while True:
    # 2.1. Lecture d'une ligne du fichier
    ligne = f.readline()
    if ligne == "":
        break
    ligne=ligne.strip() # elever les espace de debut de de fin  de chaque ligne 
    #ligne=ligne.rstrip()
    login, password, uid, gid, commentaire, home, shell =ligne.split(":")
        
    # 2.3. Afficher les données
    print("Login: ", login)
    print("UID: ", uid)
    print("Shell: ", shell)
    print("============================")