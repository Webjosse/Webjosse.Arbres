from Arbre import Arbre

class ABR(Arbre):

    #Se définit depuis une liste d'int
    def __init__(self,liste):
        Arbre.__init__(self,liste[0])
        i = 1
        while i<len(liste):
            self.planter(liste[i])
            i += 1

    def planter(self,val):
        if val>self.val:
            if self.fd == None:
                self.fd = ABR([val])
            else:
                self.fd.planter(val)
        else:
            if self.fg == None:
                self.fg = ABR([val])
            else:
                self.fg.planter(val)
    
    def recherche(self,val):
        if self == None:
            return False
        if self.val == val:
            return True
        if val <self.val:
            return ABR.recherche(self.fg,val)
        else:
            return ABR.recherche(self.fd,val)

    
    def supprimer(self,val):
        if self == None:
            return None
        if val > self.val:
            self.fd = ABR.supprimer(self.fd,val)
            return self
        elif val < self.val:
            self.fg = ABR.supprimer(self.fg,val)
            return self

        if self.fg == None:
            return self.fd
        if self.fd == None:
            return self.fg
        
        parent = self
        noeud = self.fg
        while noeud.fd != None:
            parent = noeud
            noeud = noeud.fd
        
        self.val = noeud.val
        if parent == self:
            self.fg = noeud.fg
        else:
            parent.fd = noeud.fg
        
        return self
