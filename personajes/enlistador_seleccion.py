import arbol.consultas as consultas

class Enlistador_seleccionador_personajes:
    """enlista los personajes para el menú
    """
    def __init__(self):
        self.primer_habitante_impreso:int=0
        self.ultimo_habitante_impreso:int=12 #para que llegue a 11
        self.lista_habitantes_disponibles:list=None
        self.lista_habitantes_impresos:list=None

    def consultar_enlistamiento(self):
        """hace la consulta de personajes disponibles al API
        """
        self.primer_habitante_impreso:int=0
        self.ultimo_habitante_impreso:int=12 #para que llegue a 11

        self.lista_habitantes_disponibles:list=[]
        x = 5000
        while x <= 95000:
            try:
                self.lista_habitantes_disponibles.extend(consultas.Consulta_habitantes_disponibles.consultar_habitantes(x))
            except:
                pass
            x += 10000

        self._cargar_enlistamiento()

    def avanzar_pagina(self):
        """pasa un página a la derecha en el menú de selección
        """
        if self.ultimo_habitante_impreso < len(self.lista_habitantes_disponibles):
            self.primer_habitante_impreso += 12
            self.ultimo_habitante_impreso += 12
            self._cargar_enlistamiento()
    def retroceder_pagina(self):
        """pasa un página a la izquierda en el menú de selección
        """
        if self.primer_habitante_impreso >=12:
            self.primer_habitante_impreso -= 12
            self.ultimo_habitante_impreso -= 12
            self._cargar_enlistamiento()

    def _cargar_enlistamiento(self):
        """carga cada sublista para cada página
        """
        self.lista_habitantes_impresos:list=[]
        for personaje in self.lista_habitantes_disponibles[self.primer_habitante_impreso:self.ultimo_habitante_impreso]:
            self.lista_habitantes_impresos.append(personaje)
        print(self.lista_habitantes_disponibles)
        print(self.lista_habitantes_impresos)