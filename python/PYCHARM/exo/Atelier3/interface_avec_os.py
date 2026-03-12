'''
Tâche 1: 
L’interface avec l’OS
1. Écrire un programme qui liste les commandes (les fichiers ordinaires exécutables présents dans les
répertoires faisant partis du PATH).
'''

# lst_cmd_win.py : liste les commandes
import os
import sys
import glob
rep_cmds = []
executables = ["*.exe", "*.cmd", "*.bat", "*.ps1"]
if ( len(sys.argv) > 1 ):
    rep_cmds = sys.argv[1:]
else:
    lepath = os.environ['PATH']
    rep_cmds = lepath.split(os.pathsep) # ";" sous Windows (":" sous Unix)
for rep in rep_cmds:
    print(">>>>>", rep)
    if not (os.path.isdir(rep) and os.access( rep, os.X_OK )):
        print("Le repertoire ", rep, "n'est pas accessible")
        continue
os.chdir(rep)
files = []
for aglob in executables:
    files += glob.glob( aglob )
for file in files:
    if os.path.isfile(file) and os.access( file, os.X_OK ):
        print("\t", file)
sys.exit(0)