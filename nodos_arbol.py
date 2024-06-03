class Nodo_persona:
    """Cada uno de estos nodos corresponde a una persona dentro del árbol genealógico.
    """
    persona_id:int=None
    padre_id:int=None
    madre_id:int=None
    padre=None
    madre=None
    conyugue=None
    hijos:list=[] #en la lista de hijos cada hijo se agregará también como un Nodo_persona
    hermanos:list=[] #en la lista de hermanos cada hermano se agregará también como un Nodo_persona
    nombre:str=None
    genero:str=None
    edad:int=None
    estado_civil:str=None
    def __init__(self,persona_id:int,padre_id:int,madre_id:int,nombre:str,genero:str,edad:int,estado_civil:str) -> None:
        """Inicializa un nodo para el árbol genealógico.
        Args:
            persona_id (int): identificación de la persona.
            padre_id (int): identificación del padre de la persona.
            madre_id (int): identificación de la madre de la persona.
            nombre (str): nombre de la persona.
            genero (str): género de la persona("Male" o "Female").
            edad (int): edad de la persona.
            estado_civil (str): estado civil de la persona("Married" o "Single")
        """
        self.persona_id:int=persona_id
        self.padre_id:int=padre_id
        self.madre_id:int=madre_id
        self.nombre:str=nombre
        self.genero=genero
        self.edad:int=edad
        self.estado_civil:str=estado_civil
    
class Agregador_familiares_directos:
    """Esta clase tiene como propósito el agregar a una persona sus familiares directos, como una instancia de Nodo_persona.
    """
    def agregar_padre(persona_raiz:Nodo_persona,padre:Nodo_persona):
        """Le agrega el nodo de padre a un personaje.

        Args:
            persona_raiz (Nodo_persona): personaje.
            padre (Nodo_persona): padre del personaje. Ambos deben ser instancias de Nodo_persona.
        """
        persona_raiz.padre:Nodo_persona=padre
    def agregar_madre(persona_raiz:Nodo_persona,padre:Nodo_persona):
        """Le agrega el nodo de madre a un personaje.

        Args:
            persona_raiz (Nodo_persona): personaje.
            padre (Nodo_persona): madre del personaje. Ambos deben ser instancias de Nodo_persona.
        """
        persona_raiz.padre:Nodo_persona=padre
    def agregar_hermano(persona_raiz:Nodo_persona,hermano:Nodo_persona):
        """agrega un hermano en la lista de hermanos de un personaje, haciendole un append.

        Args:
            persona_raiz (Nodo_persona): personaje.
            hermano (Nodo_persona): hermano/hermana del personaje. Ambos deben ser instancias de Nodo_persona.
        """
        persona_raiz.hermanos.append(hermano)
    def agregar_hijo(persona_raiz:Nodo_persona,hijo:Nodo_persona):
        """agrega un hijo en la lista de hijos de un personaje, haciendole un append.

        Args:
            persona_raiz (Nodo_persona): personaje.
            hermano (Nodo_persona): hijo/hija del personaje. Ambos deben ser instancias de Nodo_persona.
        """
        persona_raiz.hermanos.append(hijo)
    def agregar_conyugue(persona_raiz:Nodo_persona,conyugue:Nodo_persona):
        """le agrega el conyugue, como instancia de Nodo_persona, al nodo del personaje.

        Args:
            persona_raiz (Nodo_persona): personaje.
            conyugue (Nodo_persona): conyugue del personaje. Ambos deben ser instancias de Nodo_persona.
        """
        persona_raiz.conyugue=conyugue