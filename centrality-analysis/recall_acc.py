
#对每个文件分别处理得到准确率和召回率
def recall_acc(n):
    # 文件按中心度从高到低顺序排列，n是要读多少行
    DNSR_path = "result/deal_cite.csv"
    KNN_path = "result/KNN/deal_cite.csv"
    ExDegree_path = "result/ExDegree/deal_cite.csv"
    Closeness_path = "result/closeness/deal_cite.txt"
    Betweenness_path = "result/betweenness/deal_cite.txt"
    actual_file = "/Users/didi/Desktop/store/data/cite/deal_actual_cite.txt"

    DNSR_node=0;KNN_node=0;ExDegree_node=0;Closeness_node=0;Betweenness_node=0
    actual_node=[]

    i=0
    with open(actual_file,'r')as f:
        for lines in f.readlines():
            if i==n:
                break
            line=lines.strip("\n").split()
            actual_node.append(line[0])
            i+=1

    i=0
    with open(DNSR_path,'r')as f:
        for lines in f.readlines():
            if i==n:
                break
            line=lines.strip("\n").split(",")
            if line[0] in actual_node:
                DNSR_node+=1
            i+=1
    print("DNSR识别到正确节点数目：",DNSR_node,"召回率为：",1.0*DNSR_node/n)

    i = 0
    with open(KNN_path, 'r')as f:
        for lines in f.readlines():
            if i == n:
                break
            line = lines.strip("\n").split(",")
            if line[0] in actual_node:
                KNN_node += 1
            i += 1
    print("KNN识别到正确节点数目：", KNN_node, "召回率为：", 1.0 * KNN_node / n)

    i = 0
    with open(ExDegree_path, 'r')as f:
        for lines in f.readlines():
            if i == n:
                break
            line = lines.strip("\n").split(",")
            if line[0] in actual_node:
                ExDegree_node += 1
            i += 1
    print("ExDegree识别到正确节点数目：", ExDegree_node, "召回率为：", 1.0 * ExDegree_node / n)

    i = 0
    with open(Closeness_path, 'r')as f:
        for lines in f.readlines():
            if i == n:
                break
            line = lines.strip("\n").split(" ")
            if line[0] in actual_node:
                Closeness_node += 1
            i += 1
    print("Closeness识别到正确节点数目：", Closeness_node, "召回率为：", 1.0 * Closeness_node / n)

    i = 0
    with open(Betweenness_path, 'r')as f:
        for lines in f.readlines():
            if i == n:
                break
            line = lines.strip("\n").split(" ")
            if line[0] in actual_node:
                Betweenness_node += 1
            i += 1
    print("Betweenness识别到正确节点数目：", Betweenness_node, "召回率为：", 1.0 * Betweenness_node / n)

if __name__=="__main__":
    recall_acc(650)