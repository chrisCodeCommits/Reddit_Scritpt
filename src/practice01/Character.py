
import pdb
import requests




class Character():

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



id_number = int(input('Enter the character ID you want to create:'))



def create_character(char_id):
    """
    Calls SWAPI and creates a Character Object
    """
    response = requests.get(f'https://swapi.co/api/people/{char_id}')
    resp_json = response.json()

    personage = Character(

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

    print("")
    print('********Character created sucessfully*********')
    print("")

    return f'Name: {personage.name} | Gender: {personage.gender} | Species: {personage.species}'





#TEST
print(create_character(id_number))
print("")


