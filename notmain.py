import json
import re

#exmaple json object: {"title":"The Wolf of Wall Street (2013 film)","cast":["[[Leonardo DiCaprio]]","[[Jonah Hill]]","[[Margot Robbie]]","[[Matthew McConaughey]]","[[Kyle Chandler]]","[[Rob Reiner]]","[[Jon Favreau]]","[[Jean Dujardin]]","[[Jon Bernthal]]","[[Joanna Lumley]]","[[Cristin Milioti]]","[[Christine Ebersole]]","[[Shea Whigham]]","[[Katarina Čas]]","[[Stephanie Kurtzuba]]","[[P. J. Byrne]]","[[Kenneth Choi]]","[[Brian Sacca]]","[[Henry Zebrowski]]","[[Ethan Suplee]]","[[Jake Hoffman (actor)|Jake Hoffman]]","[[Mackenzie Meehan]]","[[Bo Dietl]]","[[Jon Spinogatti]]","[[Aya Cash]]","[[Jordan Belfort]]","[[Catherine Curtin]]","[[Stephen Kunken]]","[[Barry Rothbart]]","[[Welker White]]","[[Daniel Flaherty|Danny Flaherty]]","[[Ted Griffin]]","[[Steven Boyer]]","[[J. C. MacKenzie]]","[[Ashlie Atkinson]]","[[Thomas Middleditch]]","[[Fran Lebowitz]]","[[Spike Jonze]]"],"directors":["[[Martin Scorsese]]"],"producers":["[[Martin Scorsese]]","[[Leonardo DiCaprio]]","[[Riza Aziz]]","[[Joey McFarland]]","[[Emma Tillinger Koskoff]]"],"companies":["[[Paramount Pictures]]"],"year":2013}

moviesList = []
testList = [{"title":"Manhatta","cast":['Morgan Freeman'],"directors":["[[Charles Sheeler]]","[[Paul Strand]]"],"year":1921},
{"title":"something","cast":[],"directors":["[[Charles Sheeler]]","[[Paul Strand]]"],"year":1921},
{"title":"some","cast":[],"directors":["[[Charles Sheeler]]","[[Paul Strand]]"],"year":1921}]

with open('data.txt') as f:
    for jsonObj in f:
        movieDict = json.loads(jsonObj)
        moviesList.append(movieDict)

class newNode:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def createTree(arr,i,n):
    root = None

    if i<n:

        root = newNode(arr[i])

        root.left = createTree(arr,2 * i + 1,n)
        
        root.right = createTree(arr,2 * i + 2,n)

    return root

#prints inorder
def inOrder(root):
    if(root != None):
        inOrder(root.left)
        print(root.data['title'])
        if(len(root.data['cast']) != 0):
            for actor in root.data['cast']:
                #actor = re.sub(r"[\[\]]",'',actor)
                
                findActor(root,actor,isContained=False)
        else: print('no cast')
        print('\n')
        inOrder(root.right)

#compile movies of a certain actor
#actorname + all the movies
def compileMovies(root,selectActor):
    if(root != None):
        pass
        
def findActor(root,actor,isContained):
    if(root != None):
        findActor(root.left,actor,isContained = False)
        if(len(root.data['cast']) != 0):
            for castMember in root.data['cast']:
                castMember = re.sub(r"[\[\]]",'',castMember)
                if castMember == actor:
                    isContained = True
        if(isContained):
            print(root.data['title'])
        findActor(root.right,actor,isContained = False)



#    if(root != None):
#        compileMovies(root.left,selectActor)
#        if(len(root.data['cast']) != 0):
#            for actor in root.data['cast']:
#                actor = re.sub(r"[\[\]]",'',actor)
#                if actor == selectActor:
#                    print(root.data['title'])
#        compileMovies(root.right,selectActor)
    
    
#root= None
#
#foundMovie = inOrder(root)
root = None
root = createTree(moviesList,0,len(moviesList))
#findActor(root,'Miles Teller',isContained=False)

def listActors():
    for movie in moviesList:
        cast = movie['cast']
        for actor in cast:
            actor = re.sub(r"[\[\]]",'',actor)
            print(actor)
            findActor(root,actor,isContained=False)
            print()

listActors()