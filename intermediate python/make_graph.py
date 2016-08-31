## Graphs / Networks

## Social Networks
## Maps
## Relationships

## Our Goal: Shortest Path

## What is a graph / network

##  - Node
##  - Edges

## How to make a Graph / Network in Python?

GRAPH = {}

def make_link(Graph, node1, node2):
    """
    A Graph will be a dictionary containing nodes.
    Theses nodes will be a dictionary of neighbor nodes.
    The node's dict. key will be the neighbor node and
    it's value will be 1.
    Return the updated Graph.
    """
    if node1 not in Graph:
        Graph[node1] = {}
    (Graph[node1])[node2] = 1
    if node2 not in Graph:
        Graph[node2] = {}
    (Graph[node2])[node1] = 1
    return Graph
