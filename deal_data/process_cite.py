#!/usr/bin/env python
# coding=utf-8
import numpy as np
import snap

def process_cite(Lfile,Cfile):
    # 仅保留两个文件中都有的节点
    L = [];
    LL = set();
    C = {};
    CC = [];

    # graph loading
    #把入度>某个值的节点加入进去
    Graph = snap.LoadEdgeList(snap.PNGraph, Lfile, 0, 1)
    nodecount = Graph.GetNodes()
    for node in Graph.Nodes():
        if node.GetInDeg()>100:
            LL.add(node.GetId())
            for in_node in node.GetInEdges():
                LL.add(in_node)
                if (in_node,node.GetId()) not in L:
                    L.append((in_node,node.GetId()))

    with open(Cfile,'r')as f:
        for line in f:
            (key,value)=[int(x) for x in line.split()]
            if key in LL:
                C[key]=value
                CC.append((key,value))

    print(len(C),len(L),len(LL))
    processed_L = [];
    processed_LL = set();
    processed_CC = [];
    print("begin process")
    for i in L:
        if i[0] in C.keys() and i[1] in C.keys():
            processed_L.append(i)
            processed_LL.add(i[0])
            processed_LL.add(i[1])

    print(len(CC), len(processed_L), len(processed_LL))

    for key in C.keys():
        if key in processed_LL:
            processed_CC.append((key, C[key]))
    print(len(processed_CC), len(processed_L), len(processed_LL))

    np.savetxt("/Users/didi/Desktop/store/data/cite/processed_cite.txt", processed_L, fmt="%d", delimiter=" ")
    np.savetxt("/Users/didi/Desktop/store/data/cite/processed_cite_communities.txt", processed_CC, fmt="%d",
               delimiter=" ")


if __name__=="__main__":
    Lfile='/Users/didi/Desktop/store/data/cite/cite.txt';
    Cfile='/Users/didi/Desktop/store/data/cite/cite_communities.txt'
    process_cite(Lfile, Cfile)