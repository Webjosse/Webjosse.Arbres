class File:

    class Maillon:
        def __init__(self,val):
            self._val = val
            self._suiv = None

    def __init__(self):
        self._tete = None
        self._queue = None

    def est_vide(self):
        b = (self._tete == None)
        return b

    def ajoutQueue(self,e):
        if self._tete == None:
            self._queue = File.Maillon(e)
            self._tete = self._queue
        else:
            self._queue._suiv = File.Maillon(e)
            self._queue = self._queue._suiv

    def est_pleine(self):
        b = False
        return b

    def retireTete(self):
        self._tete = self._tete._suiv

    def accesTete(self):
        e = self._tete._val
        return e
