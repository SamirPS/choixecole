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

def specialité(table):
    """Nous revoie toutes les spécialité disponible sous forme d'une liste de tuples"""
    curseur.execute("SELECT Nom FROM Specialite")
    specialite = curseur.fetchall() #resultats de la commande
    for specialite in specialite:
        table.append(specialite) #apprend les specialité dans la table spe
    return table

def filtre(table,specialiteid):
    curseur.execute("SELECT IdEcole FROM EcoleSpe")
    ecole = curseur.fetchall() #resultat de la commande
    for ecole in ecole:
        table.append(ecole) #appends les ecoles en fonction de la  specialité 
    return table

Spe=specialité(Spe)
print(Spe)

specialiteid=int(input("donne le numero de la spécialite \n"))
while specialiteid>len(Spe):
    print("bien jouer le bug ")
    specialiteid=int(input("donne le numero de la spécialite  \n"))

Ecole=filtre(Ecole,specialiteid)
print(Ecole)
