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

def renvoie_admission():

    return [resultat[0] for resultat in curseur.execute("SELECT DISTINCT Admission FROM EcoleS") ]

def renvoie_specialites():

    return [resultat[0] for resultat in curseur.execute("SELECT  DISTINCT Nom FROM Specialite") ]

def renvoie_regions():

    return [resultat[0] for resultat in curseur.execute("SELECT DISTINCT Region FROM EcoleS")]

def renvoie_idspe(choix):

    choix=tuple(choix)
    for i in choix:
        choix+=tuple(spe[0] for spe in curseur.execute("SELECT Id FROM Specialite WHERE Nom="+"'"+i+"'"))
    return choix



def filtre(choix_utilisateur, notes):

    """
    Construit la requete Sql et filtre les ecoles en fonction du choix de l'utilisateur
    """
    conditions=[]
    if choix_utilisateur["specialites"]!=None:
        conditions.append(["Idspe","IN",choix_utilisateur["specialites"]])
    if choix_utilisateur["alternance"]!=None:
        conditions.append(["Alternance","IN",choix_utilisateur["alternance"]])
    if choix_utilisateur["concours"]!=None:
        conditions.append(["Admission","IN",choix_utilisateur["concours"]])
    if choix_utilisateur["regions"]!=None:
        conditions.append(["Region","IN",choix_utilisateur["regions"]])

    if choix_utilisateur["annee"]==("3/2",):
        bonif_str = "Bonification"
    else:
        bonif_str = "0"

    variables=tuple(cond[2] for cond in conditions if cond[1]!="IN")
    requete=( """
        SELECT Nom,Admission,Commune
        FROM EcoleSpe
        JOIN EcoleS on EcoleSpe.IdEcole=EcoleS.id
        JOIN Coefficient on Coefficient.Groupe=EcoleS.Groupe
        WHERE """
        +  str(notes["maths"])+"""*Maths+"""
        +  str(notes["physique"])+"""*Physique+"""
        +  str(notes["si"])+"""*SI+"""
        +  str(notes["informatique"])+"""*Informatique+"""
        +  str(notes["anglais"])+"""*Anglais+"""
        +  str(notes["francais"])+"""*Francais+"""
        +  str(notes["modelisation"])+"""*Modelisation+"""
        +  bonif_str
        + """>= Points AND """

    )

    for i in range(len(conditions)):
        if conditions[i][1]=="IN":
            if len(conditions[i][2])==1:
                requete+=conditions[i][0]+" "+conditions[i][1]+" "+str(conditions[i][2])[0:-2]+")"+" AND "
            else:
                requete+=conditions[i][0]+" "+conditions[i][1]+" "+str(conditions[i][2])+" AND "

        else:
            requete+=conditions[i][0]+conditions[i][1]+"? "+" AND "
    print(requete)
    ecoles=[ecole for ecole in curseur.execute(requete[0:len(requete)-4],variables)]
    return ecoles