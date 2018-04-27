from skimage import io, transform
from find_structure import *
import glob
import os
import tensorflow as tf
import numpy as np
import time

#使用cnn进行训练，得到准确率最高时的3个权重
start_time = time.time()
path = 'img/'

# 将所有的图片resize
w =5
h = 3
c = 1            #c是指图像的通道数,灰度图像是单通道的

# 读取图片
def read_img(path):
    cate = [path + x for x in os.listdir(path) if os.path.isdir(path + x)]
    imgs = []
    labels = []
    for idx, folder in enumerate(cate):   #enumerate()同时得到index和value值
        print('reading the images from',folder)
        for im in glob.glob(folder + '/*.png'):
            img = io.imread(im)
            img = transform.resize(img, (w, h,1))
            #print(img.shape[2])
            imgs.append(img)
            labels.append(idx)
    # 转化成矩阵返回
    return np.asarray(imgs, np.float32), np.asarray(labels, np.int32)


data, label = read_img(path)

# 打乱顺序
num_example = data.shape[0]
arr = np.arange(num_example)
np.random.shuffle(arr)
data = data[arr]          #按照arr的顺序来重新排列data
label = label[arr]

# 将所有数据分为训练集和验证集
ratio = 0.1
s = np.int(num_example * ratio)
x_train = data[:s]
y_train = label[:s]
x_val = data[s:]
y_val = label[s:]

# -----------------构建网络----------------------
# 占位符
x = tf.placeholder(tf.float32, shape=[None, w, h,c], name='x')
y_ = tf.placeholder(tf.int32, shape=[None, ], name='y_')

# 第一个卷积层（8*3*1——>8*1*1),1个卷积核，步长是1,从截断的正态分布中输出随机值
#conv1 = tf.layers.conv2d(inputs=x, filters=1, kernel_size=[1,3], activation=tf.nn.relu,strides=1,name="conv1",
#                         kernel_initializer=tf.truncated_normal_initializer(stddev=0.01))

conv1 = tf.layers.conv2d(inputs=x, filters=1, kernel_size=[1,3], activation=tf.nn.relu,strides=1,name="conv1",
                         kernel_initializer=tf.random_uniform_initializer(minval=0, maxval=None))

re1 = tf.reshape(conv1, [-1, w * 1 * 1])

# 全连接层
dense1 = tf.layers.dense(inputs=re1, units=1024, activation=tf.nn.relu,
                         kernel_initializer=tf.truncated_normal_initializer(stddev=0.01),
                         kernel_regularizer=tf.contrib.layers.l2_regularizer(0.003))
dense2 = tf.layers.dense(inputs=dense1, units=512, activation=tf.nn.relu,
                         kernel_initializer=tf.truncated_normal_initializer(stddev=0.01),
                         kernel_regularizer=tf.contrib.layers.l2_regularizer(0.003))
logits = tf.layers.dense(inputs=dense2, units=w, activation=None,
                         kernel_initializer=tf.truncated_normal_initializer(stddev=0.01),
                         kernel_regularizer=tf.contrib.layers.l2_regularizer(0.003))
# ---------------------------网络结束---------------------------

loss = tf.losses.sparse_softmax_cross_entropy(labels=y_, logits=logits)
train_op = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)
correct_prediction = tf.equal(tf.cast(tf.argmax(logits, 1), tf.int32), y_)  #找一行中最大的那个值与标签比较
acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# 定义一个函数，按批次取数据
def minibatches(inputs=None, targets=None, batch_size=None, shuffle=False):
    assert len(inputs) == len(targets)
    if shuffle:
        indices = np.arange(len(inputs))
        np.random.shuffle(indices)
    for start_idx in range(0, len(inputs) - batch_size + 1, batch_size):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batch_size]
        else:
            excerpt = slice(start_idx, start_idx + batch_size)
        yield inputs[excerpt], targets[excerpt]


# 训练和测试数据，可将n_epoch设置更大一些

n_epoch = 80
batch_size = 300
max_acc=0;k_epoch=0;     #最大的准确率以及第几次迭代
save_csv=[]
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
for epoch in range(n_epoch):

    # training
    train_loss, train_acc, n_batch = 0, 0, 0
    for x_train_a, y_train_a in minibatches(x_train, y_train, batch_size, shuffle=True):
        _, err, ac = sess.run([train_op, loss, acc], feed_dict={x: x_train_a, y_: y_train_a})
        train_loss += err;
        train_acc += ac;
        n_batch += 1

    #得到每次卷积层的kernal值
    gr = tf.get_default_graph()
    conv1_kernel_val = gr.get_tensor_by_name('conv1/kernel:0').eval()
    #print(conv1_kernel_val)

    #计算训练准确率和误差
    train_loss_ave = train_loss / n_batch
    train_acc_ave=train_acc/n_batch
    print("第",epoch,"次结果：")
    print("   train loss: %f" % train_loss_ave)
    print("   train acc: %f" % train_acc_ave)

    # validation
    val_loss, val_acc, n_batch = 0, 0, 0
    for x_val_a, y_val_a in minibatches(x_val, y_val, batch_size, shuffle=False):
        err, ac = sess.run([loss, acc], feed_dict={x: x_val_a, y_: y_val_a})
        val_loss += err;
        val_acc += ac;
        n_batch += 1

    # 计算交叉验证的准确率和误差
    loss_val = val_loss / n_batch
    acc_val = val_acc / n_batch
    print("   validation loss: %f" % loss_val)
    print("   validation acc: %f" % acc_val)
    #保存下交叉验证的正确率最大值，以及此时的权重参数
    if acc_val>max_acc:
        max_acc=acc_val
        k_epoch=epoch
        w=[conv1_kernel_val[0][0][0][0],conv1_kernel_val[0][1][0][0],conv1_kernel_val[0][2][0][0]]

    #把每次运行的参数保存到一个列表，用于写入csv文件
    tmpL=[epoch,train_loss_ave,train_acc_ave,loss_val,acc_val,conv1_kernel_val[0][0][0][0],conv1_kernel_val[0][1][0][0],conv1_kernel_val[0][2][0][0]]
    save_csv.append(tmpL)

end_time=time.time()
num_time=end_time-start_time;
print("第",k_epoch ,"次迭代时达到最大准确率为：",max_acc)
print("最大准确率时的权重值：",w[0],"  ",w[1],"    ",w[2])
print("运行总时间为：",num_time)
savetxt("result/model/weibo_trick.csv",save_csv,fmt="%f",delimiter=",")
sess.close()