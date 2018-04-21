from find_structure import *

Lfile='/Users/didi/Desktop/store/data/weibo/deal_weibo.txt';
Cfile='/Users/didi/Desktop/store/data/weibo/deal_weibo_community.txt'
L,C,LL=read_file(Lfile,Cfile)

#计算图有几个Communites
n=0;k=[];
for key in C:
    if C[key] not in k:
        k.append(C[key])
        n+=1
print("图的commnunite类型：",k)
print("图的commnunite数目=",n)
print(len(C),len(LL))

#把3邻居结构数目保存到csv文件中
train_node=LL
train_data=zeros([len(train_node),n*3],int)
node_name=zeros(len(train_data),int) #节点名称，放在第一列
label_data=zeros(len(train_data),int)
k=0;
for Trnode in train_node:
    W=find_stru(L,n,C,Trnode)
    W2=W.reshape(n*3,order='C')
    #print("转换成行向量",W2)#一行有n*3列
    train_data[k]=W2
    node_name[k]=Trnode
    #node_name[k]=k
    label_data[k]=C[Trnode]
    k+=1

train_data=c_[train_data,label_data]
train_data=c_[node_name,train_data]
print(train_data)

savetxt("result/weibo.csv",train_data,fmt="%d",delimiter=",")
