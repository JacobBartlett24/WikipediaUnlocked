from itertools import count
import json
import re



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

"""
    NAME:           findHeight
    PARAMETERS:     root, the tree starting at the specified movie
    PURPOSE:        To find the height of said node.
    PRECONDITION:   The array should be full of movie nodes 
    POSTCONDITION:  The heightArray should be full of integers representing the heights of certain movies
"""


def findHeight(root):
    if root is None:
        return 0
    leftHeight = findHeight(root.left)
    rightHeight = findHeight(root.right)
    return max(leftHeight,rightHeight) + 1

"""
    NAME:           findHeightOfAllMovies
    PARAMETERS:     arr, list of nodes that contains movies of a certain actor
    PURPOSE:        To return an array of heights of all movies passed by array
    PRECONDITION:   The array should be full of movie nodes 
    POSTCONDITION:  The heightArray should be full of integers representing the heights of certain movies
"""

def findHeightOfAllMovies(arr):
    heightArray = []
    for node in arr:
        root = node
        heightArray.append(findHeight(root))
    return heightArray
        


"""
    AUTHOR:        Jacob Bartlett, Sam Wilson
    FILENAME:      main.py 
    SPECIFICATION: Find distance between two nodes (actors), should return the Bacon number (distance)
    FOR:           CS 3368 Introduction to Artificial Intelligence Section 001
"""

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
