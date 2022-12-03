import networkx as nx
import pandas as pd 
import time
from louvain import Louvain
from girvanNewman import girvanNewman, util
from collections import defaultdict

def makeSampleGraph():
    g = nx.Graph()
    f = open('data/sample_data.txt')
    while 1:
        line = f.readline()
        if not line:
            break 
        a, b = line.split(",")
        b = b.replace("\n","")
        g.add_edge(a, b, weight =1.)
    return g

if __name__ == "__main__":
    print("Starting Louvain's Community Detection Algoirthm...")
    start_time = time.time()
    sample_graph = makeSampleGraph()
    louvain = Louvain()
    print("Loaded Input Graph!")
    partition = louvain.getBestPartition(sample_graph)

    p = defaultdict(list)
    for node, com_id in partition.items():
        p[com_id].append(node)
    print("Community Detection Results:")
    for com, nodes in p.items():
        print(com, nodes)
    print("Runtime of Louvain's Algorithm %s seconds" % (time.time() - start_time))
    
    
