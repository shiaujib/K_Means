import math
import random

data=[]
sample=[[1.0, 1.0], [1.5, 2.0], [3.0, 4.0], [5.0, 7.0], [3.5, 5.0], [4.5, 5.0], [3.5, 4.5]]
centroids=[]

clusNum=2
dataNum=7
maxIndex=5
minIndex=5

class dataPoint:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def set_x(self,x):
        self.x=x

    def set_y(self,y):
        self.y=y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

    def set_clus(self,clus):
        self.clus=clus
    def get_clus(self):
        return self.clus


class centroid:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def set_x(self,x):
        self.x=x

    def set_y(self,y):
        self.y=y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

def find_min_max():
    min=1000000
    max=0
    for i in range(dataNum):
        value=data[i].get_x()+data[i].get_y()
        if value>max:
            max=value
            global maxIndex
            maxIndex=i
        if value<min:
            min=value
            global minIndex
            minIndex=i
    maxData=max
    minData=min
    print maxIndex
    print minIndex
        


def init_centroid():
    centroids.append(centroid(sample[minIndex][0],sample[minIndex][1])) #0 is minimum data
    centroids.append(centroid(sample[maxIndex][0],sample[maxIndex][1])) #3 is maximum data
    
def init_dataPoint():
    for i in range(dataNum):
        newPoint=dataPoint(sample[i][0],sample[i][1])
        if i==minIndex:
            newPoint.set_clus(0)
        elif i==maxIndex:
            newPoint.set_clus(1)
        else:
            newPoint.set_clus(None)
        data.append(newPoint)

def get_distance(datax,datay,cenx,ceny):
    return math.sqrt(math.pow((cenx-datax),2)+math.pow((ceny-datay),2))


def update_centroid():
    totalX=0
    totalY=0
    totalInClus=0
    for i in range(clusNum):
        for j in range(dataNum):
            #print "clus  ",data[j].get_clus()
            if data[j].get_clus()==i:
                totalX=totalX+data[j].get_x()
                totalY=totalY+data[j].get_y()
                totalInClus+=1
                #print "total clus",totoalInClus
                #print "clus  ",data[j].get_clus()
        if totalInClus>0:
            centroids[i].set_x(totalX/totalInClus)
            centroids[i].set_y(totalY/totalInClus)
            totalX=0
            totalY=0
            totalInClus=0
    
    
def update_clus():
    min=1000000
    moveFlag=0
    for i in range(dataNum):
        min=1000000
        clusIndex=0
        for j in range(clusNum):
            tmpMin=get_distance(data[i].get_x(),data[i].get_y(),centroids[j].get_x(),centroids[j].get_y())
            if tmpMin<min:
                min=tmpMin
                clusIndex=j
        if (data[i].get_clus()is None or data[i].get_clus()!=clusIndex):
            data[i].set_clus(clusIndex)
            moveFlag=1
    return moveFlag

def K_mean():
    count=0
    moveFlag=1
    init_dataPoint()
    find_min_max()
    init_centroid()
    print_result()
    while moveFlag==1:
        count+=1
        print count
        moveFlag=update_clus()
        update_centroid()
        #print_result()
        

def print_result():
    for i in range(clusNum):
        print "Cluster ",i
        for j in range(dataNum):
            if(data[j].get_clus() == i):
                print("(", data[j].get_x(), ", ", data[j].get_y(), ")")
        print "centroid" ,centroids[i].get_x(),"  ",centroids[i].get_y() 

K_mean()
print_result()
