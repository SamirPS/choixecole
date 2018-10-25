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

Concours=[]
def Spe():
    Specialite=model.renvoie_specialite()
    for i in range(len(Specialite)) : #on affiche les spécialite avec un numero pour faciliter l'usage du programme
        print(i+1,Specialite[i])
        
    specialiteid=int(input("donne le numero de la spécialite \n"))
    
    while specialiteid>len(Specialite) or specialiteid<1 : #Eviter un bug
        specialiteid=int(input("donne le numero de la spécialite  compris entre 1 et 4 \n"))
    
    Ecole=model.filtre(specialiteid)
    if len(Ecole)==0:# Si la liste a aucun élèment 
        print("Pas d'école trouvée en fonction des critéres")
    else:
        print("Voila les écoles : \n") #On affiche les écoles contenue dans la liste 
        for i in range(len(Ecole)): 
            print(Ecole[i])
            
            

def concours():
    nomduconcours=input("CCS ou CCP\n")
    Concours=model.filtreadmission(nomduconcours)
    if len(Concours)==0:# Si la liste a aucun élèment 
        print("Pas d'école trouvée en fonction des critéres")
    else:
        print("Voila les écoles : \n") #On affiche les écoles contenue dans la liste 
        for i in range(len(Concours)): 
            print(Concours[i])
    
def choixtri():
    choix=input("Trier en foction de la 1)Specialite ou 2)Concours \n")
    if choix=="1" :
        Spe()
    elif choix=="2" :
        concours()
    while choix!="1" and choix!="2" :
        choix=input("Trier en foction de la 1)Specialite ou 2)Concours")       
choixtri()
