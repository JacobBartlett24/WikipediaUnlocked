import json
import re
import time
from typing import cast

class Actor(): 
    def __init__(self, line, name):
        self.line = line
        self.name = name
        self.movies_list = []
        self.movies_count = 1

    def addToList(self, movie):
        if(movie not in self.movies_list):
            self.movies_list.append(movie)


moviesList = []
actorList = {}
actorJsonList = []

testList = [{"title":"The Killer Must Kill Again","cast":["[[George Hilton (actor)|George Hilton]]","[[Antoine Saint-John]]","[[Femi Benussi]]","[[Cristina Galbó]]","[[Eduardo Fajardo]]","[[Tere Velázquez]]","[[Alessio Orano]]"],"directors":["[[Luigi Cozzi]]"],"producers":["Sergio Gobbi","[[Umberto Lenzi]] <small>(as Umberto Linzi)</small>","Giuseppe Tortorella"],"companies":["Albione Cinematografica","Git International Film","Paris-Cannes Productions"],"year":1975},
{"title":"Silent Action","cast":["[[Mel Ferrer]]","[[Brad Pitt]]","[[Tomas Milian]]","[[Luc Merenda]]","[[Michele Gammino]]","[[Paola Tedesco]]","[[Gianfranco Barra]]","Carlo Alighiero","[[Antonio Casale]]","Gianni Di Benedetto","[[Claudio Gora]]","[[Clara Colosimo]]","[[Arturo Dominici]]"],"directors":["[[Sergio Martino]]"],"producers":["[[Luciano Martino]]"],"companies":["Flora Film","Medusa Distribuzione","Medusa"],"year":1975},
{"title":"Manzil (1979 film)","cast":["[[Amitabh Bachchan]]","[[Moushumi Chatterjee]]","[[Rakesh Pandey]]","[[Satyen Kappu]]","[[Urmila Bhatt]]","[[Lalita Pawar]]","[[Shreeram Lagoo]]","[[A. K. Hangal]]","[[C. S. Dubey]]"],"directors":["[[Basu Chatterjee]]"],"producers":["Jai Pawar","Raj Prakash","Rajiv Suri"],"year":1979},
{"title":"Saajan Ki Baahon Mein","cast":["[[Rishi Kapoor]]","Sumeet Saigal","[[Raveena Tandon]]","[[Tabu (actress)|Tabu]]","[[Prem Chopra]]","[[Deven Verma]]","[[Laxmikant Berde]]","[[Pran (actor)|Pran]]","[[Saeed Jaffrey]]"],"directors":["Jay Prakash"],"producers":["Dinesh B. Patel"],"year":1995}]

with open('data.txt') as f:
    for jsonObj in f:
        movieDict = json.loads(jsonObj)
        moviesList.append(movieDict)

def movieCount():
    
    for movie in moviesList:
        for i in range(0,len(movie['cast'])):
            
            actor = re.sub(r"[\[\]]",'',movie['cast'][i])

            if actor in actorList.keys():
                actorList[actor].append(movie['title'])
            else:
                actorList[actor] = [movie['title']]
            



            """ if(actor not in actorList):

                #actorJson = 
                #                "name": actor,
                #                "count": "0",
                #            }
                actorList.append(actor)
                 """
                #actorJsonList.append(actorJson)
    

    json.dump(actorList, open("actor_data.json", 'w'), indent=2)
    
    createGraph(actorList,moviesList)
                    
def createGraph(actorList, moviesList):
    
    

    """ matrix = [[0 for x in range(len(actorList))] for y in range (len(moviesList))]
    
    print('Starting matrix creation...')
    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            for castMember in moviesList[j]['cast']:
                actor = re.sub(r"[\[\]]",'',castMember)
                if(actor == actorList[i]):
                    matrix[i][j] = 1
    print(matrix) """

#movie_file = open("actor_data.txt", "w")
#movieCount(movie_file)
#movie_file.close()
movieCount()

