import numpy as np

def result_try(filepath,w,n):
    # parm：文件位置，3种结构影响度构成的列表，图中类别数目，acc是准确率，err是分类错误的个数，fal是错误的行数
    acc = 0;
    err = 0;
    fal = []
    data=[];true_labels=[]
    with open(filepath, 'r')as f:
        for lines in f.readlines():
            line=lines.strip('\n').split(',')
            data.append(line[1:n*3+1])
            true_labels.append(int(line[n*3+1]))

    # data是所有数据，true_label是节点真实类别，pre_labels是预测类别，Y是每个节点每种类别的可能性，其中最大可能的类别放入pre_labels
    pre_labels = np.zeros(len(data), int)
    Y = np.zeros([len(data), n], int)
    # ma是一行中最大的数,k代表ma的index，j代表类别
    for i in range(0, len(data)):
        ma = -100000;
        k = 0
        for j in range(n):
            num = int(data[i][j * 3]) * w[0] + int(data[i][j * 3 + 1]) * w[1] + int(data[i][j * 3 + 2]) * w[2]
            Y[i][j] = num
            if num >ma:
                ma = num
                k = j
        # print(Y[i]," ",k)
        pre_labels[i] = k
        if pre_labels[i] != true_labels[i]:
            err += 1
            wrong = [i, true_labels[i], pre_labels[i]]  # 记录下哪个节点
            # 被分错，真实类别与被预测的类别
            fal.append(wrong)

    print("错误的总数目：", err)
    acc = 1 - (err / len(data))
    np.savetxt("result/para_try_weibo.csv", fal, fmt="%d", delimiter=",")
    return acc


if __name__ == "__main__":
    acc = result_try("result/weibo.csv", [1 , 1,  1], 6)
    print("准确率为：", acc)