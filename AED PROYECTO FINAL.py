import re

class NodoRegion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subregiones = {}
        self.centros = []

def agregar_jerarquia(raiz, region, subregion, centro):
    if region not in raiz.subregiones:
        nuevo_nodo_region = NodoRegion(region)
        raiz.subregiones[region] = nuevo_nodo_region
    
    nodo_reg = raiz.subregiones[region]
    
    if subregion not in nodo_reg.subregiones:
        nuevo_nodo_sub = NodoRegion(subregion)
        nodo_reg.subregiones[subregion] = nuevo_nodo_sub
        
    nodo_sub = nodo_reg.subregiones[subregion]
    
    if centro not in nodo_sub.centros:
        nodo_sub.centros.append(centro)



def validar_password(password):
    if len(password) < 6:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    return True