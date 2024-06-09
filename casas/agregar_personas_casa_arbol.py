from arbol.arbol_genealogico import Arbol_genealogico_insertador
from arbol.nodos_arbol import Nodo_persona

class Insertador_casas_arbol:
    def __init__(self):
        self.arbol:Arbol_genealogico_insertador=Arbol_genealogico_insertador()
    def insertar_grupo_personas(self,lista_personas,nodo_raiz):
        contador=0
        nueva_lista_nodos=[]
        for persona in lista_personas:
            nueva_lista_nodos.append(Nodo_persona(persona["id"],persona["father"],persona["mother"],persona["name"],persona["gender"],persona["age"],persona["marital_status"]))
        for persona in nueva_lista_nodos:
            if self.arbol.insertar_persona(nodo_raiz,persona):
                contador += 1
        if contador == 0:
            print ("No se descubrieron familiares nuevos.")
        else:
            print(f"Se descubrieron {contador} familiares nuevos.")