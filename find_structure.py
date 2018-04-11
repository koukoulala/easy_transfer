from numpy import *

#param:Lfile为边表文件，Cfile为节点所属类别文件
#return:L为节点对组成的List，LL是所有节点去重后的set，C是（node,communite）字典
def read_file(Lfile,Cfile):
    L=[];LL=set();C={};
    with open(Lfile,'r')as f:
        for line in f.readlines():
            line=[int(x) for x in line.split()]
            #line2=[line[1],line[0]]
            L.append(line)
            #L.append((line2))
            for i in line:
                LL.add(i)
    with open(Cfile,'r')as f:
        for line in f:
            (key,value)=[int(x) for x in line.split()]
            C[key]=value
    return L,C,LL

#param:L是节点对list，n是communite的数目，C是（node,communite）字典，Tnode是目标节点
#return:W矩阵，W[i][j]=k代表目标节点的邻居类别=i的节点的wj结构有k个，n行3列的二维数组
def find_stru(L,n,C,Tnode):
    W=zeros([n,3],int16)
    #l为目标节点的不同类别的直接前驱点
    l=[];i=0;
    while i!=n:
        l.append([])
        i+=1
    for i in L:
        if i[1] == Tnode:
            l[C[i[0]]].append(i[0])
    #print("目标节点",Tnode,"的直接前驱情况:",l)

    #一个类别一个类别的来计算不同结构数目
    k=0
    for ll in l:
        if ll!=[]:
            while 1:
                if len(ll)==0:    #不能在for循环里面用remove,所以使用判断列表是否为空的方法，每次取列表的第一个
                    break;
                i=ll[0]
                flag=0; #如果flag=0，也就是不存在w2结构，也就是只有w1结构
                for j in L:
                    if j[1]==i and C[j[0]]==k: # 前驱点有前驱,且类别也相同
                        k2 = j[0]
                        flag=1
                        if k2 in ll:  # 前驱的前驱也是直接前驱，w3的结构
                            W[k][2] += 1;
                            ll.remove(k2)  #k2这个节点是用来组成w3结构的，所以要去掉，否则会又组成一个w1结构
                        else:
                            W[k][1] += 1;
                ll.remove(i)
                if flag == 0:
                    W[k][0] += 1;
        k+=1

    #print("目标节点",Tnode,"有",n,"种类别，每个类别3种结构数目:")
    #print(W)
    return W
