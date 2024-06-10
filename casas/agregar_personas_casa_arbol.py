from arbol.arbol_genealogico import Arbol_genealogico_insertador
from arbol.nodos_arbol import Nodo_persona

class Insertador_casas_arbol:
    def __init__(self,personaje_seleccionado:Nodo_persona):
        self.personaje_seleccionado=personaje_seleccionado
        self.arbol:Arbol_genealogico_insertador=Arbol_genealogico_insertador()
    def insertar_grupo_personas(self,lista_personas,nodo_raiz):
        nueva_lista_nodos:list=[]
        for persona in lista_personas:
            nueva_lista_nodos.append(Nodo_persona(persona["id"],persona["father"],persona["mother"],persona["name"],persona["gender"],persona["age"],persona["marital_status"]))

        lista_nombres_retorno:list=[]
        for persona in nueva_lista_nodos:
            grado = self.arbol.insertar_persona(nodo_raiz,persona)
            if grado != None:
                lista_nombres_retorno.append(persona.nombre)
                self.personaje_seleccionado.puntaje+=(grado*5)
        return(lista_nombres_retorno)