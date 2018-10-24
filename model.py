#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018
@author: samir
"""
import sqlite3
Spe=[]#liste des spécialité
Ecole=[]#Liste des ecoles
Alternance=["non","oui","n'importe"]
connexion = sqlite3.connect('choixecole.db')#On ouvre la base de donnée
curseur = connexion.cursor() #execute les commandes sql

def specialite():
    """Nous revoie toutes les spécialité disponible sous forme d'une liste de tuples"""
    curseur.execute("SELECT Nom FROM Specialite")
    specialite = curseur.fetchall() #resultats de la commande
    for specialite in specialite:
        Spe.append(specialite[0]) #apprend les specialité dans la table spe
    return Spe


def filtre(specialiteid,alternanceid):
    if alternanceid==3:
        curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? and IdAlternance=?",(specialiteid,0))
        ecole = curseur.fetchall() #resultat de la commande
        for ecole in ecole:
            Ecole.append(ecole[0]) #appends les ecoles en fonction de la  specialité 
        curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? and IdAlternance=?",(specialiteid,1))
        ecole = curseur.fetchall() #resultat de la commande
        for ecole in ecole:
            Ecole.append(ecole[0]) #appends les ecoles en fonction de la  specialité 
        return Ecole
    curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? and IdAlternance=?",(specialiteid,alternanceid-1))
    ecole = curseur.fetchall() #resultat de la commande
    for ecole in ecole:
        Ecole.append(ecole[0]) #appends les ecoles en fonction de la  specialité 
    return Ecole


Spe=specialite()

for i in range(len(Spe)) : #on affiche les spécialite avec un numero pour faciliter l'usage du programme
    print(i+1,Spe[i])
    
specialiteid=int(input("donne le numero de la spécialite \n"))
for k in range(1):
    print("\n")
    
print("Alternance:")
for j in range(len(Alternance)) :
    print(j+1,Alternance[j])
    
    
alternanceid=int(input("donne le numero en fonction du choix \n"))


while specialiteid>len(Spe) or specialiteid<1  or alternanceid>len(Alternance)  or alternanceid<1 : #Eviter un bug
    print("bien jouer le bug ")
    specialiteid=int(input("donne le numero de la spécialite  \n"))

Ecole=filtre(specialiteid,alternanceid)

if len(Ecole)==0:# Si la liste a aucun élèment 
    print("Pas d'école trouvée en fonction des critéres")
else:
    print("Voila les écoles : \n") #On affiche les écoles contenue dans la liste 
    for i in range(len(Ecole)): 
        print(Ecole[i])

connexion.close() #on se deconnecte de la bdd