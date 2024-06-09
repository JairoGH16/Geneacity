import json
# import consultas as consultas
from nodos_arbol import Nodo_persona
import pydot
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

class Arbol_genealogico_insertador:
    def __init__(self) -> None:
        self.personaje_id = int
        self.hermanos_tios_ids = []
        self.ascendencia_ids = []
        self.descendencia_ids = []
        self.sobrinos_primos_ids = []

    def insertar_persona(self,raiz,persona):

        if self.__insertar_hermanos_tios(raiz,persona):
            if persona.persona_id not in self.hermanos_tios_ids:
                self.hermanos_tios_ids.append(persona.persona_id)
                self.guardar_json(raiz)
            return True
        elif self.__insertar_ascendencia(raiz,persona):
            if persona.persona_id not in self.ascendencia_ids:
                self.ascendencia_ids.append(persona.persona_id)
                self.guardar_json(raiz)
            return True
        elif self.__insertar_descendencia(raiz,persona):
            if persona.persona_id not in self.descendencia_ids:
                self.descendencia_ids.append(persona.persona_id)
                self.guardar_json(raiz)
            return True
        elif self.__insertar_sobrinos_primos(raiz,persona):
            if persona.persona_id not in self.sobrinos_primos_ids:
                self.sobrinos_primos_ids.append(persona.persona_id)
                self.guardar_json(raiz)
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
                if persona not in raiz.hijos:
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
    
    def guardar_json(self, raiz):
        data = {
            "hermanos_tios": self.hermanos_tios_ids,
            "ascendencia": self.ascendencia_ids,
            "descendencia": self.descendencia_ids,
            "sobrinos_primos": self.sobrinos_primos_ids
        }
        with open(f"arbol_genealogico.json", "w") as file:
            json.dump(data, file, indent=4)

    def cargar_json(self):
        with open("arbol_genealogico.json", "r") as file:
            data = json.load(file)
            self.hermanos_tios_ids = data.get("hermanos_tios", [])
            self.ascendencia_ids = data.get("ascendencia", [])
            self.descendencia_ids = data.get("descendencia", [])
            self.sobrinos_primos_ids = data.get("sobrinos_primos", [])

    # def cargar_arbol(self, raiz):
    #     self.cargar_json()
    #     for ascendencia_id in self.ascendencia_ids:
    #         info_actual = consultas.Consulta_persona_por_id.consultar_persona(ascendencia_id)
    #         ascendencia = Nodo_persona(info_actual["id"],
    #                              info_actual["father"], #id de padre
    #                              info_actual["mother"], #id de madre
    #                              info_actual["name"],
    #                              info_actual["gender"],
    #                              info_actual["age"],
    #                              info_actual["marital_status"])
    #         self.insertar_persona(raiz, ascendencia)
    #     for descendencia_id in self.descendencia_ids:
    #         info_actual = consultas.Consulta_persona_por_id.consultar_persona(descendencia_id)
    #         descendencia = Nodo_persona(info_actual["id"],
    #                                     info_actual["father"], #id de padre
    #                                     info_actual["mother"], #id de madre
    #                                     info_actual["name"],
    #                                     info_actual["gender"],
    #                                     info_actual["age"],
    #                                     info_actual["marital_status"])
    #         self.insertar_persona(raiz, descendencia)
    #     for hermanos_tios_id in self.hermanos_tios_ids:
    #         info_actual = consultas.Consulta_persona_por_id.consultar_persona(hermanos_tios_id)
    #         hermanos_tios = Nodo_persona(info_actual["id"],
    #                                      info_actual["father"], #id de padre
    #                                      info_actual["mother"], #id de madre
    #                                      info_actual["name"],
    #                                      info_actual["gender"],
    #                                      info_actual["age"],
    #                                      info_actual["marital_status"])
    #         self.insertar_persona(raiz, hermanos_tios)
    #     for sobrinos_primos_id in self.sobrinos_primos_ids:
    #         info_actual = consultas.Consulta_persona_por_id.consultar_persona(sobrinos_primos_id)
    #         sobrinos_primos = Nodo_persona(info_actual["id"],
    #                                        info_actual["father"], #id de padre
    #                                        info_actual["mother"], #id de madre
    #                                        info_actual["name"],
    #                                        info_actual["gender"],
    #                                        info_actual["age"],
    #                                        info_actual["marital_status"])
    #         self.insertar_persona(raiz, sobrinos_primos)
    #         pass

def construir_arbol(personas):
    personas_dict = {p.persona_id: p for p in personas}
    
    for persona in personas:
        if persona.padre_id in personas_dict:
            persona.padre = personas_dict[persona.padre_id]
            personas_dict[persona.padre_id].hijos.append(persona)
        if persona.madre_id in personas_dict:
            persona.madre = personas_dict[persona.madre_id]
            personas_dict[persona.madre_id].hijos.append(persona)
    
    return personas_dict

def crear_grafico_arbol(personas_dict):
    g = nx.DiGraph()
    
    for persona_id, persona in personas_dict.items():
        label = f"{persona.nombre}\n{persona.edad} años"
        g.add_node(persona_id, label=label)
        
        if persona.padre:
            g.add_edge(persona.padre.persona_id, persona_id)
        if persona.madre:
            g.add_edge(persona.madre.persona_id, persona_id)
    
    return g

# Creación del árbol genealógico según tu ejemplo
Rodolfo = Nodo_persona(1, 0, 12, "Rodolfo", "Male", 80, "Single")
Lucho = Nodo_persona(23, 0, 12, "Lucho", "Male", 70, "Married")
Esteban = Nodo_persona(45, 23, 46, "Esteban", "Male", 65, "Married")
Pablo = Nodo_persona(2, 1, 11, "Pablo", "Male", 55, "Single")
ernesto = Nodo_persona(3, 2, 10, "Ernesto", "Male", 25, "Single")
luis = Nodo_persona(4, 3, 9, "Luis", "Male", 5, "Single")
pedro = Nodo_persona(22, 4, 89, "Pedro", "Male", 1, "Married")
luish = Nodo_persona(13, 3, 9, "Hermano", "Male", 15, "Single")
luish2 = Nodo_persona(15, 3, 9, "Hermano2", "Male", 15, "Single")
luish3 = Nodo_persona(16, 3, 9, "Hermano3", "Male", 15, "Single")

arbol=Arbol_genealogico_insertador()
arbol.insertar_persona(pedro,luis)
arbol.insertar_persona(pedro,ernesto)
arbol.insertar_persona(pedro,Pablo)
arbol.insertar_persona(pedro,Esteban)
arbol.insertar_persona(pedro,Lucho)
arbol.insertar_persona(pedro,Rodolfo)
arbol.insertar_persona(pedro,luish)
arbol.insertar_persona(pedro,luish2)
arbol.insertar_persona(pedro,luish3)
pass

# Lista de todas las personas
personas = [Rodolfo, Lucho, Esteban, Pablo, ernesto, luis, pedro, luish, luish2, luish3]

# Construcción del árbol genealógico
personas_dict = construir_arbol(personas)

# Creación del gráfico del árbol genealógico
grafico_arbol = crear_grafico_arbol(personas_dict)

# Visualización del gráfico
pos = graphviz_layout(grafico_arbol, prog="dot")
labels = nx.get_node_attributes(grafico_arbol, 'label')

plt.figure(figsize=(12, 8))
nx.draw(grafico_arbol, pos, labels=labels, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20)
plt.title("Árbol Genealógico")
plt.show()