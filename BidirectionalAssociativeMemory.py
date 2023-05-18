# C022
# Isha Gupta
# Program to implement Auto Associative and Hetero Associative Neural network.

def actfun(ch, inp): # Activation function for limiting value
    if ch==1:
        if inp>0:
            return 1
        else:
            return 0
    else:
        if inp>=0:
            return 1
        else:
            return -1
# Input number of test cases from user
t = int(input("Enter number of test cases: "))

# Input number input matrix
nx = int(input("Enter number of inputs: "))
print("Enter input matrix:")
x = [ list(map(int, input().split())) for __ in range(t) ]

# Input number output matrix
ny = int(input("Enter number of outputs: "))
print("Enter output matrix:")
y = [ list(map(int, input().split())) for __ in range(t) ]

# Initialize weight matrix
w = [[0 for _ in range(ny)] for __ in range(nx)]
target = [ [0 for _ in range(ny)] for __ in range(t)]

for __ in range(t):
    # Weight calculation for each test cases
    for i in range(nx):
        for j in range(ny):
            w[i][j] = w[i][j] + (x[__][i]*y[__][j])
# Calculate output
for __ in range(t):
    for i in range(ny):
        for j in range(nx):
            target[__][i] += x[__][j]*w[j][i]
        target[__][i] = actfun(1, target[__][i])

# Final weights and result
print("Final weights: ",w)
print("Result: ",target)

# Testing with mistaken values
print("For mistaken value, Enter test matrix: ")
checkInput = [ list(map(int, input().split())) for __ in range(t) ]
checkTarget = [ [0 for _ in range(ny)] for __ in range(t) ]
for __ in range(t):
    for i in range(ny):
        for j in range(nx):
            checkTarget[__][i] += checkInput[__][j]*w[j][i]
        checkTarget[__][i] = actfun(1, checkTarget[__][i])
print("Test 1, Target values: ", checkTarget)

# Testing with missing values
print("For missing value, Enter test matrix: ")
checkInput = [ [int(_) if _.isnumeric() else _ for _ in input().split()] for __ in range(t) ]
checkTarget = [ [0 for _ in range(ny)] for __ in range(t) ]
for __ in range(t):
    for i in range(ny):
        for j in range(nx):
            if not type(checkInput[__][j]) == str:
                checkTarget[__][i] += checkInput[__][j]*w[j][i]
        checkTarget[__][i] = actfun(1, checkTarget[__][i])
print("Test 2, Target values: ", checkTarget)
