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
    """Renvoie la liste des Communes des differentes ecoles"""
    
    Commune=[]
    Commune.append("Peu importe") #Si on veut pas choisir de commune.
    curseur.execute("SELECT Commune FROM EcoleS")
    commune = curseur.fetchall() #resultats de la commande
    for commune in commune:
        Commune.append(commune[0]) #apprend les communes dans la liste commune
    Commune=list(set(Commune)) #enleve les doublons
    return Commune

def renvoie_concours():
    
    """Renvoie la liste des concours """
    Concours=[]
    Concours.append("Peu importe")#Si on veut pas choisir de concours.
    curseur.execute("SELECT Admission FROM EcoleS")
    concours = curseur.fetchall() #resultats de la commande
    for concours in concours:
        Concours.append(concours[0]) #apprend les concours dans la liste concours
    Concours=list(set(Concours))#enleve les doublons
    return Concours


def renvoie_coeffccs():
    """Permet d'avoir les coefficient de CSS pour avoir la Note"""
    Coeffccs=[]
    curseur.execute("Select Coefficient FROM CCSCoeff")
    coeffccs=curseur.fetchall()
    for coeffccs in coeffccs:
        Coeffccs.append(float(coeffccs[0]))
    return Coeffccs

def renvoie_coeffccp():
    """Permet d'avoir les coefficient de CCP pour avoir la Note"""
    Coeffccp=[]
    curseur.execute("Select Coefficient FROM CCPCoeff")
    coeffccp=curseur.fetchall()
    for coeffccp in coeffccp:
        Coeffccp.append(float(coeffccp[0]))
    return Coeffccp


def renvoie_specialite():
    
    """Nous revoie toutes les spécialité disponible sous forme d'une liste"""
    Specialite=[]
    curseur.execute("SELECT Nom FROM Specialite")
    valeur_spe = curseur.fetchall() #resultats de la commande
    for valeur_spe in valeur_spe:
        Specialite.append(valeur_spe[0]) #apprend les specialité dans la table spe
    Specialite=list(set(Specialite))#enleve les doublons
    return Specialite

def BoucleNote(Note):
    """Permet de connaitre le nombres de fois ou on passe dans le for depend de la Note afin d'avoir le Niveau de l'utilisateur"""
    Boucle=0
    if Note>15 :
        Boucle=3
    elif 10<Note<15:
        Boucle=2
    elif  0<Note<10:
        Boucle=1
    return Boucle 


def filtre(specialiteid,communeid,concoursid,Note):
    """C'est un filtre qui renvoie les ecoles en fonction des choix et de la note de l'utilisateur"""
    
    Condition=["Facile","Moyen","Dur"]
    Boucle=BoucleNote(Note)
    Ecole=[]
    
    if concoursid=="Peu importe":
        if communeid=="Peu importe":
            for z in range(Boucle):
                curseur.execute("SELECT Nom,Admission,Commune FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? And Niveau=? ",(specialiteid,Condition[z],))
                ecole=curseur.fetchall()
                for ecole in ecole :
                    Ecole.append(ecole)
        else:
            for z in range(Boucle):
                curseur.execute("SELECT Nom,Admission,Commune  FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Niveau=? ",(specialiteid,communeid,Condition[z],))
                ecole=curseur.fetchall()
                for ecole in ecole :
                    Ecole.append(ecole)
    else :
        if communeid=="Peu importe":
            for z in range(Boucle):
                curseur.execute("SELECT Nom,Admission,Commune  FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? And Niveau=? And Admission=? ",(specialiteid,Condition[z],concoursid,))
                ecole=curseur.fetchall()
                for ecole in ecole :
                    Ecole.append(ecole)
        else:
            for z in range(Boucle):
                curseur.execute("SELECT Nom,Admission,Commune  FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Niveau=? And Admission=? ",(specialiteid,communeid,Condition[z],concoursid,))
                ecole=curseur.fetchall()
                for ecole in ecole :
                    Ecole.append(ecole)
    
    return Ecole