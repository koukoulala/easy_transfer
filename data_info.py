from find_structure import *
import config

Lfile=config.Lfile
Cfile=config.Cfile
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