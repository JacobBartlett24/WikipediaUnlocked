import wikipedia
from bs4 import BeautifulSoup as bs4
import requests
import json

with open('data.json') as json_file:

    data = json.load(json_file)

def promptSearchActor():
    actor = input('Type in which actor you want to connect to Kevin Bacon: ')
    suggestions = wikipedia.search(actor);
    makeSuggestionList(suggestions)
    suggestion = pickSuggestion(suggestions)
    startScript(wikipedia.page(suggestion, auto_suggest=False))

def pickSuggestion(suggestions):
    suggestionPick = input('\nType the number of which suggestion is correct: ')
    suggestionPick = int(suggestionPick)
    suggestion = suggestions[suggestionPick - 1]
    return suggestion

def makeSuggestionList(suggestions):
    print('')
    for i in range(0,len(suggestions)):
        suggestionListItem = str(i + 1) + '.' + suggestions[i]
        print(suggestionListItem)
    
def startScript(actor):
    #extractMovies(actor)
    extractActors(actor)
    pass

def extractActors(actor):
    response = requests.get(actor.url)
    soup = bs4(response.text,'html.parser')
    aTagList = soup.find_all("a")

    for i in range(0,len(aTagList)):
        for j in range(0,len(data)):
            print()

def extractMovies(actor):
    findIMDBLink(actor)
    pass

def findIMDBLink(actor):
    response = requests.get(actor.url)
    soup = bs4(response.text,'html.parser')
    aTagList = soup.find_all("a", {"class": "external text"})
    
    for i in range(0, len(aTagList)):
        if 'imdb.com/name' in str(aTagList[i]):
            IMDBLink = aTagList[i]['href']
            movieArr = getAllMovies(IMDBLink)

def getAllMovies(IMDBLink):
    response = requests.get(IMDBLink)
    soup = bs4(response.text, 'html.parser')
    movieList = soup.find_all('div', {'class': 'filmo-row'})
    titleArr = []
    
    for i in range(0,len(movieList)):
        children = movieList[i].findChildren('a',recursive=True)
        for child in children:
            titleArr.append(child)

    return titleArr

promptSearchActor()