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
    for resultat in curseur:
        Informationvoulue.append(resultat[0])
    if colonne=="Commune" or colonne=="Admission":
        Informationvoulue[0:0] = ["Peu importe"]
        Informationvoulue=list(set(Informationvoulue))
    return Informationvoulue

def filtre(specialiteid,communeid,concoursid,Note):
    """Construit la requete Sql et filtre les ecoles en fonction du choix de l'utilisateur"""
    Ecole=[]
    requete="SELECT Nom,Admission,Commune FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe="+str(specialiteid)
    Condition=[]
    
    if Note>15 :
        Condition.append(("Niveau","<=",2))
    if 10<Note<15:
        Condition.append(("Niveau","<=",1))
    if  0<Note<10:
        Condition.append(("Niveau","<=",0))
    if concoursid!="Peu importe" :
        Condition.append(("Admission","=",concoursid))
    if communeid!="Peu importe":
        Condition.append(("Commune","=",communeid))
    for i in range(len(Condition)):
        requete=requete+" And "+Condition[i][0]+Condition[i][1]+'"'+str(Condition[i][2])+'"'
        
    curseur.execute(requete)
    for ecole in curseur :
        Ecole.append(ecole)
    return Ecole
