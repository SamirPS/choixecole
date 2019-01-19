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
    for i in range(len(choix)):
        choix+=tuple(resultat[0] for resultat in curseur.execute("SELECT Id FROM Specialite WHERE Nom="+"'"+choix[i]+"'"))
    return choix
        

def renvoie_coefficient():
    """Donne la liste des concours  et donne les groupes et coefficient grâce a un dictonnaire """
       
    colonne="Groupe,Maths,Physique,SI,Informatique,Anglais,Francais,Modelisation,Bonification "
    liste_concours=list(set([resultat[0] for resultat in curseur.execute("SELECT Concours FROM Coefficient")]))
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
            coeff={
            "maths": coefficient[nom][cle][0],
            "physique": coefficient[nom][cle][1],
            "si":coefficient[nom][cle][2],
            "informatique":coefficient[nom][cle][3],
            "anglais":coefficient[nom][cle][4],
            "francais":coefficient[nom][cle][5],
            "modelisation":coefficient[nom][cle][6],
            }
            if variable==("3/2",):
                dictnoteconcours[nom][cle]=sum(coeff[key]*matiere[key] for key in coeff)+coefficient[nom][cle][7]
            else :
                dictnoteconcours[nom][cle]=sum(coeff[key]*matiere[key] for key in coeff)
    
    return dictnoteconcours

def filtre(choix_utilisateur,groupe,note):

    """
    Construit la requete Sql et filtre les ecoles en fonction du choix de l'utilisateur
    """
    conditions=[]
    ConditionsVariable={"note":("Points","<=",note),
                        "groupe":("groupe","=",groupe),
                        choix_utilisateur["specialites"]:("Idspe","IN",choix_utilisateur["specialites"]),
                        choix_utilisateur["alternance"]:("Alternance","IN",choix_utilisateur["alternance"]),
                        choix_utilisateur["concours"]:("Admission","IN",choix_utilisateur["concours"]),
                        choix_utilisateur["regions"]:("Region","IN",choix_utilisateur["regions"])
                        }
    
    for cle in ConditionsVariable:
        if ConditionsVariable[cle][2]!=None:
            conditions.append(ConditionsVariable[cle])
            
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
    
    if not conditions:
        requete=requete[0:len(requete)-6]
    else :
        requete=requete[0:len(requete)-4]
        
        
    ecoles=[ecole for ecole in curseur.execute(requete,variables)]
    return ecoles