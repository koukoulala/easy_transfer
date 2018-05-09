#!/usr/bin/env python
import snap
import time
import sys
sys.path.append("../")
import config

start = time.clock()
Txt_name="result/closeness/"
Lfile = config.ce_Lfile

# graph loading
Graph = snap.LoadEdgeList(snap.PNGraph, Lfile, 0, 1)

# num of nodes
nodecount = Graph.GetNodes()

# creating required lists
cc = set()
closeness = dict()

for node in Graph.Nodes():
    # closeness centrality
    Clcentr = snap.GetClosenessCentr(Graph,node.GetId())
    closeness[node.GetId()] = Clcentr

for item in closeness:
    cc.add(closeness[item])

# writing the data to files in descending order
with open(Txt_name + config.ce_data+'.txt', 'w+') as fp:
    for p in sorted(closeness.items(), key=lambda (k, v): (v, k), reverse=True):
        fp.write("%s : %s\n" % p)

end = time.clock()
sum_time = end - start
print("complete,time=",sum_time)
f=open("result/closeness/"+config.ce_data+"_time.txt",'w')
f.write(str(sum_time))
f.close()


