
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
    Calls SWAPI and creates a SWCharacter Object with the stats below
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
    resp_json["created"],
    )

    return personage.name


#TEST
print(create_character_from_api(8))





"""
name string -- The name of this person.
birth_year string -- The birth year of the person, using the in-universe standard of BBY or ABY - Before the Battle of Yavin or After the Battle of Yavin. The Battle of Yavin is a battle that occurs at the end of Star Wars episode IV: A New Hope.
eye_color string -- The eye color of this person. Will be "unknown" if not known or "n/a" if the person does not have an eye.
gender string -- The gender of this person. Either "Male", "Female" or "unknown", "n/a" if the person does not have a gender.
hair_color string -- The hair color of this person. Will be "unknown" if not known or "n/a" if the person does not have hair.
height string -- The height of the person in centimeters.
mass string -- The mass of the person in kilograms.
skin_color string -- The skin color of this person.
"""

