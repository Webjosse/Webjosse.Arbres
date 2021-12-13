from ABR import ABR
from flask import Flask as _Flask
from file import File as _File

_app = _Flask(__name__)


_local_abr = ABR([10])

def voir(a):
    global _local_abr
    _local_abr = a
    _app.run(host='127.0.0.1', port='5000', debug=False)

_layfile = open("layout.html","r")
_layout = _layfile.read()
_layfile.close()

def _to_div(a):
    F = _File()

    t = "<div>"
    niveau = 0

    cont = True

    oTt = False

    F.ajoutQueue([a,niveau])
    while cont and not F.est_vide():
        s = F.accesTete()

        sommet = s[0]
        nivtete = s[1]
        if nivtete > niveau:
            niveau = nivtete
            t += "</div><div>"
            cont = OTt
            OTt = False

        if sommet == None:
            t += "<p> </p>"
            F.ajoutQueue([None,nivtete+1])
            F.ajoutQueue([None,nivtete+1])
        else:
            t += "<p class=\"el\">"+str(sommet)+"</p>"
            OTt = True
            F.ajoutQueue([sommet.fg,nivtete+1])
            F.ajoutQueue([sommet.fd,nivtete+1])

        F.retireTete()
    t += "</div>"
    return t

@_app.route('/')
def _index():
    global _local_abr
    return _layout.replace("{{INNER}}",_to_div(_local_abr))

