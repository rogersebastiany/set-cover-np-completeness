from collections import defaultdict, deque
import set_cover

class Graph:
    def __init__(self, vertices):
        self.V = vertices
         
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v):
        self.graph[u].append(v)

g = Graph(6)                                   
g.addEdge(1, 2)                                
g.addEdge(1, 3)                                
g.addEdge(2, 3)                               
g.addEdge(2, 4)                                
g.addEdge(3, 5)                                
g.addEdge(4, 5)                                
g.addEdge(4, 6)                                

#Isso nao funcionaria se algum vértice tiver um valor maior do que 10, ou se
#o grafo tiver mais do que 10 vértices. Nesse caso, seria necessário criar V e E na mão.
# V = {12, 13, 23, 24, 35, 45, 46}
# E =  [{12,13},
#          {12, 23, 24},
#          {13, 23, 35},
#          {24, 45, 46},
#          {35,45},
#          {46}]

V=set()                                       
for u in dict(g.graph).keys():                # O(u)*O(u*v) -> v*O(u²)
    for v in dict(g.graph)[u]:                # O(u)
        V.add(u*10+v)                         # O(u*v)                      
                                            
                                  
E = []                                        
max_u = g.V                                   
def is_edge_of(v, u):
    return (str(u) in str(v))
for u in range(1, max_u+1):                              # O(u)*O(u+v)
    v_of_u = set(filter(lambda v: is_edge_of(v, u), V))  # O(u+v)
    E.append(v_of_u)

k = set_cover.brute_force(V, E)
res = deque(k)
res.popleft()

bf = 0
for r in list(res):                                      # O(u)
    if r == 1:                                 
        bf+=1                                  

print(bf, list(res))    

#Assumindo que u e v tenham tamanho n
#Complexidade Final
#
# v*O(u²) + O(u²) + O(u) -> v*O(u²)
# 



