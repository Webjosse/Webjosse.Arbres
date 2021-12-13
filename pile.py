class Pile:

    class Maillon:
        def __init__(self,val):
            self._val = val
            self._suiv = None

    def __init__(self):
        self._sommet = None

    def est_vide(self):
        b = (self._sommet == None)
        return b

    def empile(self,e):
        nouvMaillon = Pile.Maillon(e)
        nouvMaillon._suiv = self._sommet
        self._sommet = nouvMaillon

    def est_pleine(self):
        b = False
        return b

    def depile(self):
        self._sommet = self._sommet._suiv

    def sommet(self):
        e = self._sommet._val
        return e
