
En général, je me retrouve avec des notes A=>E ou ++ => -- ... Ou une note sur 20. Sur chacun des points suivants

=> Je tente de mettre des notes "a priori" + des remarques durant les deux dernières séances (en particulier la dernière) 
- je note les points de vigilance
- j'interroge les groupes sur la description des fonctionnalités et le code associé
- => Je leur dis quand je vois des choses améliorables
=> On peut donner cette grille (ou d'autres) aux étudiants en amont...

## Oral

- Fluidité, mise en scène
- Est ce que c'est convainquant?
- Est ce que c'est complet/impressionnant?
- Respect du temps (je coupe à 5'30 au pire, je considère que c'est parfait entre 4'30 et 5')
- => Je ne regarde pas la qualité du code pour cette note, on est sur la forme
- Equilibrage binome => je n'hésite pas distinguer les notes entre binôme si l'oral est asymétrique.

## Organisation du code 

- Structuration générale import => def => script
	- pas de code intermédiaire
- Les fonctions sont elles courtes, avec des arguments, avec des noms qui semblent refléter des fonctions raisonnables
- Absence mélange entre les input et les fonctions SQL (notamment les insertions) (=séparation entre récupération des infos et fct opérationnelles)
- Pas de variables globales (je suis assez sévère là-dessus, même sur le curseur)
- Pas de boucle for avec des bornes en dur (e.g. for i in range(8):)... Ca pique les yeux, sauf exception, je mets une petite pénalité

[bon niveau] Est ce que les fonctions de base sont ré-utilisées entre fonctionnalités? 
Ex: insérer un client utilisée pour la lecture de fichier + pour une fonction de saisie au clavier (mode accueil)
[opt bonus] import interne + structuration raisonnable dans le choix des fonctions mises dans les fichiers externes

## Commentaires (note souvent liée à l'organisation)

- Les fonctions et les variables ont des noms parlants
- Il y a des commentaires sur les points critiques du code
- docstring

## Fiabilité, niveau de contrôle, saisie

- Est ce que les saisies sont vérifiées? 
	- Qu'est ce qui se passe si on valide un input vide? Un client qui n'existe pas? ...
	- Cas pathologique à inventer au fur et à mesure de la description des fonctionnalités par les étudiants: qu'est ce qui se passe si...
- Ergonomie générale de la saisie
	- input brut / input + vérif + while / input avancé = proposition de réponse + sélection de valeur
	- certains projets sont très mal organisés et il faut rentrer plusieurs fois la même info ou rentrer des info redondantes... D'autres sont très élégants

## Chemin d'accès aux fichiers

- pénalité pour les chemins d'accès globaux (non transférable d'un ordi à l'autre)
- pénalité pour les fichiers textes qui sont au milieu du code... (souvent avec la BD)
- vérification du respect de la structure arborescente proposée initialement
	- Attention, je ne pénalise pas les imports dans le même répertoire: les dernières version de python imposent le ```__init__``` pour les modules 
- Traitement des ensembles de fichier avec du ```listdir``` (et pas une boucle pourrie avec des noms et une borne en dur)

## Menu

- Combien de niveaux? 
	- Possibilité de retour en arrière entre niveaux
- Quelle cohérence/complétude?
- Ergonomie générale du menu
- + Esthétique du menu
- Certains groupes font du Tkinter... En général, c'est mal codé et plein de variables globales... Mais ça part d'une bonne intention... Je mets régulièrement un bonus.

## SQL (et un peu python)

- Complexité des requêtes SQL dans les fonctions développées
	- vérification de l'existence de group by + sous-requêtes
	- complexité dans l'enchainement des insert
- Complexité du python (joli enchaînements de fonction), fonctionnalités ambitieuses, ...
- Respect des wildcards
	- tolérance pour tous les cas où la wildcard ne marche pas (table, nom de colonne...)
- Pénalisation forte sur les erreurs d'usage python/SQL
	- select * puis boucle for pour la sélection au lieu d'un where : il faut que les traitements lourds en volume de données soient en SQL et les légers en python

- Nombre de fonctionnalité et cohérence du scénario
	- le nombre de fonctionnalité n'est pas très important... Mais un peu quand même
	- cohérence du scénario: Ca relève du code et un peu de l'oral... Mais certains projets sont particulièrement cohérents, on a vraiment une impression d'utilité et de complétude des fonctions... Ca mérite un petit bonus.
		[non rempli pour la majorité des groupes]