#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:19:23 2019
@author: robinchaussemy
"""
import openpyxl
import sqlite3

connexion = sqlite3.connect("choixecole.db")
curseur = connexion.cursor()


""" Retourne la taille du fichier et les valeurs"""

book = openpyxl.load_workbook('BdDEcoles.xlsx')
sheet = book.get_sheet_by_name('Ecoles')
book2= openpyxl.load_workbook('sam.xlsx')
sheet2 =book2.get_sheet_by_name('Feuille8')

"""Connaitre le nombre de colonnes et de lignes des feuilles """
r = sheet.max_row
c = sheet.max_column
r1 = sheet2.max_row
c1= sheet2.max_column

def ecole():
    curseur.execute("DROP TABLE EcoleS")
    connexion.commit()
    curseur.execute("CREATE TABLE `EcoleS` (`Id`	INTEGER PRIMARY KEY AUTOINCREMENT,`Acronyme`	TEXT,`Nom`	TEXT,`Groupe`	TEXT,`Commune`	TEXT,`Region`	TEXT,`Admission`	TEXT,`Statut`	TEXT,`Points`	INTEGER);")

    for i in range(3,r):
        t2=[]
        for j in range(1, c+1):
            temp=sheet.cell(row=i, column=j).value
            t2.append(temp)
        curseur.execute("INSERT INTO EcoleS (Acronyme,Nom,Commune,Region,Admission,Statut,Points,Groupe) VALUES  (?,?,?,?,?,?,?,?)",(t2[0],t2[1],t2[2],t2[3],t2[5],t2[6],0,t2[5]))

    connexion.commit()

def spe():
    curseur.execute("DROP TABLE Specialite")
    connexion.commit()
    curseur.execute("CREATE TABLE Specialite(Idspecialite INTEGER PRIMARY KEY AUTOINCREMENT,NomSpe TEXT)")
    for i in range(11,35):
        temp=sheet.cell(row=2,column=i).value
        curseur.execute("INSERT INTO Specialite (NomSpe) VALUES (?)",(temp,))


def alter():
    curseur.execute("DROP TABLE EcoleSpe")
    connexion.commit()
    curseur.execute(
        "CREATE TABLE `EcoleSpe` (`IdEcole`	INTEGER,`IdSpe` INTEGER,`Alternance` TEXT,FOREIGN KEY(`IdEcole`) REFERENCES `EcoleS`(`Id`),UNIQUE(`IdEcole`,`IdSpe`,`Alternance`),FOREIGN KEY(`IdSpe`) REFERENCES `Specialite`(`Idspecialite`));")

    for i in range(3, r):
        for j in range(11, 35):
            temp = sheet.cell(row=i, column=38).value
            temp2 = sheet.cell(row=i, column=j).value
            if temp2 == "OUI":
                temp = temp.capitalize()
                curseur.execute("INSERT INTO EcoleSpe (Alternance,IdSpe,IdEcole) VALUES (?,?,?)", (temp, j - 10, i - 2))
def creeDB():

    ecole()
    spe()
    alter()
    connexion.commit()
creeDB()