# Follow the lady

Le sujet suivant a été conçu pour une UE de programmation objet en JAVA... Il est évidemment possible (et intéressant) de le traiter en n'importe quel langage, notammment le python.

* L'énoncé inclus le type des variables, c'est intéressant même si c'est implicite en python.
* `null` en java est l'équivalent de `None` en python


### Règles

Le jeu Follow the lady (ou bonneteau en francais) est un jeu classique de hasard : trois cartes sont posées à la suite sur une table (typiquement 2 valets et une dame de coeur), un joueur mélange les cartes en échangeant leurs positions et le joueur adverse doit deviner où se trouve la dame de coeur.

### Modélisation

Nous allons modéliser le jeu en utilisant 3 classes : Carte pour représenter une carte, Emplacement pour représenter là où peuvent être posées les cartes, et Jeu pour gérer le mécanisme du jeu.


## Questions plus précises

### Donner la classe **Carte** qui contient:

* une variable d’instance `String nom`, 
* deux constructeurs (le premier sans paramètre qui nomme la carte par défaut “Valet”, et le deuxième à un paramètre, le nom  – penser à utiiliser this(…) pour l’un des deux)
* la méthode `String toString()` qui permet de renvoyer le nom de la carte.

### Donner la classe **Emplacement**  qui contient :

* deux variables, `Carte carte` et `String nom`. La variable carte permet de stocker la carte qui sera posée sur cet emplacement (que vaut la variable lorsqu’aucune carte n’est posée ?).
* une méthode `String toString()` qui renvoie `nom de l’emplacement : nom de la carte`;
* une méthode `boolean estVide()` qui permet de savoir si l’emplacement est disponible;
* les méthodes `boolean poser(Carte carte)` qui permet de poser une carte sur l’emplacement (renvoie faux si l’emplacement n’est pas vide, vrai si l’emplacement était vide et la carte a été posée), 
* `Carte enlever()` qui permet de retirer la carte de l’emplacement (renvoie `null` s’il n’y a pas de carte).
* deux constructeurs : `Emplacement(String nom)` qui initialise juste le nom, et `Emplacement(String nom, Carte carte)` qui permet de passer également une carte à poser sur l’emplacement en paramètre.

Tester votre classe en faisant un main qui créé un emplacement, puis une carte, puis dépose la carte sur l’emplacement, affiche la description de l’emplacement, puis enlève la carte et ré-affiche l’emplacement.

### La classe **Jeu** permet d’initialiser le jeu et de jouer. 

Elle dispose :

* trois variables `Emplacement gauche`, `milieu`, `droit` et une variable `Carte cible` (la carte que l’on cherche à retrouver).
* un constructeur Jeu() qui permet d’initialiser le jeu (qui créé les trois emplacements, les trois cartes, enregistre la cible et dispose les trois cartes sur les emplacements).
* une méthode String toString() qui permet de renvoyer la description de l’état du jeu (les 3 emplacements avec la carte qu’ils contiennent).
* Ajouter à la classe Jeu la méthode void echanger(Emplacement a, Emplacement b) qui permet d’échanger les cartes entre les deux emplacements en paramètres (en utilisant les méthodes poser et enlever de Carte). Ajouter également la méthode void echanger(int i, int j) qui permet d’échanger les deux emplacements indiqués par les entier i et j (en considérant que gauche est 0, milieu 1 et droit 2; astuce : si i+j==1 alors c’est gauche et milieu qui sont échangés; si i+j==2 alors c’est gauche et droit; sinon c’est milieu et droit).
* Ajouter la méthode boolean choisir(Emplacement a) et boolean choisir(int i) qui renvoie true si l’emplacement a  (ou correspondant à l’entier i) contient la carte cible, false sinon.
* Ajouter la méthode void melanger() qui permet de échanger au hasard deux emplacements; la méthode void melanger(int n) qui permet de faire n mélanges au hasard.

Tester vos classes dans un main qui initialise un jeu, mélange 100 fois aléatoirement, et choisit un emplacement au hasard, affiche s’il a gagné ou pas. Répéter l’expérience 1000 fois. Quelle est la moyenne du nombre de fois où le programme gagne  ?
Quel est l’intérêt de déclarer en private les variables d’instances des différentes classes ? Y’a-t-il un moyen de tricher tel quel ? Et si les variables étaient public ?