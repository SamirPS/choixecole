#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018
@author: samir
"""
import sqlite3
connexion = sqlite3.connect("choixecole.db")#On ouvre la base de donnée
curseur = connexion.cursor() #execute les commandes sql


def renvoie_commune():
    Commune=[]
    Commune.append("Peu importe")
    curseur.execute("SELECT Commune FROM EcoleS")
    commune = curseur.fetchall() #resultats de la commande
    for commune in commune:
        Commune.append(commune[0]) #apprend les specialité dans la table spe
    Commune=list(set(Commune))
    return Commune

def renvoie_concours():
    Concours=[]
    Concours.append("Peu importe")
    curseur.execute("SELECT Admission FROM EcoleS")
    concours = curseur.fetchall() #resultats de la commande
    for concours in concours:
        Concours.append(concours[0]) #apprend les specialité dans la table spe
    Concours=list(set(Concours))
    return Concours


def renvoie_coeffccs():
    Coeffccs=[]
    curseur.execute("Select Coefficient FROM CCSCoeff")
    coeffccs=curseur.fetchall()
    for coeffccs in coeffccs:
        Coeffccs.append(coeffccs[0])
    return Coeffccs

def renvoie_coeffccp():
    Coeffccp=[]
    curseur.execute("Select Coefficient FROM CCPCoeff")
    coeffccp=curseur.fetchall()
    for coeffccp in coeffccp:
        Coeffccp.append(coeffccp[0])
    return Coeffccp


def renvoie_specialite():
    
    """Nous revoie toutes les spécialité disponible sous forme d'une liste"""
    Specialite=[]
    curseur.execute("SELECT Nom FROM Specialite")
    valeur_spe = curseur.fetchall() #resultats de la commande
    for valeur_spe in valeur_spe:
        Specialite.append(valeur_spe[0]) #apprend les specialité dans la table spe
    return Specialite

def BoucleNote(Note):
    a=0
    if Note>15 :
        a=3
    elif 10<Note<15:
        a=2
    elif  0<Note<10:
        a=1
    return a 


def filtre(specialiteid,communeid,concoursid,Note):
    Condition=[("Facile","Moyen","Dur")]
    a=BoucleNote(Note)
    Ecole=[]
    if concoursid=="Peu importe":
        if communeid=="Peu importe":
            for z in range(a):
                curseur.execute("SELECT Nom,Admission,Commune FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? And Niveau=? ",(specialiteid,Condition[0][z],))
                ecole=curseur.fetchall()
                for ecole in ecole :
                    Ecole.append(ecole)
        else:
            for z in range(a):
                curseur.execute("SELECT Nom,Admission,Commune  FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Niveau=? ",(specialiteid,communeid,Condition[0][z],))
                ecole=curseur.fetchall()
                for ecole in ecole :
                    Ecole.append(ecole)
    else :
        if communeid=="Peu importe":
            for z in range(a):
                curseur.execute("SELECT Nom,Admission,Commune  FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? And Niveau=? And Admission=? ",(specialiteid,Condition[0][z],concoursid,))
                ecole=curseur.fetchall()
                for ecole in ecole :
                    Ecole.append(ecole)
        else:
            for z in range(a):
                curseur.execute("SELECT Nom,Admission,Commune  FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Niveau=? And Admission=? ",(specialiteid,communeid,Condition[0][z],concoursid,))
                ecole=curseur.fetchall()
                for ecole in ecole :
                    Ecole.append(ecole)
    
    return Ecole