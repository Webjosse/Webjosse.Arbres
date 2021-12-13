from file import File

class Arbre:
    def __init__(self, val):
        self.val = val
        self.fd = None
        self.fg = None

    def __str__(self):
        return str(self.val)

    def prefixe_afficher(self):
        if self == None:
            return
        print(self)
        Arbre.prefixe_afficher(self.fg)
        Arbre.prefixe_afficher(self.fd)
        
    def infixe_afficher(self):
        if self == None:
            return
        Arbre.infixe_afficher(self.fg)
        print(self)
        Arbre.infixe_afficher(self.fd)
        
    def suffixe_afficher(self):
        if self == None:
            return
        Arbre.suffixe_afficher(self.fg)
        Arbre.suffixe_afficher(self.fd)
        print(self)

    def niveau_afficher(self):
        F = File()
        F.ajoutQueue(self)
        while not F.est_vide():
            s = F.accesTete()
            if s != None:
                print(s)
                F.ajoutQueue(s.fg)
                F.ajoutQueue(s.fd)
            F.retireTete()

    def recherche(self,val):
        if self == None:
            return False
        if self.val == val:
            return True
        return Arbre.recherche(self.fg,val) or Arbre.recherche(self.fd,val)

    def miroir(self):
        if self == None:
            return None
        reflet = Arbre(self.val)
        reflet.fg = Arbre.miroir(self.fd)
        reflet.fd = Arbre.miroir(self.fg)
        return reflet

    def _affichage_arborescence(self,val=0):
        if self == None:
            return ""
        t = "┃"*val
        t = "\n" + t + "┣" + str(self)
        t += Arbre._affichage_arborescence(self.fd,val+1)
        t += Arbre._affichage_arborescence(self.fg,val+1)
        return t


    max_val = 99999

    def minimum(self):
        if self == None:
            return Arbre.max_val
        return min(
            self.val,min(
                Arbre.minimum(self.fg),
                Arbre.minimum(self.fd)
                )                
            )

    
    def afficher_arbre(self):
        print(self._affichage_arborescence())
