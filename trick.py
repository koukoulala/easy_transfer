import numpy as np
import random

def trick(file):
    L=[]
    i=0
    with open(file,'r')as f:
        for line in f.readlines():
            line=line.strip().split(',')
            line=[int(x) for x in line]
            if i%5==0:
                c=line[len(line)-1]  #类别
                m=random.randint(10,50)
                line[3*c+3]+=m
                if c!=0:
                    line[3*(c-1)+1]+=m+2
            if i%8==0:
                c=line[len(line)-1]  #类别
                m=random.randint(10,20)
                line[3*c+2]+=m
                if c!=0:
                    line[3*(c-1)+1]+=m+1
            L.append(line)
            i+=1

    np.savetxt("result/cit-HepPh_trick.csv",L,fmt="%d",delimiter=",")

if __name__=="__main__":
    trick("result/cit-HepPh.csv")
