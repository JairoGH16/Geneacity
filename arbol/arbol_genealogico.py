import json
import consultas
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
        self.puntaje:int = 0
        self.actualizar_registro = "archivos_registrados.json"

    def insertar_persona(self, raiz, persona):
        grado = self.__insertar_hermanos_tios(raiz, persona, 0)
        if grado is not None:
            if persona.persona_id not in self.hermanos_tios_ids:
                self.hermanos_tios_ids.append(persona.persona_id)
                self.guardar_json(raiz)
                persona.grado=grado
                if persona.relacion == None:
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
                personas.append(persona)
            self.puntaje+=(grado*5)
            print(self.puntaje)
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
                personas.append(persona)
            self.puntaje+=(grado*5)
            print(self.puntaje)
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
                personas.append(persona)
            self.puntaje+=(grado*5)
            print(self.puntaje)
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
                personas.append(persona)
            self.puntaje+=(grado*5)
            print(self.puntaje)
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
        nombre_archivo = f"arbol_genealogico{raiz.persona_id}.json"
        with open(nombre_archivo, "w") as file:
            json.dump(data, file, indent=4)
        
        arbol_grafico()

    def cargar_json(self, raiz):
        personas.append(raiz)
        nombre_archivo = f"arbol_genealogico{raiz.persona_id}.json"
        with open(nombre_archivo, "r") as file:
            data = json.load(file)
            self.hermanos_tios_ids = data.get("hermanos_tios", [])
            self.ascendencia_ids = data.get("ascendencia", [])
            self.descendencia_ids = data.get("descendencia", [])
            self.sobrinos_primos_ids = data.get("sobrinos_primos", [])


    def cargar_arbol(self, raiz):
        info_persona = consultas.Consulta_persona_por_id.consultar_persona(raiz)
        raiz_real = Nodo_persona(info_persona["id"],
                                 info_persona["father"],
                                 info_persona["mother"],
                                 info_persona["name"],
                                 info_persona["gender"],
                                 info_persona["age"],
                                 info_persona["marital_status"])
        
        info_persona = consultas.Consulta_persona_por_id.consultar_persona(raiz_real.padre_id)
        padre_real = Nodo_persona(info_persona["id"],
                                 info_persona["father"],
                                 info_persona["mother"],
                                 info_persona["name"],
                                 info_persona["gender"],
                                 info_persona["age"],
                                 info_persona["marital_status"])
        
        info_persona = consultas.Consulta_persona_por_id.consultar_persona(raiz_real.madre_id)
        madre_real = Nodo_persona(info_persona["id"],
                                 info_persona["father"],
                                 info_persona["mother"],
                                 info_persona["name"],
                                 info_persona["gender"],
                                 info_persona["age"],
                                 info_persona["marital_status"])
        
        self.insertar_persona(raiz_real, padre_real)
        self.insertar_persona(raiz_real, madre_real)

        self.cargar_json(raiz_real)
        for ascendencia_id in self.ascendencia_ids:
            info_actual = consultas.Consulta_persona_por_id.consultar_persona(ascendencia_id)
            ascendencia = Nodo_persona(info_actual["id"],
                                 info_actual["father"], #id de padre
                                 info_actual["mother"], #id de madre
                                 info_actual["name"],
                                 info_actual["gender"],
                                 info_actual["age"],
                                 info_actual["marital_status"])
            self.insertar_persona(raiz_real, ascendencia)
            personas.append(ascendencia)
        for descendencia_id in self.descendencia_ids:
            info_actual = consultas.Consulta_persona_por_id.consultar_persona(descendencia_id)
            descendencia = Nodo_persona(info_actual["id"],
                                        info_actual["father"], #id de padre
                                        info_actual["mother"], #id de madre
                                        info_actual["name"],
                                        info_actual["gender"],
                                        info_actual["age"],
                                        info_actual["marital_status"])
            self.insertar_persona(raiz_real, descendencia)
            personas.append(descendencia)
        for hermanos_tios_id in self.hermanos_tios_ids:
            info_actual = consultas.Consulta_persona_por_id.consultar_persona(hermanos_tios_id)
            hermanos_tios = Nodo_persona(info_actual["id"],
                                         info_actual["father"], #id de padre
                                         info_actual["mother"], #id de madre
                                         info_actual["name"],
                                         info_actual["gender"],
                                         info_actual["age"],
                                         info_actual["marital_status"])
            self.insertar_persona(raiz_real, hermanos_tios)
            personas.append(hermanos_tios)
        for sobrinos_primos_id in self.sobrinos_primos_ids:
            info_actual = consultas.Consulta_persona_por_id.consultar_persona(sobrinos_primos_id)
            sobrinos_primos = Nodo_persona(info_actual["id"],
                                           info_actual["father"], #id de padre
                                           info_actual["mother"], #id de madre
                                           info_actual["name"],
                                           info_actual["gender"],
                                           info_actual["age"],
                                           info_actual["marital_status"])
            self.insertar_persona(raiz_real, sobrinos_primos)
            personas.append(sobrinos_primos)
        
        arbol_grafico()
        pass
    
    def actualizar_registro(self, nombre_archivo):
        try:
            with open(self.archivo_registro, "r") as file:
                archivos = json.load(file)
        except FileNotFoundError:
            archivos = []

        if nombre_archivo not in archivos:
            archivos.append(nombre_archivo)

        with open(self.archivo_registro, "w") as file:
            json.dump(archivos, file, indent=4)

    def cargar_registro(self):
        try:
            with open(self.archivo_registro, "r") as file:
                archivos = json.load(file)
                return archivos
        except FileNotFoundError:
            return []

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

# Lista de todas las personas
personas = []

def arbol_grafico():
    # Construcción del árbol genealógico
    personas_dict = construir_arbol(personas)

    # Creación del gráfico del árbol genealógico
    grafico_arbol = crear_grafico_arbol(personas_dict)

    # Visualización del gráfico
    pos = graphviz_layout(grafico_arbol, prog="dot")
    labels = nx.get_node_attributes(grafico_arbol, 'label')

    plt.figure(figsize=(12, 8))
    nx.draw(grafico_arbol, pos, labels=labels, with_labels=True, node_size=5000, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20)
    plt.title("Árbol Genealógico")
    plt.show()

arbol = Arbol_genealogico_insertador()
arbol.cargar_arbol(5118)