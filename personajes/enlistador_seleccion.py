import consultas

class Enlistador_seleccionador_personajes:
    def __init__(self):
        self.primer_habitante_impreso:int=0
        self.ultimo_habitante_impreso:int=12 #para que llegue a 11
        self.lista_habitantes_disponibles:list=None
        self.lista_habitantes_impresos:list=None

    def consultar_enlistamiento(self):
        self.primer_habitante_impreso:int=0
        self.ultimo_habitante_impreso:int=12 #para que llegue a 11
        self.lista_habitantes_disponibles:list=consultas.Consulta_habitantes_disponibles.consultar_habitantes(100000,100000)
        self._cargar_enlistamiento()

    def avanzar_pagina(self):
        if self.ultimo_habitante_impreso < len(self.lista_habitantes_disponibles):
            self.primer_habitante_impreso += 12
            self.ultimo_habitante_impreso += 12
            self._cargar_enlistamiento()
    def retroceder_pagina(self):
        if self.primer_habitante_impreso >=12:
            self.primer_habitante_impreso -= 12
            self.ultimo_habitante_impreso -= 12
            self._cargar_enlistamiento()

    def _cargar_enlistamiento(self):
        self.lista_habitantes_impresos:list=[]
        for personaje in self.lista_habitantes_disponibles[self.primer_habitante_impreso:self.ultimo_habitante_impreso]:
            self.lista_habitantes_impresos.append(personaje)
        print(self.lista_habitantes_disponibles)
        print(self.lista_habitantes_impresos)