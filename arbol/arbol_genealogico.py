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

    def insertar_persona(self, raiz, persona):
        grado = self.__insertar_hermanos_tios(raiz, persona, 0)
        if grado is not None:
            if persona.persona_id not in self.hermanos_tios_ids:
                self.hermanos_tios_ids.append(persona.persona_id)
                self.guardar_json(raiz)
                persona.grado=grado
                if persona.grado == 2:
                    persona.relacion = "Hermano/a"
                elif persona.grado == 3:
                    persona.relacion = "Tio/a"
                elif persona.grado == 4:
                    persona.relacion = "Tio Abuelo"
                elif persona.grado == 5:
                    persona.relacion = "Tio Bisabuelo"
                elif persona.grado == 5:
                    persona.relacion = "Tio Tatarabuelo"
            return grado

        grado = self.__insertar_ascendencia(raiz, persona, 0)
        if grado is not None:
            if persona.persona_id not in self.ascendencia_ids:
                self.ascendencia_ids.append(persona.persona_id)
                self.guardar_json(raiz)
                persona.grado=grado
                if persona.grado == 1:
                    persona.relacion = "Padre/Madre"
                elif persona.grado == 2:
                    persona.relacion = "Abuelo/a"
                elif persona.grado == 3:
                    persona.relacion = "Bisabuelo/a"
                elif persona.grado == 4:
                    persona.relacion = "Tatarabuelo/a"
                elif persona.grado == 5:
                    persona.relacion = "Trastatarabuelo/a"
            return grado

        grado = self.__insertar_descendencia(raiz, persona, 0)
        if grado is not None:
            if persona.persona_id not in self.descendencia_ids:
                self.descendencia_ids.append(persona.persona_id)
                self.guardar_json(raiz)
                persona.grado=grado
                if persona.grado == 1:
                    persona.relacion = "Hijo/a"
                elif persona.grado == 2:
                    persona.relacion = "Nieto/a"
                elif persona.grado == 3:
                    persona.relacion = "Bisnieto/a"
                elif persona.grado == 4:
                    persona.relacion = "Tataranieto/a"
                elif persona.grado == 5:
                    persona.relacion = "Trastataranieto"
            return grado

        grado = self.__insertar_sobrinos_primos(raiz, persona, 0)
        if grado is not None:
            if persona.persona_id not in self.sobrinos_primos_ids:
                self.sobrinos_primos_ids.append(persona.persona_id)
                self.guardar_json(raiz)
                persona.grado=grado
                if persona.grado == 3:
                    persona.relacion = "Sobrino/a"
                elif persona.grado == 4 and persona.padre.relacion == "Sobrino/a":
                    persona.relacion = "Sobrino nieto"
                elif persona.grado == 4 and persona.padre.relacion == "Tio/a":
                    persona.relacion = "Primo/a"
                elif persona.grado == 5 and persona.padre.relacion == "Sobrino nieto":
                    persona.relacion = "Sobrino bisnieto"
                elif persona.grado == 5 and persona.padre.relacion == "Primo/a":
                    persona.relacion = "Sobrino Segundo"
                elif persona.grado == 5:
                    persona.relacion = "Tio Segundo"
                elif persona.grado == 6 and persona.padre.relacion == "Sobrino bisnieto":
                    persona.relacion = "Sobrino tataranieto"
                elif persona.grado == 6 and persona.padre.relacion == "Sobrino Segundo":
                    persona.relacion = "Sobrino nieto segundo"
                elif persona.grado == 6 and persona.padre.relacion == "Tio Segundo":
                    persona.relacion = "Primo segundo"
                elif persona.grado == 6:
                    persona.relacion = "Tio abuelo segundo"
                elif persona.grado == 7 and persona.padre.relacion == "Sobrino nieto segundo":
                    persona.relacion = "Sobrino bisnieto segundo"
                elif persona.grado == 7 and persona.padre.relacion == "Primo segundo":
                    persona.relacion = "Sobrino tercero"
                elif persona.grado == 7 and persona.padre.relacion == "Tio abuelo segundo":
                    persona.relacion = "Tio tercero"
                elif persona.grado == 7:
                    persona.relacion = "Tio bisabuelo segundo"
                elif persona.grado == 8 and persona.padre.relacion == "Sobrino tercero":
                    persona.relacion = "Sobrino nieto tercero"
                elif persona.grado == 8 and persona.padre.relacion == "Tio tercero":
                    persona.relacion = "Primo tercero"
                elif persona.grado == 8 and persona.padre.relacion == "Tio bisabuelo segundo":
                    persona.relacion = "Tio abuelo tercero"
                elif persona.grado == 9 and persona.padre.relacion == "Primo tercero":
                    persona.relacion = "Sobrino cuarto"
                elif persona.grado == 9 and persona.padre.relacion == "Tio abuelo tercero":
                    persona.relacion = "Tio cuarto"
                elif persona.grado == 10 and persona.padre.relacion == "Tio cuarto":
                    persona.relacion = "Primo cuarto"
            return grado

        return None
    
    def __insertar_hermanos_tios(self, raiz: Nodo_persona, persona: Nodo_persona, grado: int):
        if raiz:
            if (raiz.padre_id == persona.padre_id and raiz.padre_id != 0) or (raiz.madre_id == persona.madre_id and raiz.madre_id != 0):
                if persona not in raiz.hermanos:
                    raiz.hermanos.append(persona)
                if raiz not in persona.hermanos:
                    persona.hermanos.append(raiz)
                grado += 2
                return grado  # Encontrado al mismo nivel
            grado_padre = self.__insertar_hermanos_tios(raiz.padre, persona, grado + 1)
            if grado_padre is not None:
                return grado_padre
            grado_madre = self.__insertar_hermanos_tios(raiz.madre, persona, grado + 1)
            if grado_madre is not None:
                return grado_madre
        return None
    
    def __insertar_ascendencia(self, raiz: Nodo_persona, persona: Nodo_persona, grado: int):
        if raiz:
            if raiz.padre_id == persona.persona_id:
                if raiz not in persona.hijos:
                    raiz.padre = persona
                    persona.hijos.append(raiz)
                return grado + 1
            elif raiz.madre_id == persona.persona_id:
                if raiz not in persona.hijos:
                    raiz.madre = persona
                    persona.hijos.append(raiz)
                return grado + 1
            grado_padre = self.__insertar_ascendencia(raiz.padre, persona, grado + 1)
            if grado_padre is not None:
                return grado_padre
            grado_madre = self.__insertar_ascendencia(raiz.madre, persona, grado + 1)
            if grado_madre is not None:
                return grado_madre
        return None
    
    def __insertar_descendencia(self, raiz: Nodo_persona, persona: Nodo_persona, grado: int):
        if raiz:
            if raiz.persona_id == persona.padre_id:
                if persona not in raiz.hijos:
                    raiz.hijos.append(persona)
                    persona.padre = raiz
                return grado + 1
            elif raiz.persona_id == persona.madre_id:
                if persona not in raiz.hijos:
                    raiz.hijos.append(persona)
                    persona.madre = raiz
                return grado + 1
            for hijo in raiz.hijos:
                grado_hijo = self.__insertar_descendencia(hijo, persona, grado + 1)
                if grado_hijo is not None:
                    return grado_hijo
        return None
    
    def __insertar_sobrinos_primos(self, raiz: Nodo_persona, persona: Nodo_persona, grado: int):
        if raiz:
            for hermano in raiz.hermanos:
                grado_descendencia = self.__insertar_descendencia(hermano, persona, grado + 2)
                if grado_descendencia is not None:
                    return grado_descendencia
            grado_padre = self.__insertar_sobrinos_primos(raiz.padre, persona, grado + 1)
            if grado_padre is not None:
                return grado_padre
            grado_madre = self.__insertar_sobrinos_primos(raiz.madre, persona, grado + 1)
            if grado_madre is not None:
                return grado_madre
        return None

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
        label = f"{persona.nombre}\n{persona.edad} años\n{persona.relacion}"
        g.add_node(persona_id, label=label)
        
        if persona.padre:
            g.add_edge(persona.padre.persona_id, persona_id)
        if persona.madre:
            g.add_edge(persona.madre.persona_id, persona_id)
    
    return g

# Creación del árbol genealógico según tu ejemplo
Rodolfo = Nodo_persona(1, 0, 12, "Rodolfo", "Male", 80, "Single")
Lucho = Nodo_persona(23, 1, 12, "Lucho", "Male", 70, "Married")
Esteban = Nodo_persona(45, 23, 46, "Esteban", "Male", 65, "Married")
Pablo = Nodo_persona(2, 1, 11, "Pablo", "Male", 55, "Single")
ernesto = Nodo_persona(3, 2, 10, "Ernesto", "Male", 25, "Single")
luis = Nodo_persona(4, 3, 9, "Luis", "Male", 5, "Single")
pedro = Nodo_persona(22, 4, 89, "Pedro", "Male", 1, "Married")
luish = Nodo_persona(13, 3, 9, "Hermano", "Male", 15, "Single")
luish2 = Nodo_persona(15, 3, 9, "Hermano2", "Male", 15, "Single")
luish3 = Nodo_persona(16, 3, 9, "Hermano3", "Male", 15, "Single")
estebanh = Nodo_persona(88, 45, 123, "HijoE", "Male", 15, "Single")
estebanhh = Nodo_persona(86, 88, 122, "HijoEE", "Male", 15, "Single")
pedroh = Nodo_persona(75, 22, 121, "HijoP", "Male", 15, "Single")
pedrohh = Nodo_persona(74, 75, 120, "HijoPP", "Male", 15, "Single")

arbol=Arbol_genealogico_insertador()
pedro.puntuacion = 0
pedro.puntuacion+=(arbol.insertar_persona(pedro,luis)*5)
print(pedro.puntuacion)
arbol.insertar_persona(pedro,ernesto)
arbol.insertar_persona(pedro,Pablo)
arbol.insertar_persona(pedro,Rodolfo)
grado2 = arbol.insertar_persona(pedro,luish)
arbol.insertar_persona(pedro,luish2)
arbol.insertar_persona(pedro,luish3)
grado1 = arbol.insertar_persona(pedro,Lucho)
grado = arbol.insertar_persona(pedro,Esteban)
grado3 = arbol.insertar_persona(pedro, estebanh)
gradof = arbol.insertar_persona(pedro, estebanhh)
arbol.insertar_persona(pedro, pedroh)
arbol.insertar_persona(pedro, pedrohh)
pass

# Lista de todas las personas
personas = [Rodolfo, Lucho, Esteban, Pablo, ernesto, luis, pedro, luish, luish2, luish3, estebanh, estebanhh, pedroh, pedrohh]

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
