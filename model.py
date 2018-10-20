#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018

@author: samir
"""
import sqlite3
Spe=[]#liste des spécialité
connexion = sqlite3.connect('choixecole.db')#O ouvre la base de donnée
curseur = connexion.cursor() 

def specialité(table):
    """Nous revoie toutes les spécialité disponible sous forme d'une liste de tuples"""
    curseur.execute("SELECT Nom FROM Specialité")
    specialite = curseur.fetchall()
    for specialite in specialite:
        table.append(specialite) #cherche les specialité dans la table spe
    return table


def filtre(table,specialitéid):
    return 0
