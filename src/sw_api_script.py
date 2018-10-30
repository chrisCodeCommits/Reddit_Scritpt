
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
##################################################################
import requests
import json






# Pulling data from the API
sw_api_request = requests.get("https://swapi.co/api/people/?page=2&format=json")

# Making the data usuable for Python
sw_usable_data = json.load(sw_api_request)



# Self explanatory
swapi_people = sw_usable_data["results"]



# This variable will act as a counter in order to make the forloop
# throughout each characheter details possible.
find_next = 0


for each_character in swapi_people:

    name = swapi_people[find_next]['name']
    specie = swapi_people[find_next]['species'][0]
    gender = swapi_people[find_next]['gender']

    # Adding a conditional statement in order to only output males characters
    if gender == "male":

        print("")
        print("Name: "+name+" | "+"Gender: male"+" | "+"Specie: "+specie)
        print("")

    # Refers to the counter to make the loop possible! by each iteration
    find_next += 1





