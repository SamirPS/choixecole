#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:59:28 2018

@author: samir
"""
from tkinter import Tk,StringVar, Label, Radiobutton,Entry
import model
import tkinter.scrolledtext as tkscrolled
from tkinter.ttk import *

class ChoixEcole:
     
    def __init__(self):
        
        """Initialise l'application et change le titre"""
  
        self.root = Tk()
        self.root.title("ChoixEcole")
        self.root.geometry('900x260')
        self.root.resizable(False, False)
         
        """Initialise  entry et vcmd est une fonction qui verifie si l'utilisateur entre les bonnes informations"""
        
        vcmd = (self.root.register(self.callback),  '%P', '%S')
        self.entry_ecole=tkscrolled.ScrolledText(self.root, width=30, height=10,)
         
        """ Initialise les variables et les entrys et label pour afficher les moyennes et met 20 par défaut"""
        
        self.matieres = ('Maths', 'Physique', 'SI', 'Informatique', 'Francais', 'Anglais')
        self.var_matieres = [StringVar(self.root) for mat in range(len(self.matieres))]
        self.labels_matiere = [ Label(self.root, text='Rentre ta moyenne de '+mat) for mat in self.matieres ] 
        for var in self.var_matieres: var.set(20) 
        self.entries_matiere = [ Entry(self.root, textvariable=var, validate='key', validatecommand = vcmd) for var in self.var_matieres ]
 
        """Initialise les variables et les entrys et label pour afficher Specialite,Commune,Concours,Alternane 
           Et les elements 
                                                                         """
        self.affichage=('Specialité :','Commune :','Concours:','Alternance')
        self.var_affichage=[StringVar(self.root) for aff in range(len(self.affichage))]
        self.labels_affichage= [ Label(self.root, text=aff) for aff in self.affichage ] 
        self.ccs,self.ccp=model.renvoie_coefficient()
        
        """Initalise les listes en utilisant les fonction du fichier model.py"""
        self.colonne_table=(("Nom","Specialite"),("Commune","EcoleS"),("Admission","EcoleS"),("Alternance","EcoleSpe"))
        self.information_desirer=[model.renvoie_information(self.colonne_table[i][0],self.colonne_table[i][1]) for i in range(len(self.colonne_table))]

        """Permet d'afficher toutes les ecoles contenue dans la base de données"""
        
        textaffiche=""
        self.listeecoles=list(set(model.filtre(None,None,None,None,None,299999)))
        for texteaafficher in range(len(self.listeecoles)):
            textaffiche=textaffiche+"\n"+self.listeecoles[texteaafficher][0]+" "+self.listeecoles[texteaafficher][1]+" "+self.listeecoles[texteaafficher][2]
        self.entry_ecole.insert(0.0,textaffiche)
         
        """Pour eviter d'écrire dans le champs Ecole"""
        self.entry_ecole.configure(state="disabled")
         
        """On affiche les cases a cocher"""
        for specialite in range(len(self.information_desirer[0])):
            Radiobutton(self.root,variable=self.var_affichage[0],text=self.information_desirer[0][specialite], value=self.information_desirer[0][specialite],command=self.AffichageEcole).grid(row=specialite+1, column=2,sticky="w")
        
        for commune in range(len(self.information_desirer[1])):
            Radiobutton(self.root,variable=self.var_affichage[1],text=self.information_desirer[1][commune], value=self.information_desirer[1][commune],command=self.AffichageEcole).grid(row=commune+1, column=3,sticky="w")
        for concours in range(len(self.information_desirer[2])):
            Radiobutton(self.root,variable=self.var_affichage[2],text=self.information_desirer[2][concours], value=self.information_desirer[2][concours],command=self.AffichageEcole).grid(row=concours+1, column=4,sticky="w")
        for alternance in range(len(self.information_desirer[3])):
            Radiobutton(self.root,variable=self.var_affichage[3],text=self.information_desirer[3][alternance], value=self.information_desirer[3][alternance],command=self.AffichageEcole).grid(row=alternance+1, column=5,sticky="w")
            
        """On place les élèments """
        for i, lab in enumerate(self.labels_matiere):
            lab.grid(row=i*2, column=1)
        for i,lab in enumerate(self.labels_affichage):
            lab.grid(row=0 ,column=i+2)
        for i, entry in enumerate(self.entries_matiere):
            entry.grid(row=i*2+1, column=1)
 
        self.entry_ecole.grid(row=1, rowspan=8,column=10) 
        Label(self.root,text='Ecole:').grid(row=0,column=10)
        
        self.root.mainloop()
 
    def callback(self, value_if_allowed, text):
        """Gerer tous les types de notes pour avoir le bon nombre de décimales dans les notes"""
        if text=="²":
            return False
        elif value_if_allowed.replace(".", "", 1).isdigit() and float(value_if_allowed)<=20.00 or value_if_allowed == "":
            try :
                if value_if_allowed[2]=="." and len(value_if_allowed)<6 :
                    return True
                elif value_if_allowed[1]=="." and len(value_if_allowed)<5 :
                    return True
                else:
                    return False
            except IndexError:
                return True
        return False
    
    def Ecole(self,listenote,dictonnaire,choix_specialite,choix_commune,choix_concours,choix_alternance):
        for note in range(len(listenote)):
                for cle in dictonnaire:
                    self.listeecoles=self.listeecoles+model.filtre(choix_specialite,choix_commune,choix_concours,choix_alternance,cle,listenote[note])
        return self.listeecoles
        
    def AffichageEcole(self):
        """Recuperer les variables entrée par l'utilisateur"""
        self.listeecoles=[]
        textaffiche="" 
        matiere=[self.entries_matiere[0].get()+self.entries_matiere[2].get()]+[self.entries_matiere[i].get() for i in range(len(self.entries_matiere))]
        zeropossible=("0","00.00","0.","00","00.0","0.0","0.00","00.")
        
        """Active le champs Ecole et supprime ce qu'il y avait écrit avant"""
        self.entry_ecole.configure(state="normal")
        self.entry_ecole.delete(0.7,'end');
        
        """Pour éviter les erreurs dans la console python"""
        
        for zero in range (len(zeropossible)):
            if zeropossible[zero] in matiere :
                self.entry_ecole.insert(0.0,"Soit pas aussi pessimiste")
                self.entry_ecole.configure(state="disabled")
                return
                
        if "" in matiere : 
            matiere=[20 for i in range (len(matiere))]
            
        else:
            matiere=[(float(self.entries_matiere[0].get())+float(self.entries_matiere[2].get()))/2]+[float(self.entries_matiere[i].get()) for i in range(len(self.entries_matiere))]
        """Boucles pour avoir les parametres choisi par l'utilisateur pour les mettres dans la fonction filtre """  
        noteccp=[model.NoteCoefficient(self.ccp[cle],matiere) for cle in self.ccp]
        noteccs=[model.NoteCoefficient(self.ccs[cle],matiere) for cle in self.ccs]
        
        if self.var_affichage[0].get()=="":
            choix_specialite=None
        else:
            choix_specialite=self.information_desirer[0].index(self.var_affichage[0].get())+1
            
        if self.var_affichage[1].get() not in self.information_desirer[1] or self.var_affichage[1].get()=="Peu importe":
            choix_commune=None
        else :
            choix_commune=self.var_affichage[1].get()
        
        if self.var_affichage[2].get() not in self.information_desirer[2] or self.var_affichage[2].get()=="Peu importe":
            choix_concours=None
        else :
            choix_concours=self.var_affichage[2].get()
            
        if self.var_affichage[3].get() not in self.information_desirer[3] or self.var_affichage[3].get()=="Peu importe":
            choix_alternance=None
        else :
            choix_alternance=self.var_affichage[3].get()
        
        
        if choix_concours=="CCS":
            self.listeecoles=list(set(self.Ecole(noteccs,self.ccs,choix_specialite,choix_commune,choix_concours,choix_alternance)))
        elif choix_concours=="CCP":
            self.listeecoles=list(set(self.Ecole(noteccp,self.ccp,choix_specialite,choix_commune,choix_concours,choix_alternance)))
        else:
            self.listeecoles=list(set(self.Ecole(noteccp,self.ccp,choix_specialite,choix_commune,choix_concours,choix_alternance)+self.Ecole(noteccs,self.ccs,choix_specialite,choix_commune,choix_concours,choix_alternance)))
 
            
        """Permet de génerer le texte affiché"""
        for texteaafficher in range(len(self.listeecoles)):
            textaffiche=textaffiche+"\n"+self.listeecoles[texteaafficher][0]+" "+self.listeecoles[texteaafficher][1]+" "+self.listeecoles[texteaafficher][2]
           
        """Affiche le texte et evite de pouvoir écrire par dessus"""  
        self.entry_ecole.insert(0.0,textaffiche)
        self.entry_ecole.configure(state="disabled")
         
if __name__ == '__main__':
    ChoixEcole()