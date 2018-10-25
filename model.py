#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018
@author: samir
"""
import sqlite3
connexion = sqlite3.connect('choixecole.db')#On ouvre la base de donnée
curseur = connexion.cursor() #execute les commandes sql

def renvoie_specialite():
    """Nous revoie toutes les spécialité disponible sous forme d'une liste"""
    Specialite=[]
    curseur.execute("SELECT Nom FROM Specialite")
    valeur_spe = curseur.fetchall() #resultats de la commande
    for valeur_spe in valeur_spe:
        Specialite.append(valeur_spe[0]) #apprend les specialité dans la table spe
    return Specialite


def filtre(specialiteid):
    """Renvoie les Ecoles en fonction de la specialité choisie"""
    Ecole=[]
    curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? ",(specialiteid,))
    ecole = curseur.fetchall() #resultat de la commande
    for ecole in ecole:
        Ecole.append(ecole[0]) #appends les ecoles en fonction de la  specialité 
    return Ecole


def filtreadmission(nomduconcours):
    """Renvoie les Ecoles en fonction du concours"""
    Concours=[]
    curseur.execute("SELECT NOM,Admission FROM EcoleS WHERE Admission=?",(niveau,))
    concours=curseur.fetchall()
    for concours in concours :
        Concours.append(concours[0])
    return Concours
