
from numpy import *

#param:Lfile为边表文件
#return:L为节点对组成的List，LL是所有节点去重后的set
def get_list_set(Lfile):
    L=[];LL=set()
    with open(Lfile,'r')as f:
        for line in f.readlines():
            #line=line.strip("\n").split(",")
            line=line.strip("\n").split()
            line=[int(x) for x in line]
            L.append(line)
            for i in line:
                LL.add(i)
    return L,LL

#param:L是节点对list，Tnode是目标节点
#return:W矩阵，W[i]=k代表目标节点的wi结构有k个，一行3列的列向量
def find_stru(L,Tnode):
    W=zeros(3,int16)
    #l为目标节点的直接前驱点
    l=[];

    for i in L:
        if i[1] == Tnode:
            l.append(i[0])

    #计算三种结构数目,每个节点只能参与到一"种"结构中

    for i in l:
        flag=0; #如果flag=0，也就是不存在w2结构，也就是只有w1结构
        for j in L:
            if j[1]==i : # 前驱点有前驱
                k2 = j[0]
                flag=1
                if k2 in l:  # 前驱的前驱也是直接前驱，w3的结构
                    W[2] += 1;
                    l.remove(k2)  #k2这个节点是用来组成w3结构的，所以要去掉，否则会又组成一个w1结构
                else:
                    W[1] += 1;
        #l.remove(i)    #把i移除，这样一个节点只能组成一种结构
        if flag == 0:
            W[0] += 1;

    return W

#求Tnode的入度和出度
def degree_base(L,Tnode):
    in_degree=0;out_degree=0
    for i in L:
        if i[1]==Tnode:
            in_degree+=1
        if i[0]==Tnode:
            out_degree+=1

    return in_degree,out_degree

