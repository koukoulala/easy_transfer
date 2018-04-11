import time
from read_structure import *

if __name__=="__main__":
    start=time.clock()
    Lfile="/Users/didi/Desktop/store/data/facebook_4039.txt"
    L,train_node=get_list_set(Lfile)

    degree_cen=zeros([len(train_node),4],int)
    k=0
    for Tnode in train_node:
        in_degree,out_degree=degree_base(L,Tnode)
        degree_cen[k][0]=Tnode
        degree_cen[k][1]=in_degree
        degree_cen[k][2]=out_degree
        degree_cen[k][3]=in_degree+out_degree
        k+=1


    #对数组按照num列进行从大到小的排序
    sorted_node=degree_cen[argsort(-degree_cen[:,3])]
    print(sorted_node[0:100,:])
    savetxt("result/degree_facebook_4039.csv",sorted_node,fmt="%d",delimiter=',')
    end=time.clock()
    sum_time=end-start
    print("程序运行总时间为:",sum_time,"s")
