import random
import pandas as pd

DNSR_path="result/deal_cit-HepPh.csv"
KNN_path="result/KNN/deal_cit-HepPh.csv"
ExDegree_path="result/ExDegree/deal_cit-HepPh.csv"
Closeness_path="result/closeness/deal_cit-HepPh.txt"
Betweenness_path="result/betweenness/deal_cit-HepPh.txt"
actual_file="/Users/didi/Desktop/store/data/cit-HepPh/deal_actual_cit-HepPh.txt"


#每个数据集里面取前300个节点
i=0;n=250;
csv_node=[]
size=500
with open(DNSR_path, 'r')as f:
    for lines in f.readlines():
        if i == n:
            break
        line = lines.strip("\n").split(",")
        csv_node.append(line[0])
        i += 1
i=0
with open(KNN_path, 'r')as f:
    for lines in f.readlines():
        if i == n:
            break
        line = lines.strip("\n").split(",")
        csv_node.append(line[0])
        i += 1
i=0
with open(ExDegree_path, 'r')as f:
    for lines in f.readlines():
        if i == n:
            break
        line = lines.strip("\n").split(",")
        csv_node.append(line[0])
        i += 1
i=0
with open(Closeness_path, 'r')as f:
    for lines in f.readlines():
        if i == n:
            break
        line = lines.strip("\n").split(":")
        csv_node.append(line[0])
        i += 1
i=0
with open(Betweenness_path, 'r')as f:
    for lines in f.readlines():
        if i == n:
            break
        line = lines.strip("\n").split(":")
        csv_node.append(line[0])
        i += 1

actual_node=random.sample(csv_node,size)
print(actual_node)
fw= open(actual_file,"w+")
for item in actual_node:
    fw.write(item)
    fw.write("\n")
fw.close()