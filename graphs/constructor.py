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
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]
            return True
        return False
    def add_edge(self,v1,v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    def remove_vertex(self,v):
        if v in self.adj_list:
            for vertices in self.adj_list[v]:
                self.adj_list[vertices].remove(v)
            del self.adj_list[v]
            return True
        return False
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
