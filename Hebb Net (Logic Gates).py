# Isha Gupta
# C022
# Implementation of logic gate (AND, OR, NOT, NAND, NOR ) using Hebb Net. 

from random import randint
from functools import reduce

def generate_tt(ch):    # Generating Truth Table
    if ch==5:
        inps=1
    else:
        inps = int(input("Enter number of inputs: "))
    tt = []
    for i in range(pow(2, inps)):
        x = f'{i:0{inps}b}'
        x = list(map(int, list(x)))
        if ch==1:
            c = reduce(lambda a, b: a & b, x)
        elif ch==2:
            c = reduce(lambda a, b: a | b, x)
        elif ch==3:
            c = reduce(lambda a, b: int(not(a & b)), x)
        elif ch==4:
            c = reduce(lambda a, b: int(not(a | b)), x)
        else:
            c=int(not(x[0]))
        x.append(1)
        x.append(c)
        x = [1 if i == 1 else -1 for i in x]
        tt.append(x)
    return tt

def realization(tt,w):  # Realization to check output
    print("\nREALIZATION:")
    for i in tt:
        s=[]
        x=0
        for j in range(len(w)):
            s.append("("+str(w[j])+"*"+str(i[j])+")")
            x+=w[j]*i[j]
        print("Equation "+str(j)+": "+"+".join(s))
        print("Result from weights: ",x)
        print("Result from Bipolar function: ", 1 if x>0 else -1)
        print("Result from truth table: ",i[-1])
        print()

def get_weights(tt):    # Calculating weights
    w = [0] * (len(tt[0]) - 1)
    print("\nInitial weights: ", w)
    for i in tt:
        for j in range(len(w)):
            w[j] = w[j] + i[j] * i[-1]
        print("Changed Weights: ", w)
    print("Weights selected: ", w)
    return w

ch = int(input("1. AND\n2. OR\n3. NAND\n4. NOR\n5. NOT\nEnter choice..."))
tt=generate_tt(ch)
w=get_weights(tt)
realization(tt,w)
