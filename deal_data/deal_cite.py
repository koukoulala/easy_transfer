import numpy as np

def deal_cite(Lfile, Cfile):

    C=[];ratio=[];l=[]
    with open(Lfile,'r')as f:
        for lines in f.readlines():
            line=lines.strip('\n').split(',')
            l.append((line[0],line[1]))
    np.savetxt("/Users/didi/Desktop/store/data/cite/cite.txt", l, fmt="%s", delimiter=" ")
    '''
    with open(Cfile,'r')as f:
        for lines in f.readlines():
            line=lines.strip('\n').split(',')
            if line[14]!='':
                C.append((line[0],line[10]))
                ratio.append((int(line[0]),int(float(line[14])*1000)))

    ratio=np.array(ratio)
    # 对Percent of Citations Made to Patents Granted Since 1963从大到小的排序
    sorted_ratio = ratio[np.argsort(-ratio[:, 1])]
    print(sorted_ratio[1:20])
    np.savetxt("/Users/didi/Desktop/store/data/cite/cite_communities.txt",C,fmt="%s",delimiter=" ")
    np.savetxt("/Users/didi/Desktop/store/data/cite/cite_ratio.txt",sorted_ratio,fmt="%s",delimiter=" ")
    '''
if __name__=="__main__":
    Lfile = '/Users/didi/Desktop/store/data/cite/cite75_99.txt';
    Cfile='/Users/didi/Desktop/store/data/cite/apat63_99.txt'
    deal_cite(Lfile,Cfile)