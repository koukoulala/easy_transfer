
from read_structure import *

if __name__=="__main__":
    Lfile="weibo/userrelation.csv"
    L,train_node=get_list_set(Lfile)

    stru_num=zeros([len(train_node),3],int)
    node_name=zeros(len(train_node),int)
    node_num = zeros(len(train_node), int)
    k=0
    for Tnode in train_node:
        W=find_stru(L,Tnode)
        print(W)
        stru_num[k]=W
        num=W[0]+2*W[1]+3*W[2]  #权重按照[1,2,3]
        node_num[k]=num
        node_name[k]=Tnode
        k+=1

    save_stru=c_[node_name,stru_num]
    save_stru = c_[save_stru, node_num]
    #对数组按照num列进行从小到大的排序
    sorted_node=save_stru[np.argsort(-save_stru[:,4])]
    print(sorted_node[0:100,:])
    #savetxt("user_W.csv",save_stru,fmt="%d",delimiter=',')
