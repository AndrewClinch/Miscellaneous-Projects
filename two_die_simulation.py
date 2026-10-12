import random
import matplotlib.pyplot as plt
import numpy as np

#create list variables
d=[] #list of roll outcomes
n=[] #list of outcome counts
x_axis = []

z=100000 #number of rolls

#input whether the dice are loaded or not
loaded = int(input("input: 1 for fair, 2 for loaded"))

#assign values to lists
if loaded % 2 == 1:
    for i in range(z):
        d1=random.randint(1,6)
        d2=random.randint(1,6)
        r=d1+d2
        d.append(r)
else:
    distribution = [0.12,0.12,0.12,0.12,0.12,0.4]
    for i in range(z):
        d1 = np.random.choice([1,2,3,4,5,6] , p = distribution)
        d2 = np.random.choice([1,2,3,4,5,6] , p = distribution)
        r = d1 + d2
        d.append(r)

for i in range(2,13):
    y=d.count(i)
    n.append(y)
    x_axis.append(i)

#plot histogram of counts vs roll addition
plt.bar(x_axis,n)
plt.show(block=False)

#calculate experimantal mean and variance
mean=0
for i in range(2,13):
    mean += i*n[i-2]/z

var = 0
for i in range (2,13):
    var = var + (n[i-2]/z)*((mean-i)**2)

print(f"mean = {mean}")
print(f"variance = {var}")

#calculate P(sum >= x)
x = 10
P = 0
for i in range(x,13):
    P = P + n[i-2]/z

print(f"P(sum >= {x}) = {P}")

#
input()
