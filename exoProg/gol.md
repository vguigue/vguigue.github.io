# Game of life

Le jeu de la vie de Conway est une simulation d'évolution d'un ensemble de cellules qui survivent, émergent ou meurent en fonction de leur environnement, selon des règles *très* simples. Les informations importantes sont résumées ci-dessous, les détails sont disponibles sur wikipedia: [lien](https://fr.wikipedia.org/wiki/Jeu_de_la_vie)

Les règles d'évolution du monde sont les suivantes:

    * si une cellule a 3 voisines vivantes, elle survit ou est créée à la génération suivante
    * si une cellule a 2 voisines vivantes, elle reste dans l'état précédent
    * sinon, elle meure

L'énoncé suivant est très long... Nous proposons un découpage en différentes sous-tâches avec des défis identifiés à chaque étape et des tests de validation intermédiaire.

1. Créer un monde aléatoirement (et l'afficher)
2. Compter les cellules voisines vivantes
3. Mettre à jour le monde et faire défiler les générations.


# 1. Création et affichage du monde

### concept préliminaire: les booléens

Le type booléen est un type comme les autres: il est possible de créer une variable et de jouer avec comme suit comme suit:

```python
a = True # affectation directe
b = 3 < random.random() # stockage du résultat d'un test
if b:
    print("c'est très étonnant")
else:
    print("ouf !")
```

Aucun problème à créer des listes de booléens:
```python
li = []
for i in range(15):
    li.append(random.random()<0.2)
print(li)
cpt = 0
for b in li:
    if b: cpt += 1
print(cpt)
```
Exécuter le code précédent et comprendre les affichages.

### concept préliminaire: les matrices

Une matrice est une liste de liste. Assez facile à créer:
```python
matrice = [[1, 2, 3], [4, 5, 6]]
matrice.append([7, 8, 9])
# accès en lecture
print(matrice[0][1]) # 2
# modifications
matrice[0][1] = 12
print(matrice)
```

Compter les lignes et les colonnes:
```python
print(len(matrice)) # compte les éléments de la liste (i.e. des sous-listes) = nb lignes
print(len(matrice[0])) # compte les éléments du premier élément la liste = nb colonnes
```

### concept préliminaire: les options de print

il est possible de faire des `print` sans retour à la ligne:
```python
print("toto") # affichage de la chaine + retour à la ligne
print("toto", end='')  # affichage de la chaine SANS retour à la ligne
print("titi ", end='') # avec un espace
print("tata")
```

### Génération du monde: `generate_monde`

Les informations à fournir à cette méthode sont: 
    * la taille du monde (nombre de lignes, nombre de colonnes)
    * le taux de cellule vivante dans le monde

La méthode retourne une matrice de booléen (cf questions préliminaires précédentes): les cellules vivantes valent `True`, les mortes valent `False`.

#### <span style="color: red;"> TEST à valider </span>

Sur un tout petit monde, on pourrait obtenir le code suivant:
```python
monde = generate_monde(2, 2, 0.2)
print(monde)
```
donne (aux aléas de random près):
```
[[True, False], [False, False]]
```


### Affichage du monde: `print_monde`

Cette fonction permet de débuguer la précédente :)

La fonction prend en argument le monde, ne retourne rien du tout et consiste principalement en une double boucle, chaque cellule étant alors affichée sous forme de `.`(=morte) ou `X`(=vivante).

```python
monde = generate_monde(6, 8, 0.2)
print_monde(monde) 
```
donne (aux aléas de random près):
```
....XX..
.X.....X
X.....X.
.......X
...X..X.
........
```

# 2. Comptage des voisins vivants

Commençons par un exemple:
```
.X.
.O.
..X
```
La cellule `O` a deux voisins vivants.

### Travail préliminaire: un monde sphérique

Dans le monde suivant, la cellule `O` a les 8 voisins repérés par les chiffres correspondants:
```
4O5.XX..
678....X
X.....X.
.......X
...X..X.
123.....
```

La solution proposée consiste à:
1. Pour tous les indices `m`, considérer `m-1, m, m+1`
2. Les indices négatifs doivent être *recalculés*... L'algorithme suivant permet de le faire

```python
# Soit nlignes le nombre de lignes
# soit m et n les coordonnées de base:
# soit i prenant les valeurs [m-1, m, m+1]
i_corrige = (i + nlignes)%nlignes
```
Sur un exemple:
```python
nlignes = 10 
i   = 2 # une coordonnée sur la ligne 2
i_c = (i+nlignes)%nlignes # => 2 (inchangé)

i = -1 # cas critique des voisins de la ligne 0
i_c = (i+nlignes)%nlignes # => 9 (passage sur la dernière ligne)
```

### Travail préliminaire: *bloquer* la fonction random

Construire des exemples reproductibles dans un contexte stochastique est dur! La solution consiste à *bloquer* la fonction random comme suit:

```python
import random
random.seed(0) # initialisation bloquée de random

random.random() # => 0.8444218515250481
# on retire le même nombre aléatoire si on relance le programme.
```

### Fonction de comptage: `cpt_voisins`

La clé du jeu de la vie consiste, pour chaque cellule du plateau, à compter les cellules vivantes parmi les 9 voisines.

La fonction `cpt_voisins` travaille sur UNE case: elle prend en argument le monde et des coordonnées `m,n`; elle retourne le nombre de voisins vivants de cette case en particulier.

#### <span style="color: red;"> TEST à valider </span>

```python
random.seed(1) # pour rendre l'expérience reproductible

monde = generate_monde(6, 8, 0.2)
print_monde(monde) 
# X.......
# XX...X..
# ...XX...
# ..X.....
# ...X...X
# ..X.....
print(cpt_voisins(monde, 0, 0)) # 2
print(cpt_voisins(monde, 1, 1)) # 2 
print(cpt_voisins(monde, 1, 4)) # 3
print(cpt_voisins(monde, 0, 3)) # 1

```

#### Test facultatif

il est intéressant de construire une seconde fonction `print_monde_db` qui affiche le nombre de voisins des cases vides. Cette fonction (variation à une ligne près de la fonction existante) permet de valider le calcul des voisins et sera utile dans la mise à jour.

```
X.......
XX...X..
...XX...
..X.....
...X...X
..X.....
========
X4211112
XX223X12
233XX211
11X43111
123X101X
22X21012
```

# 3. Mise à jour du monde

La mise à jour du monde semble simple:
1. Calcul des nombres de voisins
2. MAJ des cases de la matrice

Mais ça va être plus compliqué. Le principal problème est que la mise à jour d'une case risque d'avoir un impact sur le calcul du nombre de voisins de la case d'à coté... Ce qui n'est pas souhaitable. Il faut donc basculer vers:

1. Copie du monde : `monde` + `newmonde`
2. Calcul des nombres de voisins dans `monde`
3. MAJ des cases de la matrice dans `newmonde`

### Copie en surface, copie en profondeur, copie en grande profondeur

Le problème de base est connu: il s'agit de référence ou de pointeur...
```python
li  = [5, 2, 3]
li2 = li # problème de référence
li2[0] = 12
print(li) # aie aie aie
```
La solution est connue:
```python
li  = [5, 2, 3]
li2 = li.copy() # a ce moment, il y a deux listes distinctes
li2[0] = 12
print(li) # OK
```
MAIS, le problème devient plus complexe sur les matrices!
```python
li  = [[5, 2, 3], [10, 1, 8]]
li2 = li.copy() 
li2[0][0] = 12
print(li) # aie aie aie
```
La solution est alors de faire appel à un package specifique:
```python
import copy
li  = [[5, 2, 3], [10, 1, 8]]
li2 = copy.deepcopy(li) 
li2[0][0] = 12
print(li) # OK
```

### Fonction de mise à jour du monde: `update_monde`

Cette fonction prend en argument l'ancien monde, crée un nouveau monde, passe sur toutes les cases et les mets à jour selon les deux règles énoncées précedemment et rappelées ci-dessous:

Les règles d'évolution du monde sont les suivantes:

    * si une cellule a 3 voisines vivantes, elle survit ou est créée à la génération suivante
    * si une cellule a 2 voisines vivantes, elle reste dans l'état précédent
    * sinon, elle meure

#### <span style="color: red;"> TEST à valider </span>


```
........X.
..X.......
...XX....X
..........
...X......
..X..X....
....X.X...
.....XXX..
X..XX.X...
..X..XX...
==========
..........
...X......
...X......
...XX.....
..........
...XXX....
....X..X..
...X...X..
...XX.....
...XXXXX..
```

### Fonction d'évolution du monde sur plusieurs générations: `play_generations`

Afin de jouer plusieurs génération, il est nécessaire d'introduire deux nouveaux outils: 

1. effacer la console entre 2 générations
2. mattre une temporisation pour visualiser l'animation

```python
# imports spécifiques
import os
import time

def cls(): 
    """
    usage = cls()
    fonction d'effaçage de la console
    """
    os.system("clear") # pour macos
    # os.system("cls") # pour windows (je crois)

def democls():
    """
    usage = democls()
    fonction de démonstration pour afficher une animation dans la console
    """
    for i in range(6):
        cls() # vider la console
        print(" "*i + 'X')
        time.sleep(1)

democls() # invocation de la démonstration

```

Construire la fonction `play_generations` sur le même format.

# 4. Pour aller plus loin

Tester les motifs classiques du jeu de la vie en repartant de la page wikipedia:
[link](https://fr.wikipedia.org/wiki/Jeu_de_la_vie) en allant à la section *Structure*