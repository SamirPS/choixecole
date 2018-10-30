#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:36:41 2018

@author: samir
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:52:07 2018

@author: samir
"""

"""On importe le fichier modeltest.py en module"""

import modeltest

"""On initialise nos variables"""

Specialite=[]#liste des spécialité
Ecole=[]#Liste des ecoles
Commune=[]
Concours=[]

modeltest.file('choixecole.db')
Concours=modeltest.renvoie_concours()
Commune=modeltest.renvoie_commune()
Specialite=modeltest.renvoie_specialite()

for a in range(len(Specialite)) : #on affiche les spécialite avec un numero pour faciliter l'usage du programme
    print(a+1,Specialite[a])

    
specialiteid=int(input("donne le numero de la spécialite \n"))

while specialiteid>len(Specialite) or specialiteid<1 : #Eviter un bug
    specialiteid=int(input("donne le numero de la spécialite  compris entre 1 et" ,a," \n"))

for b in range(len(Commune)):
    print(Commune[b])


communeid=input("donne le nom de la commune \n")

for c in range(len(Concours)):
    print(Concours[c])


concoursid=input("donne le nom du concours \n")

Note=float(input("Votre Note Test \n"))


Ecole=modeltest.filtre(specialiteid,communeid,concoursid,Note)


if Ecole==[]:# Si la liste a aucun élèment 
    
    print("Pas d'école trouvée en fonction des critéres")

elif concoursid=="Peu importe":
    print("Voila les écoles : \n") #On affiche les écoles contenue dans la liste 
    for d in range(len(Ecole)): 
        print(Ecole[d][0],Ecole[d][1])
else:
    print("Voila les écoles : \n")
    for d in range(len(Ecole)):
        print(Ecole[d][0])
        