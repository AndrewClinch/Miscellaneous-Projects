import numpy as np
import matplotlib.pyplot as plt
import random



def function(domain): #the function is x^2
    if type(domain) == list or type(domain) == tuple:
        y = []
        for i in range(0,len(domain)):
            a = (domain[i])**2
            y.append(a)
    elif type(domain) == int or type(domain) == float:
        y = domain**2
    return y    

#function that calculates the area under the curve between the limits
def area(lim1,lim2):
    domain = list(range(lim1,lim2+1,1))
    y = function(domain)
    random_scatter = []
    count = 0
    x = 1000
    for i in range(0,x):
        a = random.uniform(lim1,lim2)
        b = random.uniform(min(y),max(y))
        print(type(a))
        if b < function(a):
            count += 1
        random_scatter.append([a,b])

    area_ = (lim2 - lim1)*(max(y) - min(y))*count/x
    print(f"area under curve = {area_}")

    random_scatter = np.array(random_scatter)

    plt.figure()
    plt.plot(domain,y)
    plt.scatter(random_scatter[:,0],random_scatter[:,1])
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.show()


area(0,10)