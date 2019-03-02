#!/usr/bin/env python3

# PathSearchLib.py
# A library module for PathSearch.py, primarily used for storing data structures

import heapq
import collections

# Data Structure
## Queue
### --> This is a wrapper class for python collection module's deque
class Queue:
    def __init__(self):
        # Init a deque
        self.elements = collections.deque()
    
    def empty(self):
        # return true if the length of the elements list is empty
        return len(self.elements) == 0

    def put(self, x):
        # Add new element to the list
        self.elements.append(x)

    def get(self):
        # Get the first out element from the queue
        return self.elements.popleft()

## Priority Queue
class PriorityQueue:
    def __init__(self):
        # Init a list of elements
        self.elements = []

    def empty(self):
        # return true if the length of the elements list is empty
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority,item))

    def get(self):
        return heapq.heappop(self.elements)[1]

# Simple Graph Implementation
class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    def getNeighbors(self, id):
        return self.edges[id]

# Weighted Graph Implementation w/ some more features
class WeightedGraph:
    def __init__(self):
        self.NodeList = {}

    def addNode(self, node_name):
        self.NodeList.append(node_name)

    def addConnection(self, root_node, connected_node, weight):
        self.NodeList[root_node].append((connected_node, weight))

    def removeNode(self, node_to_be_removed):
        if(node_to_be_removed in self.NodeList):
            self.NodeList.pop(node_to_be_removed)
        else:
            return

    def getConnection(self, root_node):
        if(root_node in self.NodeList):
            return self.NodeList[root_node]
        else:
            return