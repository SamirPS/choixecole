#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018

@author: samir
"""
import sqlite3
Spe=[]#liste des spécialité
Ecole=[]#Liste des ecoles
connexion = sqlite3.connect('choixecole.db')#On ouvre la base de donnée
curseur = connexion.cursor() #execute les commandes sql

def specialite(table):
    """Nous revoie toutes les spécialité disponible sous forme d'une liste de tuples"""
    curseur.execute("SELECT Nom FROM Specialite")
    specialite = curseur.fetchall() #resultats de la commande
    for specialite in specialite:
        table.append(specialite[0]) #apprend les specialité dans la table spe
    return table


def filtre(table,specialiteid):
    curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=?",(specialiteid,))
    ecole = curseur.fetchall() #resultat de la commande
    for ecole in ecole:
        table.append(ecole[0]) #appends les ecoles en fonction de la  specialité 
    return table


Spe=specialite(Spe)
for i in range(len(Spe)) : #on affiche les spécialite avec un numero pour faciliter l'usage du programme
    print(i+1,Spe[i])
    
specialiteid=int(input("donne le numero de la spécialite \n"))


while specialiteid>len(Spe): #Eviter un bug
    print("bien jouer le bug ")
    specialiteid=int(input("donne le numero de la spécialite  \n"))

Ecole=filtre(Ecole,specialiteid)

if len(Ecole)==0:# Si la liste a aucun élèment 
    print("Pas d'école trouvée en fonction des critéres")
else:
    print("Voila les écoles : \n") #On affiche les écoles contenue dans la liste 
    for i in range(len(Ecole)): 
        print(Ecole[i])

connexion.close() #on se deconnecte de la bdd
