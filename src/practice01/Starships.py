import pdb
import requests




class Starship():

    def __init__(

        self, MGLT,
        cargo_capacity,
        consumables,
        cost_in_credits,
        created,
        crew,
        edited,
        hyperdrive_rating,
        length,
        manufacturer,
        max_atmosphering_speed,
        model,
        name,
        passengers,
        films,
        pilots,
        starship_class,
        url

        ):

        self.MGLT                   = MGLT
        self.cargo_capacity         = cargo_capacity
        self.consumables            = consumables
        self.cost_in_credits        = cost_in_credits
        self.created                = created
        self.crew                   = crew
        self.edited                 = edited
        self.hyperdrive_rating      = hyperdrive_rating
        self.length                 = length
        self.manufacturer           = manufacturer
        self.max_atmosphering_speed = max_atmosphering_speed
        self.model                  = model
        self.name                   = name
        self.passengers             = passengers
        self.films                  = films
        self.pilots                 = pilots
        self.starship_class         = starship_class
        self.url                    = url

    def __str__(self):
        return {self.name}



ship_id = int(input('Enter the Starship ID you want to create:'))



def create_starship(shp_id):

    response = requests.get(f'https://swapi.co/api/starships/{shp_id}')
    resp_json = response.json()

    ship = Starship(

    resp_json["MGLT"],
    resp_json["cargo_capacity"],
    resp_json["consumables"],
    resp_json["cost_in_credits"],
    resp_json["created"],
    resp_json["crew"],
    resp_json["edited"],
    resp_json["hyperdrive_rating"],
    resp_json["length"],
    resp_json["manufacturer"],
    resp_json["max_atmosphering_speed"],
    resp_json["model"],
    resp_json["name"],
    resp_json["passengers"],
    resp_json["films"],
    resp_json["pilots"],
    resp_json["starship_class"],
    resp_json["url"],

    )

    print("")
    print('********Starship created sucessfully*********')
    print("")

    return f'Name: {ship.name} | Model: {ship.model} | Max_speed: {ship.max_atmosphering_speed}'





#TEST
print(create_starship(ship_id))
print("")
