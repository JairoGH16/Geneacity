import json
from nodos_arbol import Nodo_persona

class Arbol_genealogico_insertador:
    def __init__(self) -> None:
        self.hermanos_tios_ids = []
        self.ascendencia_ids = []
        self.descendencia_ids = []
        self.sobrinos_primos_ids = []

    def insertar_persona(self,raiz,persona):
        if self.__insertar_hermanos_tios(raiz,persona):
            if persona.persona_id not in self.hermanos_tios_ids:
                self.hermanos_tios_ids.append(persona.persona_id)
                self.guardar_json()
            return True
        elif self.__insertar_ascendencia(raiz,persona):
            if persona.persona_id not in self.ascendencia_ids:
                self.ascendencia_ids.append(persona.persona_id)
                self.guardar_json()
            return True
        elif self.__insertar_descendencia(raiz,persona):
            if persona.persona_id not in self.descendencia_ids:
                self.descendencia_ids.append(persona.persona_id)
                self.guardar_json()
            return True
        elif self.__insertar_sobrinos_primos(raiz,persona):
            if persona.persona_id not in self.sobrinos_primos_ids:
                self.sobrinos_primos_ids.append(persona.persona_id)
                self.guardar_json()
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
    def __insertar_ascendencia(self,raiz:Nodo_persona,persona:Nodo_persona):
        if raiz:
            if raiz.padre_id==persona.persona_id:
                if raiz not in persona.hijos:
                    raiz.padre=persona
                    persona.hijos.append(raiz)
                return True
            elif raiz.madre_id==persona.persona_id:
                if raiz not in persona.hijos:
                    raiz.madre=persona
                    persona.hijos.append(raiz)
                return True
            elif self.__insertar_ascendencia(raiz.padre,persona)==True:
                return True
            elif self.__insertar_ascendencia(raiz.madre,persona)==True:
                return True
            return False
    def __insertar_descendencia(self,raiz:Nodo_persona,persona:Nodo_persona):
        if raiz:
            if raiz.persona_id==persona.padre_id:
                if persona not in raiz.hijos:
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
    def __insertar_sobrinos_primos(self,raiz:Nodo_persona,persona:Nodo_persona):
        if raiz:
            for hermano in raiz.hermanos:
                if self.__insertar_descendencia(hermano,persona):
                    return True
            if self.__insertar_sobrinos_primos(raiz.padre,persona):
                return True
            if self.__insertar_sobrinos_primos(raiz.madre,persona):
                return True
        return False
    
    def guardar_json(self):
        data = {
            "hermanos_tios": self.hermanos_tios_ids,
            "ascendencia": self.ascendencia_ids,
            "descendencia": self.descendencia_ids,
            "sobrinos_primos": self.sobrinos_primos_ids
        }
        with open("arbol_genealogico.json", "w") as file:
            json.dump(data, file, indent=4)
            
#BISABUELO
Rodolfo=Nodo_persona(1,0,12,"Rodolfo","Male",80,"Single")
Lucho=Nodo_persona(23,0,12,"Lucho","Male",70,"Married")
#Hijo de Lucho
Esteban=Nodo_persona(45,23,46,"Esteban","Male",65,"Married")
#ABUELO
Pablo=Nodo_persona(2,1,11,"Pablo","Male",55,"Single")
#PADRE
ernesto=Nodo_persona(3,2,10,"Ernesto","Male",25,"Single")
#PERSONA
luis=Nodo_persona(4,3,9,"Luis","Male",5,"Single")
#HIJO
pedro=Nodo_persona(22,4,89,"Pedro","Male",1,"Married")
arbol=Arbol_genealogico_insertador()
arbol.insertar_persona(luis,ernesto)
arbol.insertar_persona(luis,Pablo)
arbol.insertar_persona(luis,Rodolfo)
arbol.insertar_persona(luis,pedro)
arbol.insertar_persona(pedro,Lucho)
arbol.insertar_persona(pedro,Esteban)
pass