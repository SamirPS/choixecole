#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018
@author: samir
"""

"""On ouvre la base de données Sqlite3 et on s'y connecte """
import sqlite3
connexion = sqlite3.connect("choixecole.db")
curseur = connexion.cursor()

def renvoie_information(colonne,table):
    """
       LA fonction prend en variable la colonne et de la table de la base de donnée qui doivent être des str,
       Elle renvoie les information contenue dans la base de donnée dans la liste Informationvoulue
       Ex:renvoie_information("Nom","Specialite") renvoie la liste des spécialites dans la liste Informationvoulue
                                                                                                            """
    Informationvoulue=[]
    curseur.execute("SELECT "+colonne+" FROM "+table)
    resultat = curseur.fetchall() #resultats de la commande
    for resultat in resultat:
        Informationvoulue.append(resultat[0])
    if colonne=="Commune" or colonne=="Admission":#apprend les communes dans la liste commune
        Informationvoulue[0:0] = ["Peu importe"]
        Informationvoulue=list(set(Informationvoulue)) #enleve les doublons
    return Informationvoulue


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
    """
    C'est un filtre qui renvoie les ecoles en fonction des choix et de la note de l'utilisateur
    En fonction de la note ,de la commune du concours et de la spécialite.
    
    """
    
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