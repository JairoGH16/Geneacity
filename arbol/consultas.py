import requests

class Consulta_API_geneacity:
    """Clase que permite utilizar el API de geneacity.
    """
    json:object=None
    url:str=None
    status:int=0
    error:str=None
    def __init__(self,url:str):
        """inicializa una consulta al API de geneacity

        Args:
            url (str): dirección de tipo url a la función a solicitar en el API.
        """
        self.url=url
        response=requests.get(url)
        if response.status_code == 200:
            self.json = response.json()
        else:
            self.error=response.status_code
        
        self.status=self.json["status"]

class Consulta_casas_cercanas:
    """Clase para consultar las casas cercanas a una posición.
    """
    def consultar_casas(x:int,y:int) -> list:
        """Retorna una lista con las casas cercanas (400 pixeles de distancia) a una posición x,y brindada.

        Args:
            x (int): posición x a buscar.
            y (int): posición y a buscar.

        Returns:
            list: lista de casas cercanas, cada casa es un diccionario con su id, su posición x,y y su cantidad de ocupantes.
        """
        consulta=Consulta_API_geneacity(f"https://geneacity.life/API/getHouses/?x={x}&y={y}")
        consulta=consulta.json
        return consulta["houses"]

class Consulta_id_personas_casa:
    """Clase para consultar quienes viven en cierta casa según la id de la respectiva casa.
    """
    def consultar_personas_casa(id_casa:int) -> list:
        """Retorna el listado descriptivo de las personas que residen en una determinda vivienda.

        Args:
            id_casa (int): identificación de la casa a solicitar su información de habitantes.

        Returns:
            list: lista con la información de cada habitante, cada habitante es un diccionario con su nombre, id, género, estado civil y padres.
        """
        consulta=Consulta_API_geneacity(f"https://geneacity.life/API/getHousesResidents/?houseId={id_casa}")
        consulta=consulta.json
        return consulta["residents"]
    
class Consulta_persona_por_id:
    """Consulta la información de un habitante según su respectiva id.
    """
    def consultar_persona(id_persona:int) -> dir:
        """Brinda la información referente a un determinado habitante (Se encuentre vivo o no).

        Args:
            id_persona (int): identificación del habitante que será consultado.

        Returns:
            dir: diccionario que incluye la siguiente información del habitante: id, nombre, género, edad, estado civil, si está vivo, padres y casa.
        """
        consulta=Consulta_API_geneacity(f"https://geneacity.life/API/getInhabitantInformation/?id={id_persona}")
        consulta=consulta.json
        return consulta["inhabitant"]

class Consulta_habitantes_disponibles:
    """Listado descriptivo de habitantes disponibles.
    """
    def consultar_habitantes(x) -> list:
        """Retorna el listado descriptivo de las personas que habitan en el juego limitando el resultado a habitantes en un área de 10.000x10.000 píxeles.

        Returns:
            list: lista con información de los habitantes, cada habitante es un diccionario dentro de la lista y contiene su id, nombre, género y edad.
        """
        consulta=Consulta_API_geneacity(f"https://geneacity.life/API/getAvailableInhabitants/?x={x}&y=0")
        consulta=consulta.json
        return consulta["inhabitants"]

class Seleccionar_habitante:
    """Selecciona un habitante para iniciar la partida.
    """
    def seleccion_habitante(id_habitante:int):
        """Selecciona un habitante disponible para iniciar partida. Una vez seleccionado este habitante ya no podrá ser seleccionada por ningún otro jugador. El jugador seleccionado debe estar soltero y vivo.

        Args:
            id_habitante (int): identificación del habitante.
        """
        consulta=Consulta_API_geneacity(f"https://geneacity.life/API/selectAvailableInhabitant/?id={id_habitante}")
        consulta=consulta.json
        return consulta

class Casar_habitantes:
    """Une dos habitantes de género opuesto en matrimonio, crea una nueva casa para ellos en la posición dada.
    """
    def unir_pareja(id_habitante1:int,id_habitante2:int,x:int,y:int):
        """Permite la unión entre dos personas y la construcción de una nueva casa donde estos habitarán. De la spersonas se verificará que deban estar solteras, tener entre 18 y 45 años y ser de género opuesto.
        De las casas se verificará que no exista otra casa cercana (a menos de 50 píxeles)
        Args:
            id_habitante1 (int): id de uno de los habitantes que se va a unir.
            id_habitante2 (int): id del otro habitante que se va a unir.
            x (int): posición x de la nueva casa para los habitantes que se van a unir.
            y (int): posición y de la nueva casa para los habitantes que se van a unir.
        """
        consulta=Consulta_API_geneacity(f"https://geneacity.life/API/createInhabitantUnion/?idInhabitant1={id_habitante1}&idInhabitant2={id_habitante2}&newHouseXPostition={x}&newHouseYPostition={y}")
        consulta=consulta.json
        return consulta
    
class Crear_habitante:
    """Crea un nuevo habitante a partir de una pareja casada.
    """
    def nacimiento(nombre:str,id_padre_madre:int,genero:str,edad:int): #El genero debe ser "Male" o "Female"
        """Permite crear un nuevo individuo a partir de un padre o madre seleccionado. Se verifica que los padres estén vivos y en un rango de edad entre 21 y 40 años. El nombre del hijo o hija tendrá un límite de 50 caracteres.
        Al nuevo individuo se le asignan los padres correspondientes y la casa de sus procreadores.
        Args:
            nombre (str): nombre del nuevo personaje.
            id_padre_madre (int): id del padre o la madre que invoca a la creación del nuevo personaje.
            genero (str): género del nuevo personaje.
            edad (int): edad con la que el nuevo personaje va a aparecer.
        """
        consulta=Consulta_API_geneacity(f"https://geneacity.life/API/createChildren/?name={nombre}&idInhabitant={id_padre_madre}&gender={genero}&age={edad}")
        consulta=consulta.json
        return consulta