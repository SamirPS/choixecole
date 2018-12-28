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
    curseur.execute("SELECT "+colonne+" FROM "+table)
    informationvoulue=[]
    for resultat in curseur:
        informationvoulue.append(resultat[0])
    if colonne=="Commune" or colonne=="Admission" or colonne=="Alternance":
        informationvoulue[0:0] = ["Peu importe"]
        informationvoulue=list(set(informationvoulue))
    return informationvoulue

def filtre(specialiteid,communeid,concoursid,alternanceid,note):
    """
    Construit la requete Sql et filtre les ecoles en fonction du choix de l'utilisateur
    """
    
    conditions=[]
    if note>=15 :
        conditions.append(("Niveau","<=",2))
    elif 10<=note:
        conditions.append(("Niveau","<=",1))
    elif 0<=note:
        conditions.append(("Niveau","<=",0))
        
    if specialiteid!=None:
        conditions.append(("Idspe","=",specialiteid))
    if alternanceid!=None:
        conditions.append(("Alternance","=",alternanceid))
    if concoursid!=None :
        conditions.append(("Admission","=",concoursid))
    if communeid!=None:
        conditions.append(("Commune","=",communeid))
    
    requete="SELECT Nom,Admission,Commune FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id"
    variables=()  
    
    for i in range(len(conditions)):
        requete=requete+" AND "+conditions[i][0]+conditions[i][1]+"? "
        variables=variables+(conditions[i][2],)   
        
    ecoles=[]
    curseur.execute(requete,variables)
    for ecole in curseur :
        ecoles.append(ecole)
    return ecoles