import numpy as np
import matplotlib.pyplot as plt
import random

#define a function to simulate a random walk starting at position x and show the path taken
def walk_path(x,p_back,p_forward):
    d = [x] #list containing walk history
    time = [0] #list for the x axis of the graph
    x1 = x

    #create a for loop which randomly changes x by +1 or -1 each iteration
    for i in range(0,100):
        n = np.random.choice([1,2],p = [p_back, p_forward])
        if n%2 == 0:
            x += 1
        else:
            x -= 1
        d.append(x)
        time.append(i+1)

    plt.figure()
    plt.plot(time,d)
    plt.title(f"Path taken on a singular walk starting at {x1}")
    plt.xlabel("iteration")
    plt.ylabel("displacement")
    plt.show(block = False)


#define a function to simulate a random walk and collect the final positions of many different trials
def walk_endpoint(x,p_back,p_forward):
    p = [] #list consisting of ending points of walks
    c = [] #list consisting of counts of ending points of different walks
    x_axis = list(range(-100,101))
    
    #create a for loop to collect the results of many random walks
    for i in range(0,1000):
        x1 = x
        #create a for loop which randomly changes x by +1 or -1 each iteration
        for i in range(0,100):
            n = np.random.choice([1,2],p = [p_back, p_forward])
            if n%2 == 0:
                x1 += 1
            else:
                x1 -= 1
        
        p.append(x1)
    
    #assign values to c
    for i in range(-100,101):
        c.append(p.count(i))
    
    #calculate mean and variance
    mean = float()
    var = float()

    for i in range(0,len(c)): #mean
        mean += (i-100)*c[i]/sum(c)
    
    for i in range(0,len(c)): #var
        var += ((mean - (i-100))**2)*c[i]/sum(c)

    print(f"mean of endpoints = {mean}")
    print(f"variance of endpoints = {var}")

    #plot histogram of frequency of endpoints vs endpoints
    plt.figure()
    plt.bar(x_axis,c)
    plt.title("Frequency of ending position vs ending position")
    plt.xlabel("ending position")
    plt.ylabel("frequency")
    plt.show(block = False)

x = 0 #starting position
p_back = 0.5
p_forward = 0.5

walk_path(x,p_back,p_forward)

walk_endpoint(x,p_back,p_forward)

input()