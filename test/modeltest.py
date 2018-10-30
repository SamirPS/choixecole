#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018
@author: samir
"""
import sqlite3

def file(file):
    global connexion,curseur
    connexion = sqlite3.connect(file)#On ouvre la base de donnée
    curseur = connexion.cursor() #execute les commandes sql



def renvoie_specialite():
    
    """Nous revoie toutes les spécialité disponible sous forme d'une liste"""
    Specialite=[]
    curseur.execute("SELECT Nom FROM Specialite")
    valeur_spe = curseur.fetchall() #resultats de la commande
    for valeur_spe in valeur_spe:
        Specialite.append(valeur_spe[0]) #apprend les specialité dans la table spe
    return Specialite


def filtre(specialiteid,communeid,concoursid,Note):
    """Renvoie les Ecoles en fonction de la specialité choisie"""
    Ecole=[]
    if Note>15 :    
        if concoursid=="Peu importe":
            if communeid=="Peu importe":
                curseur.execute("SELECT Nom,Admission FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Niveau='Dur' ",(specialiteid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) 
                    
                curseur.execute("SELECT Nom,Admission FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Niveau='Moyen'  ",(specialiteid,))
                ecole= curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole)
                    
                curseur.execute("SELECT Nom,Admission FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Niveau='Facile' ",(specialiteid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole)
                    #appends les ecoles en fonction de la  specialité 
                
                return Ecole
            
            else :
                curseur.execute("SELECT Nom, Admission FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Niveau='Dur'  ",(specialiteid,communeid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) #appends les ecoles en fonction de la  specialité 
                
                curseur.execute("SELECT Nom, Admission FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE  IdSpe=? AND Commune=? AND  Niveau='Moyen'  ",(specialiteid,communeid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) #appends les ecoles en fonction de la  specialité 
                
                curseur.execute("SELECT Nom, Admission FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE  IdSpe=? AND Commune=? AND Niveau='Facile' ",(specialiteid,communeid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) #appends les ecoles en fonction de la  specialité 
                
                return Ecole
        else:
            if communeid=="Peu importe":
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? and Admission=? AND Niveau='Dur' ",(specialiteid,concoursid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) #appends les ecoles en fonction de la  specialité 
            
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? and Admission=? AND Niveau='Moyen' ",(specialiteid,concoursid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) #appends les ecoles en fonction de la  specialité 

                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? and Admission=? AND Niveau='Facile' ",(specialiteid,concoursid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) #appends les ecoles en fonction de la  specialité 
                return Ecole
            else :
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Admission=? AND Niveau='Dur' ",(specialiteid,communeid,concoursid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) 
                    
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Admission=? AND Niveau='Moyen' ",(specialiteid,communeid,concoursid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) 
                    
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Admission=? AND Niveau='Facile' ",(specialiteid,communeid,concoursid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) 
                    #appends les ecoles en fonction de la  specialité 
                return Ecole
    elif 10<Note<15:
        if concoursid=="Peu importe":
            if communeid=="Peu importe":
                curseur.execute("SELECT Nom,Admission FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=?  AND Niveau='Moyen'",(specialiteid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) 
                
                curseur.execute("SELECT Nom,Admission FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=?  AND Niveau='Facile'",(specialiteid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) #appends les ecoles en fonction de la  specialité 
                return Ecole
            else :
                curseur.execute("SELECT Nom, Admission FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Niveau='Moyen'",(specialiteid,communeid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) 
                
                curseur.execute("SELECT Nom, Admission FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Niveau='Facile'",(specialiteid,communeid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) #appends les ecoles en fonction de la  specialité 
                return Ecole
        else:
            if communeid=="Peu importe":
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? and Admission=? AND  Niveau='Moyen' ",(specialiteid,concoursid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) 
                
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? and Admission=? AND  Niveau='Facile' ",(specialiteid,concoursid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole)
                    #appends les ecoles en fonction de la  specialité 
                return Ecole
            else :
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Admission=? AND Niveau='Moyen' ",(specialiteid,communeid,concoursid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole)
                
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Admission=? AND Niveau='Facile' ",(specialiteid,communeid,concoursid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole)
                    #appends les ecoles en fonction de la  specialité 
                return Ecole
    elif Note>0:
        if concoursid=="Peu importe":
            if communeid=="Peu importe":
                curseur.execute("SELECT Nom,Admission FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Niveau='Facile' ",(specialiteid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) #appends les ecoles en fonction de la  specialité 
                return Ecole
            else :
                curseur.execute("SELECT Nom, Admission FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Niveau='Facile' ",(specialiteid,communeid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) #appends les ecoles en fonction de la  specialité 
                return Ecole
        else:
            if communeid=="Peu importe":
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? and Admission=? AND Niveau='Facile' ",(specialiteid,concoursid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) #appends les ecoles en fonction de la  specialité 
                return Ecole
            else :
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? AND Commune=? AND Admission=? AND Niveau='Facile' ",(specialiteid,communeid,concoursid,))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole) #appends les ecoles en fonction de la  specialité 
                return Ecole
        
        
        

def renvoie_commune():
    Commune=[]
    Commune.append("Peu importe")
    curseur.execute("SELECT Commune FROM EcoleS")
    commune = curseur.fetchall() #resultats de la commande
    for commune in commune:
        Commune.append(commune[0]) #apprend les specialité dans la table spe
    Commune=list(set(Commune))
    return Commune

def renvoie_concours():
    Concours=[]
    Concours.append("Peu importe")
    curseur.execute("SELECT Admission FROM EcoleS")
    concours = curseur.fetchall() #resultats de la commande
    for concours in concours:
        Concours.append(concours[0]) #apprend les specialité dans la table spe
    Concours=list(set(Concours))
    return Concours


def renvoie_coeffccs():
    Coeffccs=[]
    curseur.execute("Select Coefficient FROM CCSCoeff")
    coeffccs=curseur.fetchall()
    for coeffccs in coeffccs:
        Coeffccs.append(coeffccs[0])
    return Coeffccs

def renvoie_coeffccp():
    Coeffccp=[]
    curseur.execute("Select Coefficient FROM CCPCoeff")
    coeffccp=curseur.fetchall()
    for coeffccp in coeffccp:
        Coeffccp.append(coeffccp[0])
    return Coeffccp