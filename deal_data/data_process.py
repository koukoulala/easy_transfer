import numpy as np
import random

def process_data(Lfile, Cfile):
    #仅保留两个文件中都有的节点
    L=[];LL=set();C={};CC=[];
    m=0
    with open(Lfile,'r')as f:
        for line in f.readlines():
            #if m>1000000:
                #break
            #m+=1
            line=line.strip('\n').split(' ')
            line=[int(x) for x in line]
            L.append(line)
            for i in line:
                LL.add(i)
    with open(Cfile,'r')as f:
        for line in f:
            (key,value)=[int(x) for x in line.split()]
            if key in LL:
                C[key]=value
                CC.append((key,value))

    print(len(C),len(L),len(LL))

    #随机从列表选择一些节点进行测试
    rate = 0.001
    size = int(rate * len(L))
    L=random.sample(L,size)


    processed_L=[];processed_LL=set();processed_CC=[]
    for i in L:
        if i[0]in C.keys() and i[1] in C.keys():
            processed_L.append(i)
            processed_LL.add(i[0])
            processed_LL.add(i[1])

    print(len(CC),len(processed_L),len(processed_LL))

    for key in C.keys():
        if key in processed_LL:
            processed_CC.append((key,C[key]))
    print(len(processed_CC),len(processed_L),len(processed_LL))

    np.savetxt("/Users/didi/Desktop/store/data/cite/processed_cite.txt",processed_L,fmt="%d",delimiter=" ")
    np.savetxt("/Users/didi/Desktop/store/data/cite/processed_cite_communities.txt",processed_CC,fmt="%d",delimiter=" ")

if __name__=="__main__":
    Lfile='/Users/didi/Desktop/store/data/cite/cite.txt';
    Cfile='/Users/didi/Desktop/store/data/cite/cite_communities.txt'
    process_data(Lfile, Cfile)