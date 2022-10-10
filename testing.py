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

def userInput():
    actor = input("Which actor do you want to connect Kevin Bacon to? ")
    return actor

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

def searchTree(root,actor,arr):
    if(root != None):
        
        for castMember in root.data['cast']:
            castMember = re.sub(r"[\[\]]",'',castMember)
            if(castMember == actor):
                arr.append(root)
        
        searchTree(root.left,actor,arr)
        searchTree(root.right,actor,arr)
    return arr

def findHeight(root):
    if root is None:
        return 0
    leftHeight = findHeight(root.left)
    rightHeight = findHeight(root.right)
    return max(leftHeight,rightHeight) + 1

def findHeightOfAllMovies(arr):
    heightArray = []
    for node in arr:
        root = node
        heightArray.append(findHeight(root))
    return heightArray
        


def maxOfArr():
    pass

def main():
    root = None
    root = createTree(moviesList,0,len(moviesList))
    actor= userInput()
    arr1 = []
    arr2 = []
    arr1 = searchTree(root,'Kevin Bacon', arr1)
    arr2 = searchTree(root,actor,arr2)

    heightArray = []
    heightArray = findHeightOfAllMovies(arr1)
   
    heightArray2 = []
    heightArray2 = findHeightOfAllMovies(arr2)

    print('Bacon Number = ' + str(min(heightArray) + min(heightArray2)))
    
    

if __name__ == "__main__":
    main()