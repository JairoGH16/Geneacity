from arbol.nodos_arbol import Nodo_persona
import consultas

class Inicializador_arbol:
    def inicializar_arbol(self,id_personaje:int):
        """           Creación de nodos del personaje seleccionado y creación de nodos iniciales para el árbol genealógico"""
        #seleccionar_habitante
        #establecer id de habitante como id_personaje
        """Personaje seleccionado"""
        #obtener información del habitante seleccionado
        info_seleccionado=consultas.Consulta_persona_por_id.consultar_persona(id_personaje)
        #crear nodo de personaje seleccionado
        personaje_seleccionado=Nodo_persona(info_seleccionado["id"],
                                         info_seleccionado["father"], #id de padre
                                         info_seleccionado["mother"], #id de madre
                                         info_seleccionado["name"],
                                         info_seleccionado["gender"],
                                         info_seleccionado["age"],
                                         info_seleccionado["marital_status"])
        """Padre del personaje seleccionado"""
        #obtener información del padre del habitante seleccionado
        info_padre_seleccionado=consultas.Consulta_persona_por_id.consultar_persona(personaje_seleccionado.padre_id)
        #crear nodo de padre de personaje seleccionado
        padre_seleccionado=Nodo_persona(info_padre_seleccionado["id"],
                                         info_padre_seleccionado["father"], #id de padre
                                         info_padre_seleccionado["mother"], #id de madre
                                         info_padre_seleccionado["name"],
                                         info_padre_seleccionado["gender"],
                                         info_padre_seleccionado["age"],
                                         info_padre_seleccionado["marital_status"])
        """Madre del personaje seleccionado"""
        #obtener información de la madre del habitante seleccionado
        info_madre_seleccionado=consultas.Consulta_persona_por_id.consultar_persona(personaje_seleccionado.madre_id)
        #crear nodo de madre de personaje seleccionado
        madre_seleccionado=Nodo_persona(info_madre_seleccionado["id"],
                                         info_madre_seleccionado["father"], #id de padre
                                         info_madre_seleccionado["mother"], #id de madre
                                         info_madre_seleccionado["name"],
                                         info_madre_seleccionado["gender"],
                                         info_madre_seleccionado["age"],
                                         info_madre_seleccionado["marital_status"])
        #Agregar padre y madre al personaje seleccionado
        personaje_seleccionado.padre=padre_seleccionado
        personaje_seleccionado.madre=madre_seleccionado
        padre_seleccionado.hijos.append(personaje_seleccionado) #agrega el personaje seleccionado en la lista de hijos de su padre
        madre_seleccionado.hijos.append(personaje_seleccionado) #agrega el personaje seleccionado en la lista de hijos de su madre

        return personaje_seleccionado