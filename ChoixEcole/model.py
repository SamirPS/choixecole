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
       Ex:renvoie_information("Nom","Specialite") renvoie les spécialites dans la liste Informationvoulue
                                                                                                            """
    colonne_peuimporte=("Nom","Region","Admission","Alternance")
    informationvoulue=[resultat[0] for resultat in curseur.execute("SELECT "+colonne+" FROM "+table) ]
    if colonne in colonne_peuimporte :
        informationvoulue=["Peu importe"]+sorted(list(set(informationvoulue)))
    return informationvoulue

def renvoie_coefficient():
    colonne="Groupe,Modelisation,Maths,Physique,SI,Informatique,Anglais,Francais,Bonification "
    CCS,CCP={},{}
    curseur.execute("Select "+colonne+" From Coefficient WHERE Concours='CCS'" )
    for resultat in curseur:
        CCS[resultat[0]]=list(resultat[1:])
    curseur.execute("Select "+colonne+" From Coefficient WHERE Concours='CCP'" )
    for resultat in curseur:
        CCP[resultat[0]]=list(resultat[1:])
    return CCS,CCP

def NoteCoefficient(coefficient,matiere):
    """Renvoie la note coefficiente"""
    note=[sum(coefficient[coeff]*matiere[coeff] for coeff in range (len(matiere)))]
    return note[0] 

def filtre(specialiteid,choix_region,concoursid,alternanceid,groupe,note):
    
    """
    Construit la requete Sql et filtre les ecoles en fonction du choix de l'utilisateur
    """
    conditions=[("Points","<=",note)]
    
    if groupe!=None:
        conditions.append(("Groupe","=",groupe))
    if specialiteid!=None:
        conditions.append(("Idspe","=",specialiteid))
    if alternanceid!=None:
        conditions.append(("Alternance","=",alternanceid))
    if concoursid!=None :
        conditions.append(("Admission","=",concoursid))
    if choix_region!=None:
        conditions.append(("Region","=",choix_region))
    
    requete="SELECT Nom,Admission,Commune FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE "
    variables=tuple(conditions[i][2] for i in  range (len(conditions)))
    for i in range(len(conditions)):
        requete=requete+conditions[i][0]+conditions[i][1]+"? "+" AND "
    ecoles=[ecole for ecole in curseur.execute(requete[0:len(requete)-4],variables)]
    return ecoles