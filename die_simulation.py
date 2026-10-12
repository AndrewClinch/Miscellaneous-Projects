import random

n1=0
n2=0
n3=0
n4=0
n5=0
n6=0

x = 100

for i in range(0,x):
    roll = random.randint(1,6)
    if roll == 1:
        n1 = n1 + 1
    elif roll == 2:
        n2 = n2 + 1
    elif roll == 3:
        n3 = n3 + 1
    elif roll == 4:
        n4 = n4 + 1
    elif roll == 5:
        n5 = n5 + 1
    elif roll == 6:
        n6 = n6 + 1

print(f"n1 = {n1}")
print(f"n2 = {n2}")
print(f"n3 = {n3}")
print(f"n4 = {n4}")
print(f"n5 = {n5}")
print(f"n6 = {n6}")

print(f"the probability of rolling a 1 is {n1/x}")
print(f"the probability of rolling a 2 is {n2/x}")
print(f"the probability of rolling a 3 is {n3/x}")
print(f"the probability of rolling a 4 is {n4/x}")
print(f"the probability of rolling a 5 is {n5/x}")
print(f"the probability of rolling a 6 is {n6/x}")