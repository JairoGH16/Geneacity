class Nodo_persona:
    """Cada uno de estos nodos corresponde a una persona dentro del árbol genealógico.
    """
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
        self.padre:Nodo_persona=None
        self.madre:Nodo_persona=None
        self.nombre:str=nombre
        self.genero:str=genero
        self.edad:int=edad
        self.estado_civil:str=estado_civil
        self.hermanos:list['Nodo_persona']=[]
        self.hijos:list['Nodo_persona']=[] 
        self.puntuacion:int=None  
        self.grado:int=None
        self.relacion:str=None
        self.puntaje:int=0