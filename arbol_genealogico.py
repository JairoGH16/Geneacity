from nodos_arbol import Nodo_persona

class Arbol_genealogico_insertador:
    def insertar_personas_casa(self,raiz:Nodo_persona,lista_personas:list['Nodo_persona']):
        for persona in lista_personas:
            self.__insertar_persona(raiz,persona)
    def __insertar_persona(self,raiz,persona):
        if self.__insertar_hermanos_tios(raiz,persona):
            return True
        elif self.__insertar_ascendencia(raiz,persona):
            return True
        elif self.__insertar_descendencia(raiz,persona):
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
    def __insertar_hermanos_tios(self,raiz:Nodo_persona,persona:Nodo_persona):
        if raiz:
            if (raiz.padre_id == persona.padre_id and raiz.padre_id != 0) or (raiz.madre_id == persona.madre_id and raiz.madre_id != 0):
                if persona not in raiz.hermanos:
                    raiz.hermanos.append(persona)
                if raiz not in persona.hermanos:
                    persona.hermanos.append(raiz)
                    return True
            elif self.__insertar_hermanos_tios(raiz.padre,persona):
                return True
            elif self.__insertar_hermanos_tios(raiz.madre,persona):
                return True
            return False
    def __insertar_descendencia(self,raiz:Nodo_persona,persona:Nodo_persona):
        if raiz:
            if raiz.persona_id==persona.padre_id:
                raiz.hijos.append(persona)
                persona.padre=raiz
                return True
            elif raiz.persona_id==persona.madre_id:
                raiz.hijos.append(persona)
                persona.madre=raiz
                return True
            elif len(raiz.hijos) > 0:
                for hijo in raiz.hijos:
                    if self.__insertar_descendencia(hijo,persona)==True:
                        return True
            return False
            
#BISABUELO
Rodolfo=Nodo_persona(1,0,12,"Rodolfo","Male",80,"Single")
Lucho=Nodo_persona(23,0,12,"Lucho","Male",70,"Married")
#ABUELO
Pablo=Nodo_persona(2,1,11,"Pablo","Male",55,"Single")
#PADRE
ernesto=Nodo_persona(3,2,10,"Ernesto","Male",25,"Single")
#PERSONA
luis=Nodo_persona(4,3,9,"Luis","Male",5,"Single")
#HIJO
pedro=Nodo_persona(22,4,89,"Pedro","Male",1,"Married")
arbol=Arbol_genealogico_insertador()
arbol.insertar_personas_casa(luis,[ernesto,Pablo])
arbol.insertar_personas_casa(luis,[Rodolfo])
arbol.insertar_personas_casa(luis,[pedro])
arbol.insertar_personas_casa(pedro,[Lucho])
pass