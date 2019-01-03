Le projet ChoixEcole vous renvoie les écoles accesible pour vous en fonction de vos choix et notes voici un petit tutoriel pour utiliser le programme :


1)Rentrer vos notes


2)Choisir la Spécialite si vous savez pas laissez vide


3)Choisir une commune ou peu importe


4)Choisir un concours ou peu importe 


5) De mếme pour l'alternance



Le programme en ayant vos notes et vos choix va vous afficher dans la zone de texte a droite les écoles ou vous serez éligible .


Maintenant je vais vous expliquer comment ajouter une école ou une spécialite:
Ecole: Ajouter une entrée dans la table Ecole et remplissez tous les champs. Points est 
la barre d'admissibilité et le groupe est pour avoir les bon coefficient choissiez un nom disponible dans la table coefficient .Pour l'affichier dans le programme  il faut créer un couple unique dans la table EcoleSpe compose de l'id de l'école,l'id de la spécialite et celui de l'alternance .
Spécialite :
Ajouter une nouvelle entrée et mettez le nom de votre spécialité l'id a gauche est celui a mettre dans id spé dans la table EcoleSpe.

Vous pouvez gérer la base de données grace a Sqlite Browser

Vous avez des exemples dans la base de données au cas ou .

Remarque :

On peut maintenant mettre que des chiffres dans les entrys grace a la fonction callback qui gére tout type des note.La fonction filtre a été modifié et n'as pas de redondance ainsi que les fonctions renvoiespecialite,renvoiealternance et autre qui ont été factorisé en une seule fonction.
