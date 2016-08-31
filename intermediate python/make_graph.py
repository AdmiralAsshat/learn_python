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

connected_letters = [('a','g'),('a','d'),('d','g'),('g','c'), \
           ('b','f'),('f','e'),('e','h')]

for (x,y) in connected_letters: make_link(GRAPH, x, y)

#####################################################################

def marked_node(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbour in G[node]:
        if neighbour not in marked:
            total_marked += marked_node(G, neighbour, marked)
    return total_marked

def list_node_sizes(G):
    marked = {}
    for node in G.keys():
        if node not in marked:
            print "Graph containing", node, \
                  ":", marked_node(G, node, marked)

#########################
### Pairwise Connection
#########################

## Depth First Search Solution
def is_connected(G, node1, node2):
    marked = {}
    marked_node(G, node1, marked)
    return node2 in marked



#list_node_sizes(GRAPH)
print is_connected(GRAPH, 'a','h')

            