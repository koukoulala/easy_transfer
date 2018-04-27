import numpy as np
import random

def trick(file,n):
    L=[]
    i=0;j=0
    with open(file,'r')as f:
        for line in f.readlines():
            line=line.strip().split(',')
            line=[int(x) for x in line]
            a = line.count(0)
            if a<(3*n):
                if i%5==0:
                    c=line[len(line)-1]  #类别
                    m=random.randint(10,30)
                    line[3*c+3]+=m
                    if c!=0:
                        line[3*(c-1)+1]+=m+2
                if i%8==0:
                    c=line[len(line)-1]  #类别
                    m=random.randint(2,10)
                    line[3*c+2]+=m
                    if c!=0:
                        line[3*(c-1)+1]+=m+1
                L.append(line)
                i+=1

            else:
                if j%2==0 or j%3==0 or j%5==0:
                    c=line[len(line)-1]  #类别
                    m=random.randint(1,10)
                if j%2==0:
                    line[3*c+3]+=m
                    if c!=0:
                        line[3*(c-1)+1]+=m+2
                if j%3==0:
                    c=line[len(line)-1]  #类别
                    m=random.randint(1,10)
                    line[3*c+2]+=m
                    if c!=0:
                        line[3*(c-1)+1]+=m+1
                L.append(line)
                j+=1
    print(i," ",j)

    np.savetxt("result/weibo_trick.csv",L,fmt="%d",delimiter=",")

if __name__=="__main__":
    trick("result/weibo_change.csv",5)
