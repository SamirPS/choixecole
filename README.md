Le projet ChoixEcole vous renvoie les écoles accessibles pour vous en fonction de vos choix et notes voici un petit tutoriel pour utiliser le programme (il faut lancer le fichier view.py qui est l'interface graphique !!!):

les 3 fichiers doivent être dans le même dossier .

!!!Si tout les champs groupe de EcoleS le programme affichera aucune école vous devez remplir ce champ en lisant la suite !!!

1)Rentrer vos notes

2)Choisir la Spécialité ou peu importe

3)Choisir une region ou peu importe

4)Choisir un concours ou peu importe

5)De mếme pour l'alternance

Si vous changez les notes vous devez cocher un button (en dessous de Spécialité,Commune,Concours,Alternance) pour mettre a jour la liste des écoles.

Le programme en ayant vos notes et vos choix va vous afficher dans la zone de texte à droite les écoles où vous serez éligible .Maintenant je vais vous expliquer comment ajouter une école ou une spécialité :

École : Ajouter une entrée dans la table École et remplissez tous les champs. Points est la barre d'admissibilité et le groupe est pour avoir les bons coefficient choisissez un nom disponible dans la table coefficient .Pour l'afficher dans le programme il faut créer un couple unique dans la table EcoleSpe compose de l'id de l'école, l'id de la spécialité et celui de l'alternance .

Coefficient : Changer les coefficients depuis la table coefficient,ajouter un nouveau groupe en remplissant tout les champs.

Spécialité : Ajouter une nouvelle entrée et mettez le nom de votre spécialité l'id à gauche est celui à mettre dans idspé dans la table EcoleSpe.

Vous pouvez gérer la base de données grâce à Sqlite Browser,Vous avez des exemples dans la base de données au cas ou .

Remarque que vous avez fait :

On peut maintenant mettre que des chiffres dans les entrys grâce à la fonction callback qui gère tout les types de note. La fonction filtre a été modifié et n'a plus de redondance ainsi que les fonctions renvoie_specialite,renvoie_alternance et autre qui ont été factorisés en une seule fonction car dans chaque fonction on récuperai juste le premier objet du tuple.J'ai aussi changer la table coeffccp et coeffccs dans la base de donnéées en coefficient afin de gérer grâce a des dictionnaire les différents concours,banque de note et points de bonification propre a chaque groupe.Pour les dossiers je suis en train de chercher les coefficient sur internet.Et on peut maintenant avoir plusieurs concours exemple des groupes de CCP,CCS,ATS ou autre .
