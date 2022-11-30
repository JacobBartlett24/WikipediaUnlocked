from collections import deque
import json
import re
import time
from typing import cast
import sys
import threading

sys.setrecursionlimit(100000000)

class Movie(): 
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name
        self.movies_list = []
        self.movies_count = 1

    def addToList(self, movie):
        if(movie not in self.movies_list):
            self.movies_list.append(movie)


moviesList = []
actorDict = {}
movieDict = {}

testList = [{"title":"The Killer Must Kill Again","cast":["[[George Hilton (actor)|George Hilton]]","[[Antoine Saint-John]]","[[Femi Benussi]]","[[Cristina Galbó]]","[[Eduardo Fajardo]]","[[Tere Velázquez]]","[[Alessio Orano]]"],"directors":["[[Luigi Cozzi]]"],"producers":["Sergio Gobbi","[[Umberto Lenzi]] <small>(as Umberto Linzi)</small>","Giuseppe Tortorella"],"companies":["Albione Cinematografica","Git International Film","Paris-Cannes Productions"],"year":1975},
{"title":"Silent Action","cast":["[[Mel Ferrer]]","[[Brad Pitt]]","[[Tomas Milian]]","[[Luc Merenda]]","[[Michele Gammino]]","[[Paola Tedesco]]","[[Gianfranco Barra]]","Carlo Alighiero","[[Antonio Casale]]","Gianni Di Benedetto","[[Claudio Gora]]","[[Clara Colosimo]]","[[Arturo Dominici]]"],"directors":["[[Sergio Martino]]"],"producers":["[[Luciano Martino]]"],"companies":["Flora Film","Medusa Distribuzione","Medusa"],"year":1975},
{"title":"Manzil (1979 film)","cast":["[[Amitabh Bachchan]]","[[Moushumi Chatterjee]]","[[Rakesh Pandey]]","[[Satyen Kappu]]","[[Urmila Bhatt]]","[[Lalita Pawar]]","[[Shreeram Lagoo]]","[[A. K. Hangal]]","[[C. S. Dubey]]"],"directors":["[[Basu Chatterjee]]"],"producers":["Jai Pawar","Raj Prakash","Rajiv Suri"],"year":1979},
{"title":"Saajan Ki Baahon Mein","cast":["[[Rishi Kapoor]]","Sumeet Saigal","[[Raveena Tandon]]","[[Tabu (actress)|Tabu]]","[[Prem Chopra]]","[[Deven Verma]]","[[Laxmikant Berde]]","[[Pran (actor)|Pran]]","[[Saeed Jaffrey]]"],"directors":["Jay Prakash"],"producers":["Dinesh B. Patel"],"year":1995}]
def load():
    with open('data.txt') as f:
        for jsonObj in f:
            movieDict = json.loads(jsonObj)
            moviesList.append(movieDict)
    return moviesList

def createMovieDict():
    sampleDict = {}

    for movie in moviesList:
        tempList = []
        for i in range(0,len(movie['cast'])):
            actor = re.sub(r"[\[\]]",'',movie['cast'][i])
            tempList.append(actor)
        sampleDict[movie['title']] = tempList
    return sampleDict

def movieCount():
    
    for movie in moviesList:
        #keys = movie.keys()
        #if('year' in keys and int(movie['year']) > 1999 and int(movie['year']) < 2001):

            for i in range(0,len(movie['cast'])):
                
                actor = re.sub(r"[\[\]]",'',movie['cast'][i])

                if actor in actorDict.keys():
                    actorDict[actor].append(movie['title'])
                else:
                    actorDict[actor] = [movie['title']]
    actorDict['Kevin Bacon'].insert(0,'Starting Over (1979 film)')
    
    actorDict['Wallace Shawn'].insert(0,'Clueless')
    actorDict['Paul Rudd'].insert(0,'Clueless')

    json.dump(actorDict, open("actor_data.json", 'w'), indent=2)
    return actorDict
                    
def setWeights(actorDict,start):
    pass
    #Set start node to start
    #some type of graph traversel (DFS ~) sets starting weights of graph
    #Call function to traverse graph

results = []
for actor in actorDict.keys():
    results.append(actor)


def bfs(actorDict,start,target,visited,path):
    if len(path) > 3:
       del path[:]
       start = og
       #bfs(actorDict, start, target, visited, path)

    visited.append(start)
    for currMovie in actorDict[start]:
        #actors in the cast of the movies start is in
        for actor in movieDict[currMovie]:
            if(actor == target):
                print(currMovie)
                print(path)
                exit(0)
                
            elif(actor not in visited and currMovie not in path):
                path.append(currMovie)
                bfs(actorDict,actor,target,visited,path)
    
    # One of the searches we were taught
    # Print the distance, # of traversals to measure performance
    # Extra: Take that information and feed it to AI to set different weights later

def dfs(actorDict,start,target):
    pass

#movie_file = open("actor_data.txt", "w")
#movieCount()
#movie_file.close()
#important = movieCount()
#traverseGraph(important, start="Kevin Bacon", target="Brad Pitt")

moviesList = load()
movieDict = createMovieDict()
actorDict = movieCount()
actorDictLength = (len(actorDict))

og = 'Kevin Bacon'

print(bfs(actorDict,start=og, target='Paul Rudd',visited=[],path = []))
