

# Teaching

### Python 1A / App

Afficher un tableau avec le bon alignement des colonnes:

```python
def aff_tab_format(data, entete = None):
"""
USAGE : aff_tab_format(data, entete = None)
Affiche le tableau mis en forme
In:
    Data : liste de tuple (comme un résultat de requête)
    Entête : liste contenant le nom des colonnes (argument optionnel)
"""
    if entete != None:
        data = [['-'*len(e) for e in entete], entete, ['-'*len(e) for e in entete]]+data
    if len(data) == 0:
        return ""
    # largeur des colonnes
    larg = [max([len(str(data[i][e])) for i in range(len(data))]) for e in range(len(data[0]))] 
    ret = "\n".join(' '.join("{:{width}s} ".format(str(ligne[c]), width=larg[c] ) for c in range(len(data[0]))) for ligne in data)
    return ret

data = [("toto", "un texte plus long", 18), ("titt", "un texte plus court", 22)]
print(aff_tab_format(data, ["col1", "col2", "col3"]))
print(aff_tab_format(data))
```

Afficher les fichiers présents dans un répertoire
```python
import os
chemin = '../Data/Files/'
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

Jouer avec les dates: exemple ajouter 2 semaines.

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

