

# Teaching

## Python 1A / App

[lien vers le formulaire d'évaluation (en version beta)](eval_python.md)

#### Fonction de lecture de fichier (.txt, .csv, ...) & usage
un peu plus générale que celle utilisée dans les TP précédents

```python
def fichier2list(fichier):
    """
    USAGE : fichier2list(fichier)
    lit le fichier et retourne le contenu sous la forme de matrice
    In:
        fichier : chemin d'accès au fichier
    Out:
        matrice des données
    """

    fichier = open(fichier,"r")     # ouverture du fichier
                                    # on ne s'occupe pas de l'entête
    
    data = fichier.readlines()      # lecture du fichier
    liste_data = []
    for ligne in data:
        ligne = ligne.replace('\n', '') # suppression du saut de ligne
        ligne = ligne.split('\t') # on coupe sur les tabulations...
        # ligne = ligne.split() # pour vétérinaire => tous les séparateurs
        liste_data.append(ligne)
    
    fichier.close()

    return liste_data
```

Usage
```python
# définition du chemin vers le fichier à lire
chemin = "../Data/Files/monFichier.txt"
""" Par exemple:
titre	Superman		
date de sortie	10/12/1978		
acteurs			
nom	prenom	web	role
Brando	Marlon	marlonbrando.com	Jor-El
"""
info = fichier2list(chemin)
print(info)
"""
Contenu de info:
info = [["titre", "Superman"], ["date de sortie", "10/12/1978"], ["acteur"],["nom", "prenom", "web", "role"], ...]
"""
# accéder à la date:
info[1][1] # 2e ligne, 2e colonne
# combien de lignes?
print(len(info))
```

#### Afficher un tableau avec le bon alignement des colonnes:

Ce n'est pas simple: il faut d'abord savoir combien de caractères réserver pour chaque colonne puis lancer l'affichage

```python
def aff_tab_format(data, entete = None):
    """
    USAGE : aff_tab_format(data, entete = None)
    Affiche le tableau mis en forme
    In:
        Data : liste de tuple (comme un résultat de requête)
        Entête : liste contenant le nom des colonnes 
                (argument optionnel, mais ça fait plus joli)
    """
    if entete != None:
        data = [['-'*len(e) for e in entete], entete,\
            ['-'*len(e) for e in entete]]+data
    if len(data) == 0:
        return ""
    # largeur des colonnes (plus longue séquence à afficher dans la colonne)
    larg = [max([len(str(data[i][e])) for i in range(len(data))])\
         for e in range(len(data[0]))] 
    ret = "\n".join(' '.join("{:{width}s} ".format(str(ligne[c]), width=larg[c] )\
         for c in range(len(data[0]))) for ligne in data)
    return ret

data = [("toto", "un texte plus long", 18), ("titt", "un texte plus court", 22)]
print(aff_tab_format(data, ["col1", "col2", "col3"]))
print(aff_tab_format(data))
```

#### Afficher les fichiers présents dans un répertoire

Si vous êtes capable de traiter un fichier du projet (e.g. ```test.txt```), il est très simple de traiter tous les fichiers du répertoire:

```python
import os
chemin = '../Data/Files/'

# explication générale du fonctionnement
liste = os.listdir(chemin)
print(liste)
print(liste[0])

# pour aller un peu plus loin (ne récupérer que les fichiers .txt)
liste = [f for f in os.listdir(chemin) if ".txt" in f]

# Parcourir les fichiers
for f in liste:
    nom_fichier = chemin+f
    ...

```

#### Jouer avec les dates: exemple ajouter 2 semaines.

ATTENTION: c'est assez dur !! Il faut utiliser les outils externes

```python
import datetime

#1. Créer une date
date = datetime.datetime(2023,10,22)
print(date)
datetime_str = "2022-10-22"
date2 =  datetime.datetime.strptime(datetime_str, '%Y-%m-%d')
print(date2)

#2. ajouter un délai
date = date + datetime.timedelta(weeks=4)

print(date)

```
### Rappel sur le traitement de problématiques complexes



**Python reminders, SQL bases** being able to program classical algorithm, avoid most traps and access data everywhere.

Apprentis access: [link](https://ecampus.paris-saclay.fr/enrol/instances.php?id=70409)

### Object Programming

A list of playful and educational exercises to improve OOP! [link](exoOOP.md)

### Data-sciences

Courses dedicated to the IODAA branch, AgroParisTech 3A.

* git basics: [link](https://github.com/vguigue/tuto_git)
* numpy/matplotlib: [link](https://github.com/vguigue/tuto_numpy)
* scikit-learn: [link](https://github.com/vguigue/tuto_sklearn)
* pytorch/deep learning: [link](https://github.com/vguigue/tuto_deep)

Seminar on appied machine learning
* Recommender Systems: [link](https://github.com/vguigue/reco_2019)
* Time series: TBD


