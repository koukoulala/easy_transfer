import numpy as np

def process_data(Lfile, Cfile):

    L=[];LL=set();C={};CC=[];
    with open(Lfile,'r')as f:
        for line in f.readlines():
            line=[int(x) for x in line.split()]
            L.append(line)
            for i in line:
                LL.add(i)
    with open(Cfile,'r')as f:
        for line in f:
            (key,value)=[int(x) for x in line.split()]
            if key in LL:
                C[key]=value
                CC.append((key,value))

    print(len(C),len(L))

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

    np.savetxt("/Users/didi/Desktop/store/data/cit-HepPh/processed_cit-HepPh.txt",processed_L,fmt="%d",delimiter=" ")
    np.savetxt("/Users/didi/Desktop/store/data/cit-HepPh/processed_cit-HepPh_communities.txt",processed_CC,fmt="%d",delimiter=" ")

if __name__=="__main__":
    Lfile='/Users/didi/Desktop/store/data/cit-HepPh/cit-HepPh.txt';
    Cfile='/Users/didi/Desktop/store/data/cit-HepPh/cit-HepPh_communities.txt'
    process_data(Lfile, Cfile)