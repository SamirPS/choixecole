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
    if colonne=="Commune" or colonne=="Admission" or colonne=="Alt":#apprend les communes dans la liste commune
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

def filtre(specialiteid,communeid,concoursid,Note,alternanceid):
    boucle=BoucleNote(Note)
    Ecole=[]
    donnee=()
    requete="SELECT Nom,Admission,Commune FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? And Niveau=?"
    Condition=[["Facile","Moyen","Dur"],]
    
    if concoursid!="Peu importe" :
        Condition.append(("Admission=?",concoursid))
    if communeid!="Peu importe":
        Condition.append(("Commune=?",communeid))
    if alternanceid!="Peu importe":
        Condition.append(("Alt=?",alternanceid))
        
    for i in range(1,len(Condition)):
        requete=requete+" And "+Condition[i][0]
        donnee=donnee+(Condition[i][1],)
    for z in range(boucle):
        variable=(specialiteid,Condition[0][z])+donnee
        curseur.execute(requete,variable)
        ecole=curseur.fetchall()
        for ecole in ecole :
            Ecole.append(ecole)
    return Ecole