# Graphs
"""

(44)---------(76)
 ^
vertices of a graphs

the "-----------" between vertices is called edge 

# edges can be weighted / not weighted

    /(84)\
   /      \   w:15   :- weighted graph used for google maps to 
  /        \         determine the best route possible 
 /          \
(44)---------(76)    
      W:- 3


the can also be directional or non directional 

(you)--------(friend)  # facebook , you and friend


(you)------->(celeb)  # you and celeb



# you can use a adjacencey matrix to repersente graphs:-

rows:- vertices with 1 representing a edge between the vertice and 0 representing 
no edge between the vertice
cols represent the nodes with which the current node has vertices 
(picture :- adjecencey mat rep)



# we could also use a adjacenecy list to store our graphs:- 

like  {'a' : ['b','e'], 'b':['a','c'] , 'c':['b','d'] , 'd':['c','e'], 'e':['a','d']}

here in the above dictionary we have our vertex and the list of vertices with which it 
has and edge with.

# Big (O) of the graph

variable definition:- No of vertices == |V| and edges == |E|

Space complexity :- 

        Adjacancey list :- 
            O(|V|+|E|)

        Adjacancey Matrix:-
         O(|V|**2)


BigO T.C :-
    for adding a vertex:-
        Adjacancey list :- 
            O(1)

        Adjacancey Matrix:-
        O(|v|**2)

    for adding an edge:-
        Adjacencey Matrix/List:-
            O(1)
    
    for removing an edge:- 
        Adjacencey List:-
           O(|E|)
        Adjacencey Matrix :-
          O(1)

    for removing vertices:-
        Adj List:-
            O(|V| + |E|)
        Adj Matrix:-
            O(|V|**2)
"""
class  Graph:
    def __init__(self):
        self.adj_list = {}
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":" , self.adj_list[vertex])
    def add_vertex(self,vertex):
        '''
        adding a new vertex to the graph using adj list
        '''
        if vertex not in self.adj_list: # check if the vertex is not already present
            self.adj_list[vertex]=[] # if not add the vertex with an empty list
            return True # return True showing the sign of adding a vertex to the matrix
        return False # return false if the vertex is already in the matrix
    def add_edge(self,v1,v2):
        '''
        adding a new edges  to the given vertex's  using adj list and taking into the account that the vertices are already present 
        and the vertices doesn't have any edges yet.
        '''
        if v1 in self.adj_list and v2 in self.adj_list: # edge case check : check if the vertex is already in the matrix and if it is 
            self.adj_list[v1].append(v2) # then add edge of v2 to v1
            self.adj_list[v2].append(v1) # same to v2
            return True  # return True showing the sign of the matrix has been added
        return False # return False if any of the given vertex is not in then matrix
    def remove_edge(self,v1,v2):
        '''
        removing edge between two vertices. 
        '''
        if v1 in self.adj_list and v2 in self.adj_list:  # checking if both of the matrices are in the adj list if yes 
            try: # try removing those edges
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError: # if those values doesn't have any edge 
                return False # return false
            return True # return True if no error has occured
        return False # return False otherwise
    def remove_vertex(self,v):
        '''
        removing a vertex from the matrix , this is the one where we remove all the edges with the given vertex 
        and then remove the vertex from our list
        '''
        if v in self.adj_list:  # checking if the given vertex already in the list
            for vertices in self.adj_list[v]: # going for every value which is with the edge with  the vertices given  
                self.adj_list[vertices].remove(v) # and going into our dictionary using that vertice as our key and removing the given vertices as a edge
            del self.adj_list[v] # after completion of the for loop , we should delete the value v
            return True # return True if everything goes well 
        return False # return False

my_graph=Graph()

my_graph.add_vertex('a')
my_graph.add_vertex('b')
my_graph.add_vertex('c')
my_graph.add_vertex('d')

my_graph.add_edge('a','b')
my_graph.add_edge('c','b')
my_graph.add_edge('a','c')
my_graph.add_edge('d','a')
my_graph.add_edge('d','b')


print("before removing the edge")
my_graph.print_graph()

my_graph.remove_edge('a','b')


print("after  removing the edge")
my_graph.print_graph()

print("after  removing the vertex ")
my_graph.remove_vertex('d')
my_graph.print_graph()
