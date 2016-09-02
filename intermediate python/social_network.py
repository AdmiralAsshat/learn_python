## Social Networks

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

social = [('Jill','New York'),('Jill','Toronto'), \
          ('Jill','London'),('Jack','France'), \
          ('Jack','New York'), ('John','Berlin'), \
          ('John','London'),('Jacob','New York'), \
          ('Joan','Toronto'),]

for (x,y) in social: make_link(GRAPH, x, y)

####################################################
####################################################

## Shortest Path
## Breadth First Search (no Recursion)
## 'Stackoverflow' solution

def short_path(G, node1, node2):
    """ Return the shortest path from node1 to node2"""
    pass
    ## Your Code Here            

print short_path(GRAPH, 'Joan', 'John')
    
