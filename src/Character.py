
import pdb
import requests




class SWCharacter():

    def __init__(
        self, name,
        birth_year,
        eye_color,
        gender,
        hair_color,
        height,
        mass,
        skin_color,
        homeworld,
        films,
        species,
        starships,
        vehicles,
        url,
        created
        ):

        self.name       = name
        self.birth_year = birth_year

        #Requested added methodes
        self.eye_color  = eye_color
        self.gender     = gender
        self.hair_color = hair_color
        self.height     = height
        self.mass       = mass
        self.skin_color = skin_color
        self.homeworld  = homeworld
        self.films      = films
        self.species    = species
        self.starships  = starships
        self.vehicles   = vehicles
        self.url        = url
        self.created    = created

    def __str__(self):
        return {self.name}




def create_character_from_api(char_id):
    """
    Calls SWAPI and creates a SWCharacter Object
    """
    response = requests.get(f'https://swapi.co/api/people/{char_id}')
    resp_json = response.json()

    personage = SWCharacter(

    resp_json["name"],
    resp_json["birth_year"],
    resp_json["eye_color"],
    resp_json["gender"],
    resp_json["hair_color"],
    resp_json["height"],
    resp_json["mass"],
    resp_json["skin_color"],
    resp_json["homeworld"],
    resp_json["films"],
    resp_json["species"],
    resp_json["starships"],
    resp_json["vehicles"],
    resp_json["url"],
    resp_json["created"]

    )

    return personage.name




#TEST
print(create_character_from_api(8))


