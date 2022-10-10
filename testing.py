from itertools import count
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

root = None
root = createTree(moviesList,0,len(moviesList))
cnt = 0
accessPointArray = []

def searchTree(root,cnt,actor):
    if(root != None):
        cnt +=1
        for notKev in root.data['cast']:
            notKev = re.sub(r"[\[\]]",'',notKev)
            if(notKev == actor):
                accessPointArray.append(root)
                cnt = 0
        searchTree(root.left,cnt,actor)
        searchTree(root.right,cnt,actor)

accessPointArray2 = []
def searchTree2(root,cnt,actor):
    if(root != None):
        cnt +=1
        for notKev in root.data['cast']:
            notKev = re.sub(r"[\[\]]",'',notKev)
            if(notKev == actor):
                accessPointArray2.append(root)
                cnt = 0
        searchTree2(root.left,cnt,actor)
        searchTree2(root.right,cnt,actor)

searchTree(root,0,actor = 'Morgan Freeman')
searchTree2(root,0,actor = 'Kevin Bacon')
print(accessPointArray2)

def findConnection(root,cnt,actor):
    if(root!=None):
        for actors in root.data['cast']:
            actors = re.sub(r"[\[\]]",'',actors)
            if(actors == actor):
                print(root.data['title'])
        findConnection(root.left,cnt,actor)
        findConnection(root.right,cnt,actor)

def findKev(actor = 'Morgan Freeman'):
    for node in accessPointArray2:
        root = node
        findConnection(root,0,actor)

findKev()


