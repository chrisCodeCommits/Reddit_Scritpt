import pdb
import requests




class Vehicle():

    def __init__(

        self,
        cargo_capacity,
        consumables,
        cost_in_credits,
        created,
        crew,
        edited,
        length,
        manufacturer,
        max_atmosphering_speed,
        model,
        name,
        passengers,
        pilots,
        films,
        url,
        vehicle_class,

        ):

        self.cargo_capacity         = cargo_capacity
        self.consumables            = consumables
        self.cost_in_credits        = cost_in_credits
        self.created                = created
        self.crew                   = crew
        self.edited                 = edited
        self.length                 = length
        self.manufacturer           = manufacturer
        self.max_atmosphering_speed = max_atmosphering_speed
        self.model                  = model
        self.name                   = name
        self.passengers             = passengers
        self.pilots                 = pilots
        self.films                  = films
        self.url                    = url
        self.vehicle_class          = vehicle_class


    def __str__(self):
        return {self.name}


print("")
vehicle_id = int(input('Enter the vehicle ID you want to create:'))



def create_vehicle(v_id):

    response = requests.get(f'https://swapi.co/api/vehicles/{v_id}')
    resp_json = response.json()

    vehicle = Vehicle(

    resp_json["cargo_capacity"],
    resp_json["consumables"],
    resp_json["cost_in_credits"],
    resp_json["created"],
    resp_json["crew"],
    resp_json["edited"],
    resp_json["length"],
    resp_json["manufacturer"],
    resp_json["max_atmosphering_speed"],
    resp_json["model"],
    resp_json["name"],
    resp_json["passengers"],
    resp_json["pilots"],
    resp_json["films"],
    resp_json["url"],
    resp_json["vehicle_class"]

    )

    print("")
    print('********Vehicle created sucessfully*********')
    print("")

    return f'Name: {vehicle.name} | Model: {vehicle.model} | Max_speed: {vehicle.max_atmosphering_speed}'





#TEST
print(create_vehicle(vehicle_id))
print("")
