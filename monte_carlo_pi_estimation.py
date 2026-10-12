import matplotlib.pyplot as plt
import numpy as np
import random

#estimate pi using the fact that the area of a square circumscribing a circle is (4/pi)*(the area of that circle), so we use repeated 
#random numbers to find the ratio between the area of the square and the circle, giving us the value of pi.

def magnitude(x,y):
    return((x**2 + y**2)**(1/2))

def monte_carlo_pi_estimation(radius,n):
    counter = 0 #counts how many points generated are inside the circle
    for i in range(0,n):
        a = [random.uniform(-radius,radius),random.uniform(-radius,radius)]
        if magnitude(a[0],a[1]) < radius: #see whether the point is within the circle or outside it
            counter += 1   
    pi = 4*counter/n
    return(pi)

print(f"pi = {monte_carlo_pi_estimation(1,1000000)}")
