
import pdb

class SWCharacter():

    def __init__(self, name, birth_year, gender, hair_color, height, mass, skin_color):

        self.name       = name
        self.birth_year = birth_year

        #Requested added methodes
        self.eye_color  = eye_color
        self.gender     = gender
        self.hair_color = hair_color
        self.height     = height
        self.mass       = mass
        self.skin_color = skin_color



    def __str__(self):
        return {self.name}

    def __repr__(self):
        return f'SWCharacter("{self.name}")'

    def introduce_myself(self):
        print(f"Hi!, my name is {self.name}. I was born in {self.birth_year}.")

    def load_char_from_api(self, char_id):


# luke = SWCharacter("Luke Skywalker", 1973)
# r2 = SWCharacter("R2-D2", 293994)


def create_character_from_api(char_id):
    """
    Calls SWAPI and creates a SWCharacter Object with the stats below
    """
    pass



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

""""
NOT THESE
homeworld string -- The URL of a planet resource, a planet that this person was born on or inhabits.
films array -- An array of film resource URLs that this person has been in.
species array -- An array of species resource URLs that this person belongs to.
starships array -- An array of starship resource URLs that this person has piloted.
vehicles array -- An array of vehicle resource URLs that this person has piloted.
url string -- the hypermedia URL of this resource.
created string -- the ISO 8601 date format of the time that this resource was created.
edited strin
"""
