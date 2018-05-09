import  numpy as np

def deal_bigdata(Lfile,Cfile):
    L = [];
    LL = set();
    C = {};
    with open(Lfile, 'r')as f:
        for line in f.readlines():
            line = [int(x) for x in line.split()]
            L.append(line)
            for i in line:
                LL.add(i)
    with open(Cfile, 'r')as f:
        for line in f:
            (key, value) = [int(x) for x in line.split()]
            C[key] = value

    deal_LL={};deal_L=[];n=0;deal_C=[]
    for i in LL:
        deal_LL[i]=n
        n+=1

    for i in range(0,len(L)):
        a=deal_LL[L[i][0]]
        b=deal_LL[L[i][1]]
        deal_L.append((a,b))

    print(deal_L[0:10])

    for key in C.keys():
        a=deal_LL[key]
        # 这里的类别要从0开始
        deal_C.append((a,C[key]-1))

    print(deal_C[0:10])
    np.savetxt("/Users/didi/Desktop/store/data/cite/deal_cite.txt",deal_L,fmt="%d",delimiter=" ")
    np.savetxt("/Users/didi/Desktop/store/data/cite/deal_cite_communities.txt", deal_C, fmt="%d", delimiter=" ")


if __name__=="__main__":
    Lfile = '/Users/didi/Desktop/store/data/cite/processed_cite.txt';
    Cfile = '/Users/didi/Desktop/store/data/cite/processed_cite_communities.txt'
    deal_bigdata(Lfile,Cfile)