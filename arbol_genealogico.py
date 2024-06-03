import consultas
from nodos_arbol import Nodo_persona

class Arbol_genealogico:
    def insertar_personas_casa(self,raiz,lista_personas):
        lista_personas
        for persona in lista_personas:
            self.__insertar_persona(raiz,persona)
        pass
    #Los hijos no están porque estos se agregan desde Agregador_familiares_directos inmediatamente cuando nacen.
    def __insertar_persona(self,raiz,persona):
        if self.__insertar_ascendencia(raiz,persona)==True:
            return True
        elif self.__insertar_hermanos(raiz,persona)==True:
            return True
        return False
    def __insertar_ascendencia(self,raiz:Nodo_persona,persona:Nodo_persona):
        if raiz:
            if raiz.padre_id==persona.persona_id:
                raiz.padre=persona
                return True
            elif raiz.madre_id==persona.persona_id:
                raiz.madre=persona
                return True
            elif self.__insertar_ascendencia(raiz.padre,persona)==True:
                return True
            elif self.__insertar_ascendencia(raiz.madre,persona)==True:
                return True
            return False
    def __insertar_hermanos(self,raiz:Nodo_persona,persona:Nodo_persona):
        if raiz:
            if (raiz.padre_id == persona.padre_id and raiz.padre_id != 0) or (raiz.madre_id == persona.madre_id and raiz.madre_id != 0):
                if persona not in raiz.hermanos:
                    raiz.hermanos.append(persona)
                if raiz not in persona.hermanos:
                    persona.hermanos.append(raiz)
            
Luis=Nodo_persona(20,1,2,"Luis","Male",23,"Single")
Juan=Nodo_persona(30,1,2,"Juan","Male",23,"Single")
#Padres
Miguel=Nodo_persona(1,3,4,"Miguel","Male",43,"Single")
Maria=Nodo_persona(2,5,6,"Maria","Female",40,"Single")
Luis.madre=Maria
Luis.padre=Miguel
Juan.padre=Miguel
Juan.madre=Maria
#Abuelos paternos
Mauricio=Nodo_persona(3,7,8,"Mauricio","Male",60,"Single")
Ana=Nodo_persona(4,9,10,"Ana","Male",58,"Single")
#Abuelos maternos
Hernando=Nodo_persona(5,11,12,"Hernando","Male",70,"Single")
Leticia=Nodo_persona(6,13,14,"Leticia","Male",68,"Single")
casa_lista=[Juan]
arbol=Arbol_genealogico()
arbol.insertar_personas_casa(Luis,casa_lista)
pass