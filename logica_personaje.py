from nodos_arbol import Nodo_persona
import consultas

"""             Selección del personaje y creación de nodos iniciales para el árbol genealógico"""

#seleccionar_habitante
#establecer id de habitante como id_personaje
id_personaje=0
"""Personaje seleccionado"""
#obtener información del habitante seleccionado
info_seleccionado=consultas.Consulta_persona_por_id.consultar_persona(id_personaje)
#crear nodo de personaje seleccionado
personaje_seleccionado=Nodo_persona(info_seleccionado["id"],
                                 info_seleccionado["father"],
                                 info_seleccionado["mother"],
                                 info_seleccionado["name"],
                                 info_seleccionado["gender"],
                                 info_seleccionado["age"],
                                 info_seleccionado["marital_status"])
"""Padre del personaje seleccionado"""
#obtener información del padre del habitante seleccionado
info_padre_seleccionado=consultas.Consulta_persona_por_id.consultar_persona(personaje_seleccionado.padre_id)
#crear nodo de padre de personaje seleccionado
padre_seleccionado=Nodo_persona(info_padre_seleccionado["id"],
                                 info_padre_seleccionado["father"],
                                 info_padre_seleccionado["mother"],
                                 info_padre_seleccionado["name"],
                                 info_padre_seleccionado["gender"],
                                 info_padre_seleccionado["age"],
                                 info_padre_seleccionado["marital_status"])
"""Madre del personaje seleccionado"""
#obtener información de la madre del habitante seleccionado
info_madre_seleccionado=consultas.Consulta_persona_por_id.consultar_persona(personaje_seleccionado.madre_id)
#crear nodo de madre de personaje seleccionado
madre_seleccionado=Nodo_persona(info_madre_seleccionado["id"],
                                 info_madre_seleccionado["father"],
                                 info_madre_seleccionado["mother"],
                                 info_madre_seleccionado["name"],
                                 info_madre_seleccionado["gender"],
                                 info_madre_seleccionado["age"],
                                 info_madre_seleccionado["marital_status"])