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
    colonne_peuimporte=("Region","Admission","Alternance")
    informationvoulue=[resultat[0] for resultat in curseur.execute("SELECT "+colonne+" FROM "+table) ]
    if colonne=="Nom":
         informationvoulue=["Peu importe"]+informationvoulue
    if colonne in colonne_peuimporte :
        informationvoulue=["Peu importe"]+list(set(informationvoulue))
    return informationvoulue

def renvoie_coefficient():
    """Donne la liste des concours  et donne les groupes et coefficient grâce a un dictonnaire """
       
    colonne="Groupe,Maths,Physique,SI,Informatique,Anglais,Francais,Modelisation,Bonification "
    liste_concours=list(set(renvoie_information("Concours","Coefficient")))
    concours={}
    for nom in liste_concours:
        concours[nom]={}
        curseur.execute("Select "+colonne+" From Coefficient WHERE Concours="+'"'+nom+'"')
        for resultat in curseur:
            concours[nom][resultat[0]]=list(resultat[1:])
    return concours


def NoteCoefficient(matiere,variable):
    coefficient=renvoie_coefficient()
    dictnoteconcours={note:{} for note in coefficient}
    for nom in coefficient:
        for cle in coefficient[nom]:
            ss={
            "maths": coefficient[nom][cle][0],
            "physique": coefficient[nom][cle][1],
            "si":coefficient[nom][cle][2],
            "informatique":coefficient[nom][cle][3],
            "anglais":coefficient[nom][cle][4],
            "francais":coefficient[nom][cle][5],
            "modelisation":coefficient[nom][cle][6],
            }
            if variable==("3/2",):
                dictnoteconcours[nom][cle]=[(ss[key]*matiere[key]) for key in ss ]+[coefficient[nom][cle][7]]
                dictnoteconcours[nom][cle]=sum(dictnoteconcours[nom][cle])
            else :
                dictnoteconcours[nom][cle]=[(ss[key]*matiere[key]) for key in ss]
                dictnoteconcours[nom][cle]=sum(dictnoteconcours[nom][cle])   
    return dictnoteconcours

def filtre(choix_utilisateur,groupe,note):

    """
    Construit la requete Sql et filtre les ecoles en fonction du choix de l'utilisateur
    """
    
    conditions=[]
    if note!=None:
        conditions.append(("Points","<=",note))
    if groupe!=None:
        conditions.append(("Groupe","=",groupe))
    if choix_utilisateur["Specialite"]!=None:
        conditions.append(("Idspe","IN",choix_utilisateur["Specialite"]))
    if choix_utilisateur["Alternance"]!=None:
        conditions.append(("Alternance","IN",choix_utilisateur["Alternance"]))
    if choix_utilisateur["Concours"]!=None :
        conditions.append(("Admission","IN",choix_utilisateur["Concours"]))
    if choix_utilisateur["Region"]!=None:
        conditions.append(("Region","IN",choix_utilisateur["Region"]))
    
    
    variables=tuple(conditions[i][2] for i in  range (len(conditions)) if conditions[i][1]!="IN")
    requete="SELECT Nom,Admission,Commune FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE "
    
    for i in range(len(conditions)):
        if conditions[i][1]=="IN":
            if len(conditions[i][2])==1:
                requete+=conditions[i][0]+" "+conditions[i][1]+" "+str(conditions[i][2])[0:-2]+")"+" AND "
            else: 
                requete+=conditions[i][0]+" "+conditions[i][1]+" "+str(conditions[i][2])+" AND "
                
        else:
            requete+=conditions[i][0]+conditions[i][1]+"? "+" AND "
    
    if conditions==[]:
        requete=requete[0:len(requete)-6]
    else :
        requete=requete[0:len(requete)-4]
        
    ecoles=[ecole for ecole in curseur.execute(requete,variables)]
    return ecoles