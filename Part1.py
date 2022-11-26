#Part1
import numpy as np
import numpy.random as npr

#Qn-1
x = np.arange(1,11)
x+= 1
print("\n")
print(x)

#Qn-2
x = np.arange(100)
x=x.reshape(10,10)
for i in range(10):
    for j in range(10):
        x[i,j]=i+j
print("\n")
print(x)

#Qn-3
data=np.exp(npr.randn(50, 5))
normalized=data

#Qn-4
stdDev=np.std(data,axis=0) 
meanData=np.mean(data, axis=0)
print("\n")
print("Standard Deviation: ",stdDev)
print("Mean: ",meanData)

#Qn-5
for i in range(50):
    for j in range(5):
        normalized[i,j]=(data[i,j]-meanData[j])/stdDev[j]
stdDevNorm=np.std(normalized,axis=0)
meanNorm=np.mean(normalized, axis=0)
print("\n")
print("Standard Deviation of Normalized Matrix: ",stdDevNorm)
print("Mean of Normalized Matrix: ",meanNorm)
