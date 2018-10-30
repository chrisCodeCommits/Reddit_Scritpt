
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


sw_api_request = {
   "count":87,
   "next":"https://swapi.co/api/people/?page=2&format=json",
   "previous":"null",
   "results":[
       {
         "name":"Luke Skywalker",
         "height":"172",
         "mass":"77",
         "hair_color":"blond",
         "skin_color":"fair",
         "eye_color":"blue",
         "birth_year":"19BBY",
         "gender":"male",
         "homeworld":"https://swapi.co/api/planets/1/",
         "films":[
            "https://swapi.co/api/films/2/",
            "https://swapi.co/api/films/6/",
            "https://swapi.co/api/films/3/",
            "https://swapi.co/api/films/1/",
            "https://swapi.co/api/films/7/"
         ],
         "species":[
            "https://swapi.co/api/species/1/"
         ],
         "vehicles":[
            "https://swapi.co/api/vehicles/14/",
            "https://swapi.co/api/vehicles/30/"
         ],
         "starships":[
            "https://swapi.co/api/starships/12/",
            "https://swapi.co/api/starships/22/"
         ],
         "created":"2014-12-09T13:50:51.644000Z",
         "edited":"2014-12-20T21:17:56.891000Z",
         "url":"https://swapi.co/api/people/1/"
      },
      {
         "name":"C-3PO",
         "height":"167",
         "mass":"75",
         "hair_color":"n/a",
         "skin_color":"gold",
         "eye_color":"yellow",
         "birth_year":"112BBY",
         "gender":"n/a",
         "homeworld":"https://swapi.co/api/planets/1/",
         "films":[
            "https://swapi.co/api/films/2/",
            "https://swapi.co/api/films/5/",
            "https://swapi.co/api/films/4/",
            "https://swapi.co/api/films/6/",
            "https://swapi.co/api/films/3/",
            "https://swapi.co/api/films/1/"
         ],
         "species":[
            "https://swapi.co/api/species/2/"
         ],
         "vehicles":[

         ],
         "starships":[

         ],
         "created":"2014-12-10T15:10:51.357000Z",
         "edited":"2014-12-20T21:17:50.309000Z",
         "url":"https://swapi.co/api/people/2/"
      },
      {
         "name":"R2-D2",
         "height":"96",
         "mass":"32",
         "hair_color":"n/a",
         "skin_color":"white, blue",
         "eye_color":"red",
         "birth_year":"33BBY",
         "gender":"n/a",
         "homeworld":"https://swapi.co/api/planets/8/",
         "films":[
            "https://swapi.co/api/films/2/",
            "https://swapi.co/api/films/5/",
            "https://swapi.co/api/films/4/",
            "https://swapi.co/api/films/6/",
            "https://swapi.co/api/films/3/",
            "https://swapi.co/api/films/1/",
            "https://swapi.co/api/films/7/"
         ],
         "species":[
            "https://swapi.co/api/species/2/"
         ],
         "vehicles":[

         ],
         "starships":[

         ],
         "created":"2014-12-10T15:11:50.376000Z",
         "edited":"2014-12-20T21:17:50.311000Z",
         "url":"https://swapi.co/api/people/3/"
      },
      {
         "name":"Darth Vader",
         "height":"202",
         "mass":"136",
         "hair_color":"none",
         "skin_color":"white",
         "eye_color":"yellow",
         "birth_year":"41.9BBY",
         "gender":"male",
         "homeworld":"https://swapi.co/api/planets/1/",
         "films":[
            "https://swapi.co/api/films/2/",
            "https://swapi.co/api/films/6/",
            "https://swapi.co/api/films/3/",
            "https://swapi.co/api/films/1/"
         ],
         "species":[
            "https://swapi.co/api/species/1/"
         ],
         "vehicles":[

         ],
         "starships":[
            "https://swapi.co/api/starships/13/"
         ],
         "created":"2014-12-10T15:18:20.704000Z",
         "edited":"2014-12-20T21:17:50.313000Z",
         "url":"https://swapi.co/api/people/4/"
      }
      ]
      }



swapi_people = sw_api_request["results"]

#print(swapi_people)

find_next = 0

for each_character in swapi_people:

    name = swapi_people[find_next]['name']
    specie = swapi_people[find_next]['species'][0]
    gender = swapi_people[find_next]['gender']

    print("")
    print("Name: "+name+" | "+"Gender: male"+" | "+"Specie: "+specie)
    print("")
    find_next +=1

#print(gender)



