#!/usr/bin/env python
#coding=utf-8
import numpy as np
import snap

tmp=np.zeros(30,int)

def get_in_degree(Graph,C,node_id,i):
    global tmp
    if i==0:
        return ;
    else:
        for try_in_node in Graph.Nodes():
            if try_in_node.GetId() == node_id:
                for in_in_node in try_in_node.GetInEdges():
                    tmp[C[in_in_node]] += 1
                    get_in_degree(Graph,C,in_in_node,i-1)
        return

def KNN(Lfile,Cfile,n,k):
    # parm：文件位置，n是图中类别数目，k是knn中的k，acc是准确率，err是分类错误的个数，fal是错误的行数
    global tmp
    acc=0;max=0;err=0
    C = {};
    AP = np.zeros([n+1, 3], float)
    map = 0

    # graph loading
    Graph = snap.LoadEdgeList(snap.PNGraph, Lfile, 0, 1)
    nodecount = Graph.GetNodes()

    with open(Cfile,'r')as f:
        for line in f:
            (key,value)=[int(x) for x in line.split()]
            C[key]=value

    # traverse the edges by nodes
    for node in Graph.Nodes():
        pre_label=n   #初始化为一个不存在的类别
        in_label = np.zeros(n,int)
        max=0
        for in_node in node.GetInEdges():
            #print(node.GetId(),' ',C[node.GetId()],' ',in_node,' ',C[in_node])
            in_label[C[in_node]]+=1

            for i in range(0,n):
                tmp[i]=in_label[i]
            get_in_degree(Graph,C,in_node,k-1)
            
            for i in range(0,n):
                in_label[i]=tmp[i]
        #print(in_label)
        for i in range(0,n):
            if in_label[i]>max:
                max=in_label[i]
                pre_label=i

        if pre_label==n:
            print(node.GetId())
        if pre_label!=C[node.GetId()]:
            #print(node.GetId(),' ',pre_label)
            err+=1
        else:
            AP[C[node.GetId()]][0] += 1

        AP[pre_label][1] += 1

    for j in range(0, n):
        if AP[j][1]!=0:
            map += AP[j][0] / AP[j][1]

    print("MAP=", map / n)
    print("err=", err)
    acc = 1 - (1.0*err / nodecount)
    return acc


if __name__ == "__main__":
    Lfile = '/Users/didi/Desktop/store/data/weibo/deal_weibo.txt';
    Cfile = '/Users/didi/Desktop/store/data/weibo/deal_change2_weibo_communities.txt'
    acc = KNN(Lfile,Cfile, 5,2)
    print("acc=", acc)