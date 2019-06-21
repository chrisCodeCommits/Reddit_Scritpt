
###### SWAPI TASKS TO COMPLETE ####################################
'''
STEP 1
fetch the Json data from SWAPI and asign it to a variable to use
in my code.

STEP 2
parse the dictionary to output:
- All male characters names
- Species
'''
####################################################################################
import requests
import pdb



def get_all_male_people():
    next_endpoint = "https://swapi.co/api/people/"
    all_males = []

    while next_endpoint:
        print(next_endpoint)
        response = requests.get(next_endpoint)

        response_json = response.json()
        people = response_json["results"]
        next_endpoint = response_json['next']

        for character in people:
            if character['gender'] == "male":
                all_males.append(character)

    print("All done!")
    return all_males


males = get_all_male_people()

###### SWAPI TASKS TO COMPLETE ####################################
'''
STEP 1
fetch the Json data from SWAPI and asign it to a variable to use
in my code.

STEP 2
parse the dictionary to output:
- All male characters names
- Species
'''
####################################################################################
import requests
import pdb




def get_all_male_people():
    next_endpoint = "https://swapi.co/api/people/"
    all_males = []

    while next_endpoint:
        print(next_endpoint)
        response = requests.get(next_endpoint)

        response_json = response.json()
        people = response_json["results"]
        next_endpoint = response_json['next']

        for character in people:
            if character['gender'] == "male":
                all_males.append(character)

    print("All done!")
    return all_males


males = get_all_male_people()
