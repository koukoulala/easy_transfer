
#处理得到准确率和召回率
def recall_acc(csvpath,datepath,n):
    #csv是按中心度从高到低顺序排列的文件，date是节点出现的时间数据，n是要读多少行
    i=0;acc=0;recall=0
    csv_node=[];date_node=[]

    with open(csvpath,'r')as f:
        for lines in f.readlines():
            if i==n:
                break
            line=lines.strip("\n").split(",")
            csv_node.append(line[0])
            i+=1
    i=0
    with open(datepath,'r')as f:
        for lines in f.readlines():
            if i==n:
                break
            line=lines.strip("\n").split("\t")
            date_node.append(line[0])
            i+=1
            if line[0] in csv_node:
                recall+=1
                print("recall:",line[0])

    for i in csv_node:
        if i in date_node:
            acc+=1
            print("acc:", i)

    return 1.0*acc/n,  1.0*recall/n


if __name__=="__main__":
    acc,recall=recall_acc("result/cit-HepPh.csv",
                          "/Users/didi/Desktop/store/data/cit-HepPh/cit-HepPh-dates.txt",150)
    print("准确率为：",acc,"召回率为：",recall)