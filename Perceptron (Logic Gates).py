# Isha Gupta
# C022
# Implementation of logic gate (AND, OR, NOT, NAND, NOR ) using Perceptron

from random import randint
from functools import reduce

def fun(x,th): # Threshold function
    if x>th:
        return 1
    elif x<-th:
        return -1
    else: 
        return 0

def generate_tt(ch): # Function to generate truth table
    if ch==5:
        inps=1
    else:
        inps = int(input("Enter number of inputs: "))   # Number of inputs
    tt = []
    th = int(input("Enter Threshold value: "))  # Threshold value for calculation
    for i in range(pow(2, inps)):
        x = f'{i:0{inps}b}'
        x = list(map(int, list(x)))
        if ch==1:
            c = reduce(lambda a, b: a & b, x)   # AND
        elif ch==2:
            c = reduce(lambda a, b: a | b, x)   # OR
        elif ch==3:
            c = reduce(lambda a, b: int(not(a & b)), x) # NAND
        elif ch==4:
            c = reduce(lambda a, b: int(not(a | b)), x) # NOR
        elif ch==5:
            c=int(not(x[0]))    # NOT
        else:
            c = reduce(lambda a, b: a & int(not(b)), x) # ANDNOT
        x.append(1)
        x.append(c)
        x = [1 if i == 1 else -1 for i in x]
        tt.append(x)
    return tt, th

def realization(tt,w):      # Function to perform realization
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

def get_weights(tt,th):     # Function to calculate weights
    w = [0] * (len(tt[0]) - 1)      # Initialize weights to 0
    print("\nInitial weights: ", w)
    alpha=1                         # Initial alpha value
    w_org=w.copy()
    while True:     # Calculate weights in each epoch 
        for i in tt:
            res=0
            for j in range(len(w)):     # Calculate truth value
                res+=w[j]*i[j]
            if fun(res,th)!=i[-1]:          # Check if calculated value matches actual value
                for j in range(len(w)):
                    w[j] = w[j]+alpha*i[-1]*i[j]        # Recalculate weights if variation
        if w!=w_org:
            print("Weights unchanged: ",w)
            break
        else: 
            print("Changed weights: ",w)
            w_org=w.copy()
    print("Weights selected: ", w)
    return w

# Driver code
ch = int(input("1. AND\n2. OR\n3. NAND\n4. NOR\n5. NOT\n6. ANDNOT\nEnter choice..."))
tt,th=generate_tt(ch)
w=get_weights(tt,th)
realization(tt,w)
