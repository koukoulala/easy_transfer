import numpy as np
import os
from PIL import Image

#把节点邻居结构的csv文件转换成一个节点一个image，不同类别放在不同文件夹中，每个节点都是n行3列的图片
#注意，将数目都*10，防止梯度消失
with open('result/bcspwr_node_2.csv','r') as csvfile:
    for line in csvfile.readlines():
        node_img = []
        img = []
        line=line.strip('\n').split(',')
        len_csv=len(line)
        node=line[0]
        label=line[len_csv-1]
        #把一行数据转换成n*3的图片
        for i in range(1,len_csv-1):
            node_img.append(int(line[i])*10)
        #print(node_img)
        tmp=np.array(node_img,dtype='float')
        img=tmp.reshape([8,3])
        #print(img)
        image=Image.fromarray(img) #从数据生成image对象

        #生成保存image的路径
        path="img/bcspwr_"+label
        if not os.path.isdir(path):
            os.makedirs(path)
        path =path+ "/" + node + ".png"
        image_save=image.convert("L")#转化为灰度图片(这一步很关键，不然图片不能以png格式保存)
        image_save.save(path)