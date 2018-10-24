#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:52:07 2018

@author: samir
"""

"""On importe le fichier model.py en module"""

import model

"""On initialise nos variables"""

Specialite=[]#liste des spécialité
Ecole=[]#Liste des ecoles

"""Renvoie les specialites contenues dans la base de données"""

Specialite=model.renvoie_specialite()

"""Affiches les specialités"""

for i in range(len(Specialite)) : #on affiche les spécialite avec un numero pour faciliter l'usage du programme
    print(i+1,Specialite[i])

"""L'utilisateur choisi sa specialité"""  
specialiteid=int(input("donne le numero de la spécialite \n"))

"""Afin d'éviter un bug avec le nombre d'items dans la liste"""


while specialiteid>len(Specialite) or specialiteid<1 : #Eviter un bug
    specialiteid=int(input("donne le numero de la spécialite  compris entre 1 et 4 \n"))

"""Renvoie les écoles en fonction de la specialité choisie"""  
Ecole=model.filtre(specialiteid)

if len(Ecole)==0:# Si la liste a aucun élèment 
    
    print("Pas d'école trouvée en fonction des critéres")

else:
    print("Voila les écoles : \n") #On affiche les écoles contenue dans la liste 
    for i in range(len(Ecole)): 
        print(Ecole[i])
