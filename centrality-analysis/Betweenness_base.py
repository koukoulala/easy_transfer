#!/usr/bin/env python
import snap
import time
import sys
sys.path.append("../")
import config

start = time.clock()
Txt_name="result/betweenness/"
Lfile = config.ce_Lfile

# graph loading
Graph = snap.LoadEdgeList(snap.PNGraph, Lfile, 0, 1)

# num of nodes
nodecount = Graph.GetNodes()

# creating required lists
bc = set()
between = dict()

# computing betweenness centrality
Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(Graph, Nodes, Edges, 1.0)

# storing Nodes : Hash Table data to a dictionary
for node in Nodes:
    between[node] = Nodes[node]

for item in between:
    bc.add(between[item])

# writing the data to files in descending order
with open(Txt_name + config.ce_data+'.txt', 'w+') as fp:
    for p in sorted(between.items(), key=lambda (k, v): (v, k), reverse=True):
        fp.write("%s : %s\n" % p)

end = time.clock()
sum_time = end - start
print("complete,time=",sum_time)
f=open("result/betweenness/"+config.ce_data+"_time.txt",'w')
f.write(str(sum_time))
f.close()

