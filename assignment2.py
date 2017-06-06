import sys
import re
import time

import math # Imported for use of infinity

graphRE=re.compile("(\\d+)\\s(\\d+)")
edgeRE=re.compile("(\\d+)\\s(\\d+)\\s(-?\\d+)")

vertices=[]
edges=[]

def BellmanFord(G):
    # G is a tuple containing a list of the vertices, and a list of the edges
    # in the format ((source,sink),weight)

    # The pathPairs list will contain the list of vertex pairs and their weights [((s,t),w),...]t
    pathPairs=[]

    # Fill in your Bellman-Ford algorithm here
    for vertex in vertices:
        pathPairs.append(BellmanFordInstance(G,vertex))
    #print(pathPairs)

    # The pathPairs list will contain the list of vertex pairs and their weights [((s,t),w),...]
    return pathPairs

def BellmanFordInstance(G,s):
    # vertexWeight is the weight at each verticie
    vertexWeight=[]

    for vertex in vertices:
        vertexWeight.append([(s,vertex), math.inf])
    #print(vertexWeight)

    vertexWeight[s][1] = 0
    #print(vertexWeight)

    # Minimum distance
    for i in range(1,len(vertices)-1):
        for u in range(len(edges)):
            for v in range(len(edges)):
                if vertexWeight[v][1] > vertexWeight[u][1] + float(edges[u][v]):
                    vertexWeight[v][1] = vertexWeight[u][1] + float(edges[u][v])
    # Negative cylce check
    for u in range(len(edges)):
        for v in range(len(edges)):
            if vertexWeight[v][1] > vertexWeight[u][1] + float(edges[u][v]):
                return False
    return (vertexWeight)

def FloydWarshall(G):
    # G is a tuple containing a list of the vertices, and a list of the edges
    # in the format ((source,sink),weight)

    # The pathPairs list will contain the list of vertex pairs and their weights [((s,t),w),...]t
    pathPairs=[]

    # Fill in your Floyd-Warshall algorithm here
    # The pathPairs list will contain the list of vertex pairs and their weights [((s,t),w),...]t
    return pathPairs

def readFile(filename):
    global vertices
    global edges
    # File format:
    # <# vertices> <# edges>
    # <s> <t> <weight>
    # ...
    inFile=open(filename,'r')
    line1=inFile.readline()
    graphMatch=graphRE.match(line1)
    if not graphMatch:
        print(line1+" not properly formatted")
        quit(1)
    vertices=list(range(int(graphMatch.group(1))))
    edges=[]
    for i in range(len(vertices)):
        row=[]
        for j in range(len(vertices)):
            row.append(float("inf"))
        edges.append(row)
    for line in inFile.readlines():
        line = line.strip()
        edgeMatch=edgeRE.match(line)
        if edgeMatch:
            source=edgeMatch.group(1)
            sink=edgeMatch.group(2)
            if int(source) > len(vertices) or int(sink) > len(vertices):
                print("Attempting to insert an edge between "+source+" and "+sink+" in a graph with "+vertices+" vertices")
                quit(1)
            weight=edgeMatch.group(3)
            edges[int(source)][int(sink)]=weight
    #Debugging
    #for i in G:
        #print(i)
    return (vertices,edges)

def main(filename,algorithm):
    algorithm=algorithm[1:]
    G=readFile(filename)
    # G is a tuple containing a list of the vertices, and a list of the edges
    # in the format ((source,sink),weight)
    if algorithm == 'b' or algorithm == 'B':
        BellmanFord(G)
    if algorithm == 'f' or algorithm == 'F':
        FloydWarshall(G)
    if algorithm == "both":
        start=time.clock()
        BellmanFord(G)
        end=time.clock()
        BFTime=end-start
        FloydWarshall(G)
        start=time.clock()
        end=time.clock()
        FWTime=end-start
        print("Bellman-Ford timing: "+str(BFTime))
        print("Floyd-Warshall timing: "+str(FWTime))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    main(sys.argv[2],sys.argv[1])
