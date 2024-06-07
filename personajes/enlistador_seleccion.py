import consultas

class Enlistador_seleccionador_personajes:
    def __init__(self):
        self.primer_habitante_impreso:int=0
        self.ultimo_habitante_impreso:int=12
        self.lista_habitantes_disponibles:list=None
        self.lista_habitantes_impresos:list=None
    def carga_inicial(self):
        self.lista_habitantes_disponibles:list=consultas.Consulta_habitantes_disponibles.consultar_habitantes()
        self.lista_habitantes_impresos:list=[]
        for personaje in self.lista_habitantes_disponibles[self.primer_habitante_impreso:self.ultimo_habitante_impreso]:
            if int(personaje["age"])>=0: #Validar que la edad sea valida.
                self.lista_habitantes_impresos.append(personaje)
        print(self.lista_habitantes_impresos)