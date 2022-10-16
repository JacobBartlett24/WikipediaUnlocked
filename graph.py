import json
import re
import time
from typing import cast

moviesList = []
actorList = []
actorJsonList = []

testList = [{"title":"The Killer Must Kill Again","cast":["[[George Hilton (actor)|George Hilton]]","[[Antoine Saint-John]]","[[Femi Benussi]]","[[Cristina Galbó]]","[[Eduardo Fajardo]]","[[Tere Velázquez]]","[[Alessio Orano]]"],"directors":["[[Luigi Cozzi]]"],"producers":["Sergio Gobbi","[[Umberto Lenzi]] <small>(as Umberto Linzi)</small>","Giuseppe Tortorella"],"companies":["Albione Cinematografica","Git International Film","Paris-Cannes Productions"],"year":1975},
{"title":"Silent Action","cast":["[[Mel Ferrer]]","[[Brad Pitt]]","[[Tomas Milian]]","[[Luc Merenda]]","[[Michele Gammino]]","[[Paola Tedesco]]","[[Gianfranco Barra]]","Carlo Alighiero","[[Antonio Casale]]","Gianni Di Benedetto","[[Claudio Gora]]","[[Clara Colosimo]]","[[Arturo Dominici]]"],"directors":["[[Sergio Martino]]"],"producers":["[[Luciano Martino]]"],"companies":["Flora Film","Medusa Distribuzione","Medusa"],"year":1975},
{"title":"Manzil (1979 film)","cast":["[[Amitabh Bachchan]]","[[Moushumi Chatterjee]]","[[Rakesh Pandey]]","[[Satyen Kappu]]","[[Urmila Bhatt]]","[[Lalita Pawar]]","[[Shreeram Lagoo]]","[[A. K. Hangal]]","[[C. S. Dubey]]"],"directors":["[[Basu Chatterjee]]"],"producers":["Jai Pawar","Raj Prakash","Rajiv Suri"],"year":1979},
{"title":"Saajan Ki Baahon Mein","cast":["[[Rishi Kapoor]]","Sumeet Saigal","[[Raveena Tandon]]","[[Tabu (actress)|Tabu]]","[[Prem Chopra]]","[[Deven Verma]]","[[Laxmikant Berde]]","[[Pran (actor)|Pran]]","[[Saeed Jaffrey]]"],"directors":["Jay Prakash"],"producers":["Dinesh B. Patel"],"year":1995}]

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

with open('data.txt') as f:
    for jsonObj in f:
        movieDict = json.loads(jsonObj)
        moviesList.append(movieDict)
def movieCount():
    print('Starting actor list creation...')
    printProgressBar(0, len(moviesList), prefix = 'Progress:', suffix = 'Complete', length = 50)
    j=0
    for movie in moviesList:
        time.sleep(0.1)
        printProgressBar(j + 1, len(moviesList), prefix = 'Progress:', suffix = 'Complete', length = 50)
        j += 1
        for i in range(0,len(movie['cast'])):
            
            actor = re.sub(r"[\[\]]",'',movie['cast'][i])

            if(actor not in actorList):

                #actorJson = {
                #                "name": actor,
                #                "count": "0",
                #            }
                actorList.append(actor)
                
                #actorJsonList.append(actorJson)
                
    createGraph(actorList,moviesList)
                    
def createGraph(actorList, moviesList):
    matrix = [[0 for x in range(len(actorList))] for y in range (len(moviesList))]
    
    print('Starting matrix creation...')
    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            for castMember in moviesList[j]['cast']:
                actor = re.sub(r"[\[\]]",'',castMember)
                if(actor == actorList[i]):
                    matrix[i][j] = 1
    print(matrix)

movieCount()
