#python 
#algorithms TD2
'''an implementation of a Graph class and related classes Node and Tree
TODO: GUI representation of graph object'''

from collections import defaultdict
from decimal import ROUND_DOWN



class Node():
    '''a node in a graph. contains the following:
        name: a string 
        color: 'white', 'black', or 'grey', for use with search algorithms
    '''
    def __init__(self, name, color = 'white'):
        self.name = name
        self.color = color 
    
    def __eq__(self, other_Node) -> bool:
        return self.name == other_Node.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self): 
        return self.name 
    
    def __lt__(self, other) -> bool:
        return self.name < other.name
    def __gt__(self, other) -> bool:
        return self.name > other.name

class Tree(): 
    ''' a tree of nodes. root is a node, children are also tree objects stored in a list'''

    def __init__(self, root, children = []):
        self.root = root
        self.children = children

    def __str__(self):
        if self.children == []:
            return str(self.root)
        else:

            return(str(self.root) + '[' + ', '.join([str(child) for child in self.children])+']')

    def add_child(self, node:Node):
        if not node in self.children:
            self.children.append(Tree(node))


class Graph():
    '''a directed graph. contains the following: 
        S: set of nodes
        A: transitions between nodes. dictionary with the starting nodes as keys and the end nodes as values 
        P:dict which keeps track of the predecessor for each node in a search'''
    def __init__(self, S = set(), A = defaultdict(lambda: []), P = dict(), w = defaultdict(int)):
        self.S = S
        self.A = A
        self.P = P
        self.w = w

        for (startNode, endNode), weight in w.items():
            self.S.add(startNode)
            self.S.add(endNode)
            if endNode not in self.A[startNode]:
                self.A[startNode].append(endNode)
  

    #methods
    def addNode(self, node):
        self.S.add(node)
    
    def addEdge(self, startNode, endNode):
        self.A[startNode]+= [endNode]

    def addP(self, node, parent):
        self.P[node] = parent
    
    def addWeight(self, nodes, weight):
        self.w[nodes] = weight



