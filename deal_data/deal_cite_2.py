#!/usr/bin/env python
#coding=utf-8

import numpy as np
import sys
sys.path.append("../")
import config
import snap

def process_cite_2(Lfile,Cfile):
    path = config.path + config.subpath
    '''
    # 保存最大连通图
    
    # graph loading
    Graph = snap.LoadEdgeList(snap.PUNGraph, Lfile, 0, 1)
    MxScc = snap.GetMxScc(Graph)
    snap.SaveEdgeList(MxScc, path+"processed_2_cite.txt", "Save as tab-separated list of edges")
    '''

    LL = set();
    # 把入度>某个值的节点加入进去
    Graph = snap.LoadEdgeList(snap.PNGraph, Lfile, 0, 1)
    for node in Graph.Nodes():
        if node.GetInDeg() > 200:
            LL.add(node.GetId())
    SubG = snap.GetSubGraph(Graph, snap.TIntV.GetV(5193110))
    snap.SaveEdgeList(SubG, path + "Sub_cite.txt")

if __name__=="__main__":
    Lfile='/Users/didi/Desktop/store/data/cite/cite.txt';
    Cfile='/Users/didi/Desktop/store/data/cite/cite_communities.txt'
    process_cite_2(Lfile, Cfile)