
param_csv="result/para/weibo.csv"
Cfile="/Users/didi/Desktop/store/data/weibo/deal_weibo_communities.txt"
Cfile_change="/Users/didi/Desktop/store/data/weibo/deal_change_weibo_communities.txt"

C={};C_para={}
with open(param_csv, 'r')as f:
    for line in f.readlines():
        line=line.strip().split(',')
        (key, value) = (line[0],line[1])
        C_para[key] = value

with open(Cfile, 'r')as f:
    for line in f:
        (key, value) = [int(x) for x in line.split()]
        C[key] = value

i=0
for key in C_para.keys():
    if i>20000:
        break
    C[key]=C_para[key]
    i+=1

with open(Cfile_change,"w+")as fw:
    for key in C.keys():
        fw.write(str(key)+" "+str(C[key])+"\n")