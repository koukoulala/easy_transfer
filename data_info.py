from find_structure import *

Lfile='/Users/didi/Desktop/store/data/cit-HepPh/processed_cit-HepPh.txt';
Cfile='/Users/didi/Desktop/store/data/cit-HepPh/processed_cit-HepPh_communities.txt'
L,C,LL=read_file(Lfile,Cfile)

#计算图有几个Communites
n=0;k=[];
for key in C:
    if C[key] not in k:
        k.append(C[key])
        n+=1
print("图的commnunite类型：",k)
print("图的commnunite数目：",n)
print("图的节点数目：",len(LL))
print("图中边的数目：",len(L))
print(len(C),len(LL))