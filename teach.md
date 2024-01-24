

# Teaching

### Python 1A / App

```python
def aff_tab_format(data, entete = None):
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

