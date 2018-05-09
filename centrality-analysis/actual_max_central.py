import random

DNSR_path="result/deal_cite.csv"
KNN_path="result/KNN/deal_cite.csv"
ExDegree_path="result/ExDegree/deal_cite.csv"
Closeness_path="result/closeness/deal_cite.txt"
Betweenness_path="result/betweenness/deal_cite.txt"
actual_file="/Users/didi/Desktop/store/data/cite/deal_actual_cite.txt"


#其他数据集里面取前300个节点
n=300;m=1500
csv_node=[]
size=500

i=0;
with open(DNSR_path, 'r')as f:
    for lines in f.readlines():
        if i == m:
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
        if line[0] not in csv_node:
            csv_node.append(line[0])
            i += 1

i=0
with open(ExDegree_path, 'r')as f:
    for lines in f.readlines():
        if i == n:
            break
        line = lines.strip("\n").split(",")
        if line[0] not in csv_node:
            csv_node.append(line[0])
            i += 1

i=0
with open(Closeness_path, 'r')as f:
    for lines in f.readlines():
        if i == n:
            break
        line = lines.strip("\n").split(":")
        if line[0] not in csv_node:
            csv_node.append(line[0])
            i += 1

i=0
with open(Betweenness_path, 'r')as f:
    for lines in f.readlines():
        if i == n:
            break
        line = lines.strip("\n").split(":")
        if line[0] not in csv_node:
            csv_node.append(line[0])
            i += 1

print(len(csv_node))
actual_node=random.sample(csv_node,size)
print(len(actual_node))
fw= open(actual_file,"w+")
for item in actual_node:
    fw.write(item)
    fw.write("\n")
fw.close()