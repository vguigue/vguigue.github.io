# Game of life

Le jeu de la vie de Conway est une simulation d'évolution d'un ensemble de cellules qui survivent, émergent ou meurent en fonction de leur environnement, selon des règles *très* simples. Les informations importantes sont résumées ci-dessous, les détails sont disponibles sur wikipedia: [lien](https://fr.wikipedia.org/wiki/Jeu_de_la_vie)

1. Les cellules sont réparties dans une matrice, comme illustré ci-dessous:
```
......X...
.....XX...
.XX.......
..XX.X....
...X..X...
...X..X...
....X.....
...X......
.XX..X..X.
...X...X..
```
2. Les règles d'évolution sont les suivantes:
    * si une cellule a 3 voisines vivantes, elle survit ou est créée à la génération suivante
    * si une cellule a 2 voisines vivantes, elle reste dans l'état précédent
    * sinon, elle meure

Nous proposons un découpage en différentes sous-tâches avec des défis identifiés à chaque étape.

## Création et affichage du monde

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
print("toto", end='') # affichage de la chaine SANS retour à la ligne
```

### Génération du monde: `generate_monde`

Les informations à fournir à cette méthode sont: 
    * la taille du monde (nombre de lignes, nombre de colonnes)
    * le taux de cellule vivante dans le monde

La méthode retourne une matrice de booléen (cf questions préliminaires précédentes): les cellules vivantes valent `True`, les mortes valent `False`.

Sur un petit monde, on pourrait obtenir le code suivant:
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

## Comptage des voisins vivants: `cpt_voisins`

La clé du jeu de la vie consiste, pour chaque cellule du plateau, à compter les cellules vivantes parmi les 9 voisines:
```
.X.
.O.
..X
```
La cellule `O` a deux voisins vivants.

La fonction `cpt_voisins` travaille sur UNE case: elle prend en argument le monde et des coordonnées `m,n`; elle retourne le nombre de voisins vivants de cette case en particulier.

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


