# Isha Gupta
# C022
# Back Propagation Training Algorithm 

import math

def calculateNetOutput(v00, x0, v10, x1, v11): # Function to calculate Net output f(Zin)
    zin1 = v00*1 + x0*v10 + x1*v11
    fzin1 = calActivation(zin1)
    return fzin1

def calActivation(Zin1): # Sigmoid activation function
    if activationFunction == 1:  # Binary sigmoid
        f = 1/(1+((math.e)**-(Zin1)))
    else:                        # Bipolar sigmoid
        f = 2/(1+((math.e)**-(Zin1)))
    return f

def calDerivate(Y): # Function to return Derivative
    return Y*(1-Y)

nx = int(input("\nEnter the number of input layer:\t"))
nz = int(input("\nEnter the number of hidden layer:\t"))
ny = int(input("\nEnter the number of output layer:\t"))
activationFunction = int(input("Solve it using?\n1. Binary sigmodal\n2. Bipolar Sigmodal\nChoose..."))
x = []
for i in range(nx):
    inputx = input("\nEnter value of x["+str(i)+"]:\t")
    x.append(float(inputx))

target = float(input("\nEnter the target value(t):\t")) # input target value
b = float(input("\nEnter the bias weight [w0] value:\t")) # input weight for bias
vi=[] 
for i in range(nx+1): # input weights at all layers
    row = []
    for j in range(nz):
        element = input("\nEnter value of v["+str(i)+"]["+str(j)+"]:\t")
        row.append(float(element))
    vi.append(row)
hw = [] 
for i in range(nz): # input weights for bias at hidden layer
    h = float(input("\nEnter hidden layer weights hw["+str(i)+"]:\t"))
    hw.append(h)
alpha = float(input("\nEnter the value of learning rate (alpha):\t")) #input learning rate
#initializing variables and lists
Y = 0 
Z = [0]*nz
din = [0]*nz
dw = [0]*nz
deltaError = [0]*nz
epoch = 1
wc = [] 

while(Y != target): # Continues Epochs until output matches the target values
    print(f"\nEPOCH - {epoch}")
    for i in range(nz): # Calculate net input for hidden layer (Zi layer)
        Z[i] = calculateNetOutput(vi[0][i], x[0], vi[i+1][0], x[1], vi[i+1][1])
        Y += Z[i]*hw[i] # Calculate value of (Yin)
    Y += b # Add bias weight to Y
    Y = calActivation(Y) # Calculating the net input entering the outer later with the activation function
    Y = float("{0:.5f}".format(Y))
    print("The value of Y: "+str(Y))

    delta = (target-Y)*calDerivate(Y) # computing the error portion Delta(k)

    for i in range(nz): # Calulating change in weights beterrn hidden and ouput layer
        dw[i] = alpha*delta*Z[i]
    dw.insert(len(dw), (alpha*delta)) # inserting the weight change of bias

    for i in range(nz): # computing the error portion Delta(j) between input and hidden layer
        din[i] = delta*hw[i] # list of delta(in)
        deltaError[i] = din[i]*calDerivate(Z[i]) # list containing Error Delta (Zinj)
        
    
    k = 0
    for i in range(nx+1): # weights updation (delta Vij values)
        row = []
        for j in range(nz):
            if i == 0:
                element = alpha*deltaError[j]
            else:
                element = alpha * deltaError[k] * x[j]
            row.append(float(element))
        if i>0:
            k+=1
        wc.append(row)

    for i in range(len(vi)): # Computing the final weights (v11,v12, v21,v22)
        for j in range(len(vi[i])):
            vi[i][j] += wc[i][j]

    for i in range(len(hw)): # Computing the final bias weights (w1,w2,w0)
        hw[i] += dw[i]
    b+=dw[-1] # computing the final bias weight
    print("The value of weights ([v01,v02],[v11,v21],[v12,v22]) are: ", vi)
    print("The value of Bias Weights(w1,w2,w0) are: ", hw)
    print("Value of bias: ", b)
    epoch+=1 # increment the EPOCH till the stopping condition