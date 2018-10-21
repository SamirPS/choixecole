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

def specialite(table):
    
    """Nous revoie toutes les spécialité disponible sous forme d'une liste de tuples"""
    
    curseur.execute("SELECT Nom FROM Specialite")
    listespecialite= curseur.fetchall()
    for listespecialite in listespecialite:
        table.append(listespecialite) #cherche les specialité dans la table spe
    return table


def filtre(table,specialitéid):
    """renvoie la liste des ecoles en fonction de la specialite """
