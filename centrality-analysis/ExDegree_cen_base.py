#!/usr/bin/env python
# coding=utf-8
import numpy as np
import snap
import time
import random

tmp = np.zeros(30, int)


def get_in_degree(Graph, C, node_id, i):
    global tmp
    if i == 0:
        return;
    else:
        for try_in_node in Graph.Nodes():
            if try_in_node.GetId() == node_id:
                for in_in_node in try_in_node.GetInEdges():
                    tmp[C[in_in_node]] += 1
                    get_in_degree(Graph, C, in_in_node, i - 1)
        return


def ExDegree(Lfile, Cfile, n, k):
    # parm：文件位置，n是图中类别数目，k是knn中的k，acc是准确率，err是分类错误的个数，fal是错误的行数，in_label存储每个节点n种类别的k度邻居总数目
    start = time.clock()
    global tmp
    C = {};

    # graph loading
    Graph = snap.LoadEdgeList(snap.PNGraph, Lfile, 0, 1)
    nodecount = Graph.GetNodes()
    in_label=np.zeros([nodecount,n+1],int)   #初始化

    with open(Cfile, 'r')as f:
        for line in f:
            (key, value) = [int(x) for x in line.split()]
            C[key] = value

    # traverse the edges by nodes
    for node in Graph.Nodes():
        for in_node in node.GetInEdges():
            # print(node.GetId(),' ',C[node.GetId()],' ',in_node,' ',C[in_node])
            in_label[node.GetId()][C[in_node]] += 1

            for i in range(0, n):
                tmp[i] = in_label[node.GetId()][i]

            # 随机得到实际扩展的层数
            m = random.randint(1, k)
            get_in_degree(Graph, C, in_node, m)

            for i in range(0, n):
                in_label[node.GetId()][i] = tmp[i]
                in_label[node.GetId()][n] += in_label[node.GetId()][i]

    sorted_node = in_label[np.argsort(-in_label[:, n])]
    print(sorted_node[0:100, :])
    np.savetxt("result/ExDegree/deal_cit-HepPh.csv", in_label, fmt="%d", delimiter=',')
    end = time.clock()
    sum_time = end - start
    return sum_time


if __name__ == "__main__":
    Lfile = '~/cit-HepPh/deal_cit-HepPh.txt';
    Cfile = '~/cit-HepPh/deal_cit-HepPh_communities.txt'
    sum_time=ExDegree(Lfile, Cfile, 11, 2)
    print("程序运行总时间为:", sum_time, "s")
    f = open("result/ExDegree/ExDegree_time.txt", 'w')
    f.write(str(sum_time))
    f.close()