import time
from read_structure import *
import sys
sys.path.append("../")
import config

if __name__=="__main__":
    start=time.clock()
    Lfile=config.ce_Lfile
    L,train_node=get_list_set(Lfile)

    stru_num=zeros([len(train_node),3],int)
    node_name=zeros(len(train_node),int)
    node_num = zeros(len(train_node), int)
    k=0
    for Tnode in train_node:
        W=find_stru(L,Tnode)
        #print(W)
        stru_num[k]=W
        num=W[0]+2*W[1]+3*W[2]  #权重按照[1,2,3]
        node_num[k]=num
        node_name[k]=Tnode
        k+=1

    save_stru=c_[node_name,stru_num]
    save_stru = c_[save_stru, node_num]
    #对数组按照num列进行从大到小的排序
    sorted_node=save_stru[argsort(-save_stru[:,4])]
    print(sorted_node[0:100,:])
    savetxt("result/"+config.ce_data+".csv",sorted_node,fmt="%d",delimiter=',')
    end=time.clock()
    sum_time=end-start
    f = open("result/"+config.ce_data+"_time.txt", 'w')
    f.write(str(sum_time))
    print("程序运行总时间为:", sum_time, "s")
