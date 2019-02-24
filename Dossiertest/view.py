#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:59:28 2018
@author: samir
"""
from tkinter import Tk, StringVar, Label, Entry, Listbox, IntVar, Checkbutton, Button, Toplevel
import model
import tkinter.scrolledtext as tkscrolled

class ChoixEcole:
    def __init__(self):

        # Initialise l'application et change le titre et la positionne
        self.root = Tk()
        self.root.title("ChoixEcole")
        self.root.resizable(False, False)
        self.entry_ecole = tkscrolled.ScrolledText(self.root, width=40, height=10, )


        self.button=[]

        self.ecolesselect={}

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
            "regions": None,
            "specialites": None,
            "alternance": None,
            "concours": None,
            "annee":None
        }
        
        self.varsbuttons={
                "specialites":IntVar(self.root),
                "regions":IntVar(self.root),
                "concours":IntVar(self.root),
                "alternance":IntVar(self.root),
                "annee":IntVar(self.root),
                "ecole":IntVar(self.root)
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
        self.specialites=Listbox(
                self.root,
                selectmode='multiple',
                exportselection=0,
                width=20,
                height=10)
        Label(
            self.root,
            text="Specialite"
        ).grid(row=0, column=6)


        
        self.specialites=Listbox(
                self.root,
                selectmode='multiple',
                exportselection=0,
                width=20,
                height=10)
        Label(
            self.root,
            text="Specialite"
        ).grid(row=0, column=6)
        self.regions=Listbox(
                self.root,
                selectmode='multiple',
                exportselection=0,
                width=20,
                height=10)
        Label(
            self.root,
            text="Region"
        ).grid(row=0, column=7)

        self.alternance=Listbox(
                self.root,
                selectmode='multiple',
                exportselection=0,
                width=20,
                height=10)
        Label(
            self.root,
            text="Alternance"
        ).grid(row=0, column=8)

        self.concours=Listbox(
                self.root,
                selectmode='multiple',
                exportselection=0,
                width=20,
                height=10)
        Label(
            self.root,
            text="Admission"
        ).grid(row=0, column=9)

        self.annee=Listbox(
                self.root,
                exportselection=0,
                width=20,
                height=10)
        Label(
            self.root,
            text="Année"
        ).grid(row=0, column=10)

        self.specialites.grid(
                row=2,
                column=6,
                rowspan=10,
                padx=10)
        

        self.regions.grid(
                row=2,
                column=7,
                rowspan=10,
                padx=10)

        self.alternance.grid(
                row=2,
                column=8,
                rowspan=10,
                padx=10)

        self.concours.grid(
                row=2,
                column=9,
                rowspan=10,
                padx=10)

        self.annee.grid(
                row=2,
                column=10,
                rowspan=10,
                padx=10)

        ########################################################################
        #                 Insertion des Bouton Peu importe                     #
        ########################################################################

        Checkbutton(self.root,
                    variable=self.varsbuttons["specialites"],
                    text="Peu importe",
                    command=self.update).grid(row=1,
                                       column=6)

        Checkbutton(self.root,
                     variable=self.varsbuttons["regions"],
                     text="Peu importe",
                     command=self.update).grid(row=1,
                                   column=7)


        Checkbutton(self.root,
                    variable=self.varsbuttons["alternance"],
                    text="Peu importe",
                    command=self.update).grid(row=1,
                                   column=8)

        Checkbutton(self.root,
                    variable=self.varsbuttons["concours"],
                    text="Peu importe",
                    command=self.update).grid(row=1,
                                   column=9)

        Button(self.root,
                    text="Plus d'information",
                    command=self.information).grid(row=2,
                                              column=31)

         ########################################################################
        #                 Insertion des données                               #
        ########################################################################
        for specialite in model.renvoie_specialites():
            self.specialites.insert("end",specialite)

        for region in model.renvoie_regions():
            self.regions.insert("end",region)

        for alternance in ["Oui","Non"]:
             self.alternance.insert("end",alternance)

        for concours in model.renvoie_admission():
            self.concours.insert("end",concours)

        for annee in ["3/2","5/2"]:
             self.annee.insert("end",annee)

         ########################################################################
        #                 On bind les ListBox                            #
        ########################################################################
        self.entry_ecole.grid(row=2, column=20, rowspan=10)

        self.specialites.bind("<<ListboxSelect>>",self.update)
        self.regions.bind("<<ListboxSelect>>",self.update)
        self.alternance.bind("<<ListboxSelect>>",self.update)
        self.concours.bind("<<ListboxSelect>>",self.update)
        self.annee.bind("<<ListboxSelect>>",self.update)
       
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
                    if len(note_var.get()) in (2,1)  :
                        pass
                    elif note_var.get()[2]=="." and len(note_var.get())<6:
                        pass
                    elif note_var.get()[1]=="." and len(note_var.get())<5:
                        pass
                    else :
                        raise ValueError 

                notes[nom_matiere] = note_float
            notes["modelisation"]=(notes["maths"]+notes["si"])/2
            self.notes = notes

        except ValueError:
            # Une erreur est survenue lors de la conversion des notes
            self.notes = None
        
    def maj_choix(self):
        ########################################################################
        #                        NOTES                                         #
        ########################################################################
        # On récupere l'index de la spécialite et le texte coché pour les autres variables
        # Et en fonction de certains cas on dit que self.choix=None

        self.choix={"specialites":model.renvoie_idspe(self.specialites.get(i) for i in self.specialites.curselection()),
                    "regions":tuple(self.regions.get(i) for i in self.regions.curselection()),
                    "concours":tuple(self.concours.get(i) for i in self.concours.curselection()),
                    "alternance":tuple(self.alternance.get(i) for i in self.alternance.curselection()),
                    "annee":tuple(self.annee.get(i) for i in self.annee.curselection())}

        if self.varsbuttons["specialites"].get()==1:
            self.specialites.selection_clear(0,"end")
        if self.varsbuttons["regions"].get()==1:
            self.regions.selection_clear(0,"end")
        if self.varsbuttons["concours"].get()==1:
            self.concours.selection_clear(0,"end")
        if self.varsbuttons["alternance"].get()==1:
            self.alternance.selection_clear(0,"end")

        for cle in self.choix:
            if not self.choix[cle] or self.varsbuttons[cle].get()==1:
                self.choix[cle]=None

    def update(self, *inutile):

        self.valide_maj_notes()
        self.maj_choix()
        self.construit_ecoles()
        self.affichage()

    def construit_ecoles(self):
        self.ecolesselect={}
         
        if self.notes!=None:
            for j,ecoles in enumerate(model.filtre(self.choix,self.notes)) :

                self.ecolesselect[j]={
                    "var":IntVar(self.root),
                    "id":ecoles[0],
                    "nom":ecoles[1],
                    "admission":ecoles[2],
                    "region":ecoles[3],
                    "Alternance":ecoles[4],
                    "Acronyme":ecoles[5],
                    "Spe":ecoles[6]
                }

    def information(self):

        window = Toplevel(self.root)
        info = tkscrolled.ScrolledText(window, width=90, height=10)
        info.grid(row=2,column=10)
        text_affiche=""

        for ecole in self.ecolesselect.values():
            if ecole["var"].get()==1:
                samir=ecole["nom"]+ " Alternance " +ecole[ "Alternance" ]

                if self.choix["specialites"]==None:

                    for ecolesinfo in self.ecolesselect.values():
                        if samir==ecolesinfo["nom"]+" Alternance " +ecolesinfo[ "Alternance" ]:

                            text_affiche+=(
                                    ecolesinfo["nom"]
                                    +" Admission : "
                                    +ecolesinfo["admission"]
                                    +" Region : "
                                    +ecolesinfo["region"]
                                    +" Alternance : "
                                    +ecolesinfo["Alternance"]
                                    +" Specialite : "
                                    +ecolesinfo["Spe"]
                                    +"\n"
                            )
                else :
                    text_affiche = (
                            ecole[ "nom" ]
                            + " Admission : "
                            + ecole[ "admission" ]
                            + " Region : "
                            + ecole[ "region" ]
                            + " Alternance : "
                            + ecole[ "Alternance" ]
                            + " Specialite : "
                            + ecole[ "Spe" ]
                            + "\n"
                    )

                info.insert(0.7, text_affiche)
        info.configure(state="disabled")


    def affichage(self):
        for i in self.button:
            i.destroy()

        self.entry_ecole.configure(state="normal")
        self.entry_ecole.delete(0.7, 'end')
        textverification = ""

        if self.notes :
            for ecole in self.ecolesselect.values():
                text_affiche = (
                        ecole[ "Acronyme" ]
                        + " Alternance " +
                        ecole[ "Alternance" ]
                )
                if text_affiche not in textverification:

                    check = Checkbutton(text=text_affiche,variable=ecole["var"])
                    self.entry_ecole.window_create(0.7,window=check)
                    self.entry_ecole.insert(0.7, "\n")
                    self.button.append(check)
                    textverification += text_affiche
        else :
            text_affiche = "Erreur lors de la saisie des notes."
            self.entry_ecole.insert(0.7,text_affiche)


        self.entry_ecole.configure(state="disabled")


if __name__ == '__main__':
    ChoixEcole()
