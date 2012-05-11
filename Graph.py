# -*- coding:UTF-8 -*-

# const
UNVISITED = 1<<31
IFINITY = -1<<31

# Edge
class Edge:
    def __init__(self,f,t):
        self.from_ = f
        self.to = t 
        self.weight = 0
# end of Edge        
        
# Graph Base Class
class Graph:
    def __init__(self,nunVertex):
        self.numVertex = numVertex
        self.numEdge = 0;
        self.Mark = []
        self.Indegree = []
        
        for i in range(0,numVertex):
            Mark[i] = UNVISITED
            Indedree[i] = 0;
        
    def FirstEdge(self, oneVertex):
        pass
    def NextEdge(self,preEdge):
        pass
    
    def VerNum(self):
        return self.numVertex
    
    def EdgesNum(self):
        return self.numEdge
    
    def IsEdge(self, edge):
        if edge.weight > 0 and edge.weight <IFINITY and edge.to >=0:
            return True
        else:
            return False
    def FromVertex(self,edge):
        return edge.from_
    def ToVertex(self,edge):
        return edge.to
    def Weight(self,edge):
        return edge.weight
    def SetEdge(self,from_,to,weight = 0):
        pass
    def delEdge(self,from_,to):
        pass
# end of Graph Base Class

class Graphm(Graph):
    def __init__(self,nunVertex):
        self.numVertex = numVertex
        self.numEdge = 0;
        self.Mark = []
        self.Indegree = []
        
        for i in range(0,numVertex):
            Mark[i] = UNVISITED
            Indedree[i] = 0;
        
    def FirstEdge(self, oneVertex):
        pass
    def NextEdge(self,preEdge):
        pass
    
    def VerNum(self):
        return self.numVertex
    
    def EdgesNum(self):
        return self.numEdge
    
    def IsEdge(self, edge):
        if edge.weight > 0 and edge.weight <IFINITY and edge.to >=0:
            return True
        else:
            return False
    def FromVertex(self,edge):
        return edge.from_
    def ToVertex(self,edge):
        return edge.to
    def Weight(self,edge):
        return edge.weight
    def SetEdge(self,from_,to,weight = 0):
        pass
    def delEdge(self,from_,to):
        pass
        
        
        