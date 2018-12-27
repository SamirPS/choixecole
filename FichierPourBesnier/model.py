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
    """
    Construit la requete Sql et filtre les ecoles en fonction du choix de l'utilisateur
    """
    ecoles,conditions,variables=[],[],(specialiteid,)
    requete="SELECT Nom,Admission,Commune FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE Idspe=?"
    
    if Note>=15 :
        conditions.append(("Niveau","<=",2))
    elif 10<=Note:
        conditions.append(("Niveau","<=",1))
    elif 0<Note:
        conditions.append(("Niveau","<=",0))
    else :
        return ecoles
        
    if concoursid!=None :
        conditions.append(("Admission","=",concoursid))
    if communeid!=None:
        conditions.append(("Commune","=",communeid))
        
    for i in range(len(conditions)):
        requete=requete+" AND "+conditions[i][0]+conditions[i][1]+"? "
        variables=variables+(conditions[i][2],)   
        
    curseur.execute(requete,variables)
    for ecole in curseur :
        ecoles.append(ecole)
    return ecoles