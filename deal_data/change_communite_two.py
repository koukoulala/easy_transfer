#!/usr/bin/env python
#coding=utf-8
import numpy as np
import snap

Lfile="/Users/didi/Desktop/store/data/weibo/deal_weibo.txt"
Cfile_change="/Users/didi/Desktop/store/data/weibo/deal_change2_weibo_communities.txt"

C={}
# graph loading
Graph = snap.LoadEdgeList(snap.PNGraph, Lfile, 0, 1)

n=5 #类别总数
i=0
for node in Graph.Nodes():
    v=node.GetId()
    if v not in C.keys():
        C[v]=i
        i=(i+1)%5
    #令这个点指向的点的类别和这个点类别相同
    for out_node in node.GetOutEdges():
        if out_node not in C.keys():
            C[out_node]=C[v]

with open(Cfile_change,"w+")as fw:
    for key in C.keys():
        fw.write(str(key)+" "+str(C[key])+"\n")