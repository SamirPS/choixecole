#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:59:28 2018
@author: samir
"""
from tkinter import (
    Tk,
    StringVar,
    Label,
    Entry,
    Listbox,
    IntVar,
    Checkbutton,
    Button,
    Toplevel,
    Scale,
    filedialog,
    Scrollbar,
    Canvas,
    Frame,
    Menu,
)
import model
import tkinter.scrolledtext as tkscrolled
from fpdf import FPDF


class ChoixEcole:
    def __init__(self):

        # Initialise l'application change le titre et la positionne
        self.root = Tk()
        self.root.title("ChoixEcole")

        """Ouvre la base de données"""

        basededonne = filedialog.askopenfilename(
            title="Ouvrir un fichier", filetypes=[("db file", ".db")]
        )
        model.connec(basededonne)

        """Ajoute un menu"""
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        menufichier = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Fichier", menu=menufichier)
        menufichier.add_command(label="Enregistrer ", command=self.save_file)
        menufichier.add_command(label="Enregistrer sous", command=self.save_file_as)
        self.filename = ()

        self.root.resizable(False, False)
        self.entry_ecole = tkscrolled.ScrolledText(self.root, width=40, height=10,)

        self.button = []
        self.ecolesselect = {}

        ########################################################################
        #                        NOTES                                         #
        ########################################################################
        # On considère les notes entrées par l'utilisateur (sous forme de
        # "StringVar"). À chaque modification d'une de ces variables, on met
        # tout à jour.

        self.notes_vars = {
            "maths": StringVar(self.root),
            "physique": StringVar(self.root),
            "si": StringVar(self.root),
            "informatique": StringVar(self.root),
            "anglais": StringVar(self.root),
            "francais": StringVar(self.root),
        }

        for var in self.notes_vars.values():
            var.trace("w", self.update)

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
            "annee": None,
        }

        self.varsbuttons = {
            "specialites": IntVar(self.root),
            "regions": IntVar(self.root),
            "concours": IntVar(self.root),
            "alternance": IntVar(self.root),
            "annee": IntVar(self.root),
            "ecole": IntVar(self.root),
        }

        ########################################################################
        #                 RENDU FORMULAIRE NOTES                               #
        ########################################################################

        self.scale = Scale(
            self.root,
            orient="horizontal",
            from_=0,
            to=100,
            resolution=1,
            tickinterval=25,
            length=100,
            label="Augmentation %",
            command=self.update,
        )

        Label(self.root, text="Maths").grid(row=2, column=1)
        Entry(self.root, textvariable=self.notes_vars["maths"]).grid(row=3, column=1)

        Label(self.root, text="Physique").grid(row=4, column=1)
        Entry(self.root, textvariable=self.notes_vars["physique"]).grid(row=5, column=1)

        Label(self.root, text="Si").grid(row=6, column=1)
        Entry(self.root, textvariable=self.notes_vars["si"]).grid(row=7, column=1)

        Label(self.root, text="Informatique").grid(row=8, column=1)
        Entry(self.root, textvariable=self.notes_vars["informatique"]).grid(
            row=9, column=1
        )

        Label(self.root, text="Anglais").grid(row=10, column=1)
        Entry(self.root, textvariable=self.notes_vars["anglais"]).grid(row=11, column=1)

        Label(self.root, text="  Francais").grid(row=12, column=1)
        Entry(self.root, textvariable=self.notes_vars["francais"]).grid(
            row=13, column=1
        )

        ########################################################################
        #                 RENDU FORMULAIRE choix                               #
        ########################################################################
        self.specialites = Listbox(
            self.root, selectmode="multiple", exportselection=0, width=20, height=10
        )
        Label(self.root, text="Specialite").grid(row=0, column=6)

        self.specialites = Listbox(
            self.root, selectmode="multiple", exportselection=0, width=20, height=10
        )
        Label(self.root, text="Specialite").grid(row=0, column=6)

        self.regions = Listbox(
            self.root, selectmode="multiple", exportselection=0, width=20, height=10
        )
        Label(self.root, text="Region").grid(row=0, column=7)

        self.alternance = Listbox(self.root, exportselection=0, width=6, height=3)
        Label(self.root, text="Alternance").grid(row=11, column=6)

        self.concours = Listbox(
            self.root, selectmode="multiple", exportselection=0, width=20, height=10
        )
        Label(self.root, text="Admission").grid(row=0, column=9)

        self.annee = Listbox(self.root, exportselection=0, width=6, height=3)
        Label(self.root, text="Année").grid(row=11, column=7)

        self.specialites.grid(row=2, column=6, rowspan=10, padx=10)

        self.regions.grid(row=2, column=7, rowspan=10, padx=10)

        self.alternance.grid(row=13, column=6, rowspan=10, padx=10)

        self.concours.grid(row=2, column=9, rowspan=10, padx=10)

        self.annee.grid(row=13, column=7, rowspan=10, padx=10)

        ########################################################################
        #                 Insertion des Bouton Peu importe                     #
        ########################################################################

        Checkbutton(
            self.root,
            variable=self.varsbuttons["specialites"],
            text="Peu importe",
            command=self.update,
        ).grid(row=1, column=6)

        Checkbutton(
            self.root,
            variable=self.varsbuttons["regions"],
            text="Peu importe",
            command=self.update,
        ).grid(row=1, column=7)

        Checkbutton(
            self.root,
            variable=self.varsbuttons["alternance"],
            text="Peu importe",
            command=self.update,
        ).grid(row=12, column=6)

        Checkbutton(
            self.root,
            variable=self.varsbuttons["concours"],
            text="Peu importe",
            command=self.update,
        ).grid(row=1, column=9)

        Button(
            self.root, text="Plus d'information", command=self.information, width=15
        ).grid(row=2, column=31)

        Button(self.root, text="Prix", command=self.calculprix, width=15).grid(
            row=2, column=32
        )

        ########################################################################
        #                 Insertion des données                                #
        ########################################################################
        for specialite in model.renvoie_specialites():
            self.specialites.insert("end", specialite)

        for region in model.renvoie_regions():
            self.regions.insert("end", region)

        for alternance in ["Oui", "Non"]:
            self.alternance.insert("end", alternance)

        for concours in model.renvoie_admission():
            self.concours.insert("end", concours)

        for annee in ["3/2", "5/2"]:
            self.annee.insert("end", annee)

        ########################################################################
        #                 On bind les ListBox                                  #
        ########################################################################
        self.entry_ecole.grid(row=2, column=20, rowspan=10)
        self.scale.grid(row=0, column=1, rowspan=2)

        self.specialites.bind("<<ListboxSelect>>", self.update)
        self.regions.bind("<<ListboxSelect>>", self.update)
        self.alternance.bind("<<ListboxSelect>>", self.update)
        self.concours.bind("<<ListboxSelect>>", self.update)
        self.annee.bind("<<ListboxSelect>>", self.update)

        self.update()
        self.root.mainloop()

    def valide_maj_notes(self):
        ########################################################################
        #                        NOTES                                         #
        ########################################################################
        # On récupere la note entrée et on la vérifie

        try:
            notes = {}
            
            for nom_matiere, note_var in self.notes_vars.items():
                note_float = float(note_var.get())
                if note_float > 20 or note_float < 0:
                    raise ValueError()

                else:
                    if len(note_var.get()) in (2, 1):
                        pass
                    elif note_var.get()[2] == "." and len(note_var.get()) < 6:
                        pass
                    elif note_var.get()[1] == "." and len(note_var.get()) < 5:
                        pass
                    else:
                        raise ValueError

                note_float += (self.scale.get() * note_float) / 100

                if note_float >= 20:
                    notes[nom_matiere] = 20
                else:
                    notes[nom_matiere] = note_float

            notes["modelisation"] = (notes["maths"] + notes["si"]) / 2

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

        self.choix = {
            "specialites": model.renvoie_idspe(
                self.specialites.get(i) for i in self.specialites.curselection()
            ),
            "regions": tuple(self.regions.get(i) for i in self.regions.curselection()),
            "concours": tuple(
                self.concours.get(i) for i in self.concours.curselection()
            ),
            "alternance": tuple(
                self.alternance.get(i) for i in self.alternance.curselection()
            ),
            "annee": tuple(self.annee.get(i) for i in self.annee.curselection()),
        }

        for cle in self.varsbuttons:
            if self.varsbuttons[cle].get() == 1:
                eval('self.'+cle+'.selection_clear(0, "end")')
               

        for cle in self.choix:
            if not self.choix[cle] or self.varsbuttons[cle].get() == 1:
                self.choix[cle] = None

    def update(self, *inutile):

        self.valide_maj_notes()
        self.maj_choix()
        self.construit_ecoles()
        self.affichage()

    def construit_ecoles(self):
        """On récupere les écoles disponibles dans la bdd et on les stocke """
        self.ecolesselect = {}

        if self.notes != None:
            for j, ecoles in enumerate(model.filtre(self.choix, self.notes)):
                self.ecolesselect[j] = {
                    "var": IntVar(self.root),
                    "id": ecoles[0],
                    "nom": ecoles[1],
                    "admission": ecoles[2],
                    "region": ecoles[3],
                    "Alternance": ecoles[4],
                    "Acronyme": ecoles[5],
                    "Spe": ecoles[6],
                }

    def information(self):
        ########################################################################
        #                  Information                                         #
        ########################################################################
        # Renvoie les spécialite offerte par l'école en fonction du choix de l'utilisateur

        window = Toplevel(self.root)
        window.resizable(False, False)
        window.geometry("700x150")
        vsb = Scrollbar(window, orient="vertical")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb = Scrollbar(window, orient="horizontal")
        hsb.grid(row=1, column=0, sticky="ew")
        ca = Canvas(window, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        ca.grid(row=0, column=0, sticky="news")
        vsb.config(command=ca.yview)
        hsb.config(command=ca.xview)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        fr = Frame(ca)

        i=1
        for a in ["Nom","Admission","Region","Alternance","Specialite"]:
            Label(fr, text=a).grid(row=0, column=i)
            i+=2

        if self.choix["specialites"] == None:
            ListeSpe = list(self.specialites.get(0, "end"))
        else:
            ListeSpe = [
                self.specialites.get(i) for i in self.specialites.curselection()
            ]

        if self.choix["alternance"] == None:
            alternance = ["Oui", "Non"]

        else:
            alternance = [self.choix["alternance"][0]]

        ligne = 1

        for ecole in self.ecolesselect.values():

            if ecole["var"].get() == 1:

                for ecolesinfo in self.ecolesselect.values():
                    if (
                            ecole["nom"] 
                        == ecolesinfo["nom"]

                        and ecolesinfo["Alternance"] in alternance

                        and ecolesinfo["Spe"] in ListeSpe


                    ):
                        i=1
                        for texte in [ecolesinfo["nom"],ecolesinfo["admission"],ecolesinfo["region"],ecolesinfo["Alternance"],ecolesinfo["Spe"]] :
                            a = Entry(fr,width=60)
                            a.insert(0,texte)
                            a.grid(row=ligne, column=i)
                            i+=2

                            
                            
                            a.config(state="disabled")
                            

                        ligne += 1

        ca.create_window(0, 0, window=fr)
        fr.update_idletasks()
        ca.config(scrollregion=ca.bbox("all"))

    def calculprix(self):

        ecoles = []
        for ecole in self.ecolesselect.values():
            if ecole["var"].get() == 1:
                ecoles.append(ecole["admission"])

        prixboursier = str(model.prix_ecole(ecoles, "Boursier"))
        prixnonboursier = str(model.prix_ecole(ecoles, "NonBoursier"))
        Label(self.root, text="Prix Boursier \n" + prixboursier).grid(row=3, column=32)
        Label(self.root, text="Prix Non Boursier\n" + prixnonboursier).grid(
            row=4, column=32
        )

    def convertpdf(self, spacing=2):
        """Converti en PDF """

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        data = [["Nom", "Résultat"]]
        admission, listeecoles = self.returntext()

        data += [[listeecoles[i], admission[i]] for i in range(len(admission))]

        col_width = pdf.w / 2.5
        row_height = pdf.font_size
        for row in data:
            for item in row:
                pdf.cell(col_width, row_height * spacing, txt=item, border=1)
            pdf.ln(row_height * spacing)
        pdf.output(self.filename)

    def returntext(self):
        """Affiche le nom de l'école et a cote Refuse ou admis"""

        ecoleamoi = list(
            set(
                [
                    ecoles[5]
                    for ecoles in model.filtre(
                        {choix: None for choix in self.choix}, self.notes
                    )
                ]
            )
        )
        listeecoles = list(
            set(
                [
                    ecoles[5]
                    for ecoles in model.filtre(
                        {choix: None for choix in self.choix},
                        {Note: 20 for Note in self.notes},
                    )
                ]
            )
        )

        admission = ["Admis"] * len(listeecoles)

        for i in range(len(listeecoles)):
            if listeecoles[i] not in ecoleamoi:
                admission[i] = "Refuse"

        return admission, listeecoles

    def save_file(self, whatever=None):
        if self.filename == ():
            self.save_file_as()
        self.convertpdf()

    def save_file_as(self, whatever=None):
        self.filename = filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("PDF", "*.pdf"),]
        )

        self.convertpdf()

    def affichage(self):
        """Affiche les écoles auquel on est admissible """

        for i in self.button:
            i.destroy()

        self.entry_ecole.configure(state="normal")
        self.entry_ecole.delete(0.7, "end")

        if self.notes:
            textverification = []
            for ecole in self.ecolesselect.values():
                if ecole["Acronyme"] not in textverification:
                    check = Checkbutton(text=ecole["Acronyme"], variable=ecole["var"])
                    self.entry_ecole.window_create(0.7, window=check)
                    self.entry_ecole.insert(0.7, "\n")
                    self.button.append(check)
                    textverification.append(ecole["Acronyme"])
        else:

            self.entry_ecole.insert(0.7, "Erreur lors de la saisie des notes.")

        self.entry_ecole.configure(state="disabled")


if __name__ == "__main__":
    ChoixEcole()
