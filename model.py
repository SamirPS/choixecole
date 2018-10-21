c#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018

@author: samir
"""
import sqlite3
Spe=[]#liste des spécialité
Ecole=[]#Liste des ecoles
connexion = sqlite3.connect('choixecole.db')#O ouvre la base de donnée
curseur = connexion.cursor() 

def specialité(table):
    """Nous revoie toutes les spécialité disponible sous forme d'une liste de tuples"""
    curseur.execute("SELECT Nom FROM Specialite")
    specialite = curseur.fetchall()
    for specialite in specialite:
        table.append(specialite) #cherche les specialité dans la table spe
    return table

def filtre(table,specialiteid):
     """Nous revoie toutes les ecoles disponible en fonction de la specialité choisi sous forme d'une liste de tuples"""
     return table


Spe=specialité(Spe)
print(Spe)

specialiteid=int(input("donne le numero de la spécialite le premier terme de la liste est 0 \n"))
while specialiteid>len(Spe):
    print("bien jouer le bug ")
    specialiteid=int(input("donne le numero de la spécialite le premier terme de la liste est 0 \n"))

Ecole=filtre(Ecole,specialiteid)
