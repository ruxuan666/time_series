#使用shape_distance方法比较两时间序列的相似性

#仅使用3种模式(1,0,-1,由所在段斜率决定)，且不进行规范化操作
#使用知乎中的例子https://zhuanlan.zhihu.com/p/69170491
S1=[[5,0],[6,1],[4.5,2],[3,3],[3,4.5]]#y值,t值
S2=[[2,0],[4,1],[6,2],[5,3],[4,4.5]]
"""#根据总的分割点确定两个模式序列
s1=[[1,1],[-1,2],[-1,3],[0,4.5]]
s2=[[1,1],[1,2],[-1,3],[-1,4.5]]"""
#计算模式值并计算shape_distance
dis=0
for i in range(1,len(S1)):#累加每一段结果
    if S1[i][0]-S1[i-1][0]>0:
        m1=1
    elif S1[i][0]-S1[i-1][0]==0:
        m1=0
    else:
        m1=-1

    if S2[i][0]-S2[i-1][0]>0:
        m2=1
    elif S2[i][0]-S2[i-1][0]==0:
        m2=0
    else:
        m2=-1
    t=S1[i][1]-S1[i-1][1]#该时间段的时间权重
    m=abs(m1-m2)#模式差绝对值
    a=S1[i][0]-S1[i-1][0]#第一个序列该时间段y值变化
    b= S2[i][0] - S2[i - 1][0]
    dis+=t*m*abs(a-b)
print('shape_distance',dis)


#根据斜率的变化确定7种模式，且对数据进行规范化处理来计算shape_distance
#[-3,-2,-1,0,1,2,3]#本阶段斜率负的且变小；斜率负的不变；斜率负的变大；本阶段斜率接近0；
S1_min=min(S1[:][0])
S1_max=max(S1[:][0])
S2_min=min(S2[:][0])
S2_max=max(S2[:][0])
S_min=min(S1_min,S2_min)
S_max=max(S1_max,S2_max)
S_diff=S_max-S1_min
th=0.5
#数据规范化处理
for i in range(len(S1)):
    S1[i][0]=(S1[i][0]-S_min)/S_diff
    S2[i][0]=(S2[i][0]-S_min)/S_diff
th=th/S_diff
print('规范化的阈值',th)
#确定斜率序列
K1,K2=[],[]
for i in range(1,len(S1)):
    k1=(S1[i][0]-S1[i-1][0])/(S1[i][1]-S1[i-1][1])
    k2 = (S2[i][0] - S2[i-1][0]) / (S2[i][1] - S2[i-1][1])
    K1.append(k1)
    K2.append(k2)
print(K1)
print(K2)
#根据斜率升降规则确定模式,并计算距离
dis=0
for i in range(len(K1)):
    if i==0:#第一段模式的确定
        if K1[i]<-th:
            m1=-3
        elif K1[i]>th:
            m1=3
        else:
            m1=0
        if K2[i] < -th:
           m2 = -3
        elif K2[i] > th:
           m2 = 3
        else:
           m2 = 0

    else: #其它段的模式确定
        if K1[i] < -th and K1[i] < K1[i - 1]:
            m1 = -3
        elif K1[i] < -th and K1[i] == K1[i - 1]:
            m1 = -2
        elif K1[i] < -th and K1[i - 1] < K1[i]:
            m1 = -1
        elif K1[i] > th and K1[i] < K1[i - 1]:
            m1 = 1
        elif K1[i] > th and K1[i] == K1[i - 1]:
            m1 = 2
        elif K1[i] > th and K1[i] > K1[i - 1]:
            m1 = 3
        else:
            m1 = 0

        if K2[i] < -th and K2[i] < K2[i - 1]:
            m2 = -3
        elif K2[i] < -th and K2[i] == K2[i - 1]:
            m2 = -2
        elif K2[i] < -th and K2[i - 1] < K2[i]:
            m2 = -1
        elif K2[i] > th and K2[i] < K2[i - 1]:
            m2 = 1
        elif K2[i] > th and K2[i] == K2[i - 1]:
            m2 = 2
        elif K2[i] > th and K2[i] > K2[i - 1]:
            m2 = 3
        else: #该时间段斜率取中间值时
            m2 = 0

    t = S1[i+1][1] - S1[i][1]  # 该时间段的时间权重
    dis+=t*abs(m1-m2)*abs((S1[i+1][0]-S1[i][0])-(S2[i+1][0]-S2[i][0]))
print('shape_dis1',dis)
