import json
import re
from typing import cast
import sys

sys.setrecursionlimit(100000000)

moviesList = []
actorDict = {}
movieDict = {}

testList = [{"title":"The Killer Must Kill Again","cast":["[[George Hilton (actor)|George Hilton]]","[[Antoine Saint-John]]","[[Femi Benussi]]","[[Cristina Galbó]]","[[Eduardo Fajardo]]","[[Tere Velázquez]]","[[Alessio Orano]]"],"directors":["[[Luigi Cozzi]]"],"producers":["Sergio Gobbi","[[Umberto Lenzi]] <small>(as Umberto Linzi)</small>","Giuseppe Tortorella"],"companies":["Albione Cinematografica","Git International Film","Paris-Cannes Productions"],"year":1975},
{"title":"Silent Action","cast":["[[Mel Ferrer]]","[[Brad Pitt]]","[[Tomas Milian]]","[[Luc Merenda]]","[[Michele Gammino]]","[[Paola Tedesco]]","[[Gianfranco Barra]]","Carlo Alighiero","[[Antonio Casale]]","Gianni Di Benedetto","[[Claudio Gora]]","[[Clara Colosimo]]","[[Arturo Dominici]]"],"directors":["[[Sergio Martino]]"],"producers":["[[Luciano Martino]]"],"companies":["Flora Film","Medusa Distribuzione","Medusa"],"year":1975},
{"title":"Manzil (1979 film)","cast":["[[Amitabh Bachchan]]","[[Moushumi Chatterjee]]","[[Rakesh Pandey]]","[[Satyen Kappu]]","[[Urmila Bhatt]]","[[Lalita Pawar]]","[[Shreeram Lagoo]]","[[A. K. Hangal]]","[[C. S. Dubey]]"],"directors":["[[Basu Chatterjee]]"],"producers":["Jai Pawar","Raj Prakash","Rajiv Suri"],"year":1979},
{"title":"Saajan Ki Baahon Mein","cast":["[[Rishi Kapoor]]","Sumeet Saigal","[[Raveena Tandon]]","[[Tabu (actress)|Tabu]]","[[Prem Chopra]]","[[Deven Verma]]","[[Laxmikant Berde]]","[[Pran (actor)|Pran]]","[[Saeed Jaffrey]]"],"directors":["Jay Prakash"],"producers":["Dinesh B. Patel"],"year":1995}]

"""
 NAME: load
 PARAMETERS: none
 PURPOSE: Load given movie data into a list for manipulation
 PRECONDITION: The data.txt file should be full in a JSON format
 POSTCONDITION: The dictionary should be copied in a different format
"""

def load():
    with open('data.txt') as f:
        for jsonObj in f:
            movieDict = json.loads(jsonObj)
            moviesList.append(movieDict)
    return moviesList


"""
 NAME: createMovieDict
 PARAMETERS: none
 PURPOSE: Create simplified movie dictionary with cast as values 
    for computation in program
 PRECONDITION: The sample dict and temp list should be empty, and the
    movie dictionary should be full from load()
 POSTCONDITION: The dictionary should be formed with the cast of the 
    movie formatted as keys, the movies as values (key value pairs)
"""

def createMovieDict():
    sampleDict = {}

    for movie in moviesList:
        tempList = []
        for i in range(0,len(movie['cast'])):
            actor = re.sub(r"[\[\]]",'',movie['cast'][i])
            tempList.append(actor)
        sampleDict[movie['title']] = tempList
    return sampleDict

"""
 NAME: movieCount
 PARAMETERS: none
 PURPOSE: Add all the movies as values (no duplicates)
 PRECONDITION: The keys in the actors dictionary should be full, the values
    should either be empty or have an empty list
 POSTCONDITION: The dictionary should be formed with the actors of the 
    dictionary formatted as keys, the movies as values (key value pairs)
"""

def movieCount():
    for movie in moviesList:

            for i in range(0,len(movie['cast'])):
                
                actor = re.sub(r"[\[\]]",'',movie['cast'][i])

                if actor in actorDict.keys():
                    actorDict[actor].append(movie['title'])
                else:
                    actorDict[actor] = [movie['title']]

    json.dump(actorDict, open("actor_data.json", 'w'), indent=2)
    return actorDict

"""
 NAME: findPath
 PARAMETERS: actorDict, start, target, visited, path
 PURPOSE: Attempt at combined DFS and BFS search using depth limiter value - 
    only returns the first and last connection between the two,
    not the entire spanning tree.
 PRECONDITION: The dictionary should be full and have no duplicates,
    the path should be empty. The start and target should have actor names.
    Visited should be an empty list and so should path (not recursion).
 POSTCONDITION: The path should be full of movies and the path should not
    exceed the length of 6.
"""

def findPath(actorDict,start,target,visited,path):
    depth = 2
    
    if len(path) >= depth:
       del path[:]
       start = og

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
                findPath(actorDict,actor,target,visited,path)
   
"""
 NAME: findNeighbors
 PARAMETERS: person_id
 PURPOSE: Return a list of (movie, person) pairs to represent 
    movies as the edges connecting the actor nodes to each other. 
 PRECONDITION: person_id should be the name of the actor targeted
 POSTCONDITION: The neighbors list is full of an actors neighbors.
"""
def findNeighbors(person_id):
    movies_in = actorDict[person_id]
    neighbors = set()

    for mov in movies_in:
        cast = movieDict[mov]
        for actor in cast:
            neighbors.add((mov, actor))
    print(neighbors)
    return neighbors

"""
 NAME: findShortest
 PARAMETERS: current, target
 PURPOSE: Proper algorithm to perform breadth first search - 
    Time consuming and costly as degrees of separation increase 
 PRECONDITION: the current should be the current actor node in the
    tree and the target should be the endpoint actors.
 POSTCONDITION: frontier should be empty.
"""

def findShortest(current, target):
    explored = set([])
    frontier = [current]
    parents = {}

    while len(frontier) > 0:
        actor = frontier.pop(0)
        if actor == target:
            break
        explored.add(actor)

        for (m, a) in findNeighbors(actor):
            if not a in frontier and not a in explored:
                frontier.append(actor)
                parents[a] = (m, actor)
                if not target in parents:
                    return None
        if not target in parents:
            return None

"""
 NAME: proper
 PARAMETERS: current, target
 PURPOSE: Test function to run findShortest() with Paul Rudd as target
 PRECONDITION: the target should be the source actor.
 POSTCONDITION: path should have the path between the source actor and 
    Paul Rudd.
"""
        
def proper():
    """
    """
    path = findShortest(og, target='Paul Rudd')
    if path is None:
        print("Not found")
    else:
        degrees_of_separation = len(path)
        print(f"{degrees_of_separation} degrees of separation.")
        print(path)
        
"""
 PURPOSE: Driver of the program with target as the target actor
    and start/og as the source actor.
"""

moviesList = load()
movieDict = createMovieDict()
actorDict = movieCount()
actorDictLength = (len(actorDict))
og = 'Kevin Bacon'

print(findPath(actorDict,start=og, target='Paul Rudd',visited=[],path = []))
proper()
