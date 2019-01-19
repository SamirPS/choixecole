#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:59:28 2018
@author: samir
"""
from tkinter import Tk,StringVar, Label,Entry,Listbox,Menu,filedialog
from fpdf import FPDF
import model
import tkinter.scrolledtext as tkscrolled

class ChoixEcole:
    def __init__(self):
        
        # Initialise l'application et change le titre et la positionne
        self.root = Tk()
        self.root.title("ChoixEcole")
        self.root.resizable(False, False)
        
        #Ajoute un Menu pour sauvegarder les fichiers 
        
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        menufichier = Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Fichier", menu=menufichier) 
        menufichier.add_command(label="Enregistrer ",command=self.save_file)
        menufichier.add_command(label="Enregistrer sous",command=self.save_file_as)
        self.filename =() 
        
        self.ecolepdf=[]
        # Initialise le widget de rendu
        self.entry_ecole = tkscrolled.ScrolledText(self.root, width=30, height=10,)
       
        ########################################################################
        #                        NOTES                                         #
        ########################################################################
        # On considère les notes entrées par l'utilisateur (sous forme de 
        # "StringVar"). À chaque modification d'une de ces variables, on met
        # tout à jour.

        self.notes_vars = {
            "maths": StringVar(self.root),
            "physique": StringVar(self.root),
            "si":StringVar(self.root),
            "informatique":StringVar(self.root),
            "anglais":StringVar(self.root),
            "francais":StringVar(self.root)
            }
       
        for var in self.notes_vars.values():
            var.trace('w', self.update)

        # self.notes représente soit une erreur de saisie des notes (avec None)
        # soit un dictionnaire "matière -> note(float)".
        self.notes = None
       

        ########################################################################
        #                        CHOIX                                         #
        ########################################################################
        # On crée un dictonnaire modifié a chaque clique sur la ListeBox.
        
        self.choix = {
            "Region": None,
            "Specialite": None,
            "Alternance": None,
            "Concours": None,
            "Année":None
        }
        
        
        ########################################################################
        #                 RENDU FORMULAIRE NOTES                               #
        ########################################################################
        
        Label(
            self.root,
            text="Moyenne en maths"
        ).grid(row=1, column=1)
        Entry(
            self.root,
            textvariable=self.notes_vars["maths"]
        ).grid(row=2, column=1)

        Label(
            self.root,
            text="Moyenne en Physique"
        ).grid(row=3, column=1)
        Entry(
            self.root,
            textvariable=self.notes_vars["physique"]
        ).grid(row=4, column=1)
        
        Label(
            self.root,
            text="Moyenne en Si"
        ).grid(row=5, column=1)
        Entry(
            self.root,
            textvariable=self.notes_vars["si"]
        ).grid(row=6, column=1)
        
        Label(
            self.root,
            text="Moyenne en Informatique"
        ).grid(row=7, column=1)
        Entry(
            self.root,
            textvariable=self.notes_vars["informatique"]
        ).grid(row=8, column=1)
        
        Label(
            self.root,
            text="Moyenne en Anglais"
        ).grid(row=9, column=1)
        Entry(
            self.root,
            textvariable=self.notes_vars["anglais"]
        ).grid(row=10, column=1)
        
        Label(
            self.root,
            text="Moyenne en Francais"
        ).grid(row=11, column=1)
        Entry(
            self.root,
            textvariable=self.notes_vars["francais"]
        ).grid(row=12, column=1)
       
         ########################################################################
        #                 RENDU FORMULAIRE choix                               #
        ########################################################################
        self.specialite=Listbox(
                self.root,
                selectmode='multiple',
                exportselection=0, 
                width=20, 
                height=10)
        Label(
            self.root,
            text="Specialite"
        ).grid(row=0, column=6)
        
        self.Region=Listbox(
                self.root,
                selectmode='multiple',
                exportselection=0, 
                width=20, 
                height=10)
        Label(
            self.root,
            text="Region"
        ).grid(row=0, column=7)
        
        self.Alternance=Listbox(
                self.root,
                selectmode='multiple',
                exportselection=0, 
                width=20, 
                height=10)
        Label(
            self.root,
            text="Alternance"
        ).grid(row=0, column=8)
        
        self.Concours=Listbox(
                self.root,
                selectmode='multiple',
                exportselection=0, 
                width=20, 
                height=10)
        Label(
            self.root,
            text="Admission"
        ).grid(row=0, column=9)
        
        self.Année=Listbox(
                self.root,
                exportselection=0, 
                width=20, 
                height=10)
        Label(
            self.root,
            text="Année"
        ).grid(row=0, column=10)
        
        self.specialite.grid(
                row=1,
                column=6,
                rowspan=10,
                padx=10)
        self.Region.grid(
                row=1,
                column=7,
                rowspan=10,
                padx=10)
        self.Alternance.grid(
                row=1,
                column=8,
                rowspan=10,
                padx=10)
        self.Concours.grid(
                row=1,
                column=9,
                rowspan=10,
                padx=10)
        self.Année.grid(
                row=1,
                column=10,
                rowspan=10,
                padx=10)
        
        
        
         ########################################################################
        #                 Insertion des données                               #
        ########################################################################
        for specialite in model.renvoie_specialites():
                self.specialite.insert("end",specialite)
        
        for Region in model.renvoie_regions():
            self.Region.insert("end",Region)
        
        for Alternance in ["Peu importe","Oui","Non"]:
             self.Alternance.insert("end",Alternance)
        
        for Concours in model.renvoie_admission():
            self.Concours.insert("end",Concours)
        
        for annee in ["3/2","5/2"]:
             self.Année.insert("end",annee)
        
         ########################################################################
        #                 On bind les ListBox                            #
        ########################################################################
        self.specialite.bind("<<ListboxSelect>>",self.update)
        self.Region.bind("<<ListboxSelect>>",self.update)
        self.Alternance.bind("<<ListboxSelect>>",self.update)
        self.Concours.bind("<<ListboxSelect>>",self.update)
        self.Année.bind("<<ListboxSelect>>",self.update)
        


        self.entry_ecole.grid(row=1,column=20,rowspan=10) 
        
        self.update()
        self.root.mainloop()

    def valide_maj_notes(self):
        try:
            notes = {}
            for nom_matiere, note_var in self.notes_vars.items():
                note_float = float(note_var.get())
                if note_float > 20 or note_float < 0:
                    raise ValueError()
                else:
                	if len(str(note_float))>1:
                		if str(note_float)[2]=="." and len(str(note_float))<6:
                			pass
                		elif str(note_float)[1]=="." and len(str(note_float))<5:
                			pass
                		else:
                			raise ValueError()

                notes[nom_matiere] = note_float
            notes["modelisation"]=(notes["maths"]+notes["si"])/2
            self.notes = notes
        except IndexError:
        	pass
        except ValueError:
            # Une erreur est survenue lors de la conversion des notes
            self.notes = None

    def maj_choix(self):
        ########################################################################
        #                        NOTES                                         #
        ########################################################################
        # On récuperer l'index de la spécialite et les autres variables
        # Et en fonction de certains cas on dit que self.choix=None
        
        self.choix={"Specialite":self.specialite.curselection(),
                    "Region":tuple(self.Region.get(i) for i in self.Region.curselection()),
                    "Concours":tuple(self.Concours.get(i) for i in self.Concours.curselection()),
                    "Alternance":tuple(self.Alternance.get(i) for i in self.Alternance.curselection()),
                    "Année":tuple(self.Année.get(i) for i in self.Année.curselection())}
        
        for cle in self.choix:
            if self.choix[cle]==() or 0 in self.choix[cle] or "Peu importe" in self.choix[cle]:
                self.choix[cle]=None
                   
        
    def update(self, *inutile):
        self.valide_maj_notes()
        self.maj_choix()
        self.affichage()
    
    
    def convertpdf(self):
            """Converti en PDF """   
            try:
                pdf=FPDF()
                pdf.add_page()
                pdf.set_font("Arial",size=12)
                admission,listeecoles=self.returntext()
                for texteaafficher in range(len(admission)):
                    pdf.cell(200,10,txt=listeecoles[texteaafficher][0]+" "*15+admission[texteaafficher] ,ln=1,align="L")
                pdf.output(self.filename)
            except TypeError:
                return
        
    def returntext(self):
        """Affiche le nom de l'école et a cote Refuse ou admis"""
        listeecoles=list(set(model.filtre({choix:None for choix in self.choix},None,None)))
        admission=["Admis"]*len(listeecoles)
        for i in range(len(listeecoles)):
            if listeecoles[i] not in self.ecolepdf  :
                admission[i]="Refuse"
        return admission,listeecoles
      
    def save_file(self, whatever = None):
        if (self.filename ==()):
            self.save_file_as()
        self.convertpdf()

    def save_file_as(self, whatever = None):
        self.filename =filedialog.asksaveasfilename(defaultextension='.pdf',
                                                             filetypes = [
        ('PDF', '*.pdf'),

            ])
   
        self.convertpdf()
        
    def affichage(self):
        # Active le champs Ecole et supprime ce qu'il y avait écrit avant
        self.entry_ecole.configure(state="normal")
        self.entry_ecole.delete(0.7,'end')
        text_affiche = "" 
        self.ecolepdf=[]
        
        
        if self.notes == None:
            text_affiche = "Erreur lors de la saisie des notes."
            
        else:
            
            notecoefficient=model.NoteCoefficient(self.notes,self.choix["Année"])
            for nom in notecoefficient:
                for cle in notecoefficient[nom]:
                    ecoles = model.filtre(self.choix, cle, notecoefficient[nom][cle])
                    self.ecolepdf+=model.filtre({choix:None for choix in self.choix},cle,notecoefficient[nom][cle])
                    
                    for ecole in ecoles:
                        text_affiche += (
                            "\n" 
                            + ecole[0] + " "
                            + ecole[1] + " "
                            + ecole[2]
                        )
                   

        self.entry_ecole.insert(0.7, text_affiche)
        self.entry_ecole.configure(state="disabled")


if __name__ == '__main__':
    ChoixEcole()