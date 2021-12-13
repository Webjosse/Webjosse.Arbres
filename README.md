# [FR] IUT - Algorithmique Avancé: Entrainement
Ce projet représente des structures de données de type:
* Arbre
* ABR
* (Peut-être AVL dans un futur plus ou moins proche, selon la demande)

**À exécuter depuis l'IDLE Python** (testé sur 3.10)

## Fonctions de l'arbre

Constructeur: `Arbre(val)`

Fonctions sans argument qui ne changent pas l'arbre: `prefixe_afficher`, `infixe_afficher`, `suffixe_afficher`, `niveau_afficher`, `minimum`, `afficher_arbre`

à noter que `afficher_arbre` est moche

`miroir()` → miroir de l'arbre

`recherche(val)` → renvoie True si val trouvée, False sinon

## Fonctions de l'ABR

* Constructeur: `ABR(liste_val)` → plante les valeurs dans l'ordre

* `recherche(val)` plus performant

* `planter(val)`→ ajoute val à l'arbre

* `supprimer(val)`→ supprime val de l'arbre

## Mode Navigateur

* Pour voir sur navigateur il faut installer flask: `python -m pip install flask` 

* Ensuite vous faites `voir(a)` et allez sur votre navigateur `http://localhost:5000/`
Normalement l'arbre s'affiche

* Pour stopper le serveur Web, un petit Ctrl+C
