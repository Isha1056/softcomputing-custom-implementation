# Isha Gupta
# C022
# Compute union,intersection,difference and compliemnt operations on fuzyy sets. Plot Triangluar member function, Trapozidal member function,Sigmodal member function 
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


# Defining sets and results
size = int(input("Enter the size of sets: "))
setA = [float(i) for i in input().split() ]
memA = [float(i) for i in input().split() ]
setB = [float(i) for i in input().split() ]
memB = [float(i) for i in input().split() ]
print(setA,setB,memA, memB)
union_Operation = []
intersection_Operation = []
compliment_OperationA = []
compliment_OperationB = []
differnce_OperationAnB = []
differnce_OperationBnA = []


# Union Operation
def unionOperation(memA,memB):
    for i in range(size):
        union_Operation.append(max(memA[i],memB[i]))
    print("\nOrignal member values/ corresponding set value:")
    for i in range(size):
        print(str(memA[i])+"/"+str(setA[i])+",", end=' ')
    print("\nAfter union operation on set A and Set B (A OR B):")
    for i in range(size):
        print(str(union_Operation[i])+"/"+str(setA[i])+",", end=' ')
    return union_Operation


# Intersection Operation
def intersectionOperation(memA,memB):
    for i in range(size):
        intersection_Operation.append(min(memA[i],memB[i]))
    print("\nOrignal member values/ corresponding set A value:")
    for i in range(size):
        print(str(memA[i])+"/"+str(setA[i])+",", end=' ')
    print("\nOrignal member values/ corresponding set B value:")
    for i in range(size):
        print(str(memB[i])+"/"+str(setB[i])+",", end=' ')
    print("\nAfter intersetion operation on set A and Set B (A AND B):")
    for i in range(size):
        print(str(intersection_Operation[i])+"/"+str(setA[i])+",", end=' ')
    return intersection_Operation


# Difference operation
def differnceOperation(memA,memB):
    for i in range(size):
        compliment_OperationA.append(1-memA[i])
        compliment_OperationB.append(1-memB[i])
    for i in range(size):
        differnce_OperationAnB.append(intersectionOperation(memA, compliment_OperationB))
        differnce_OperationBnA.append(intersectionOperation(memB, compliment_OperationA))
    print("\nOrignal member values/ corresponding set value:")
    for i in range(size):
        print(str(memA[i])+"/"+str(setA[i])+",", end=' ')
    print("\nAfter difference operation on set A and Set B (A | B):")
    for i in range(size):
        print(str(differnce_OperationAnB[i])+"/"+str(setA[i])+",", end=' ')
    print("\nAfter difference operation on set A and Set B (B | A):")
    for i in range(size):
        print(str(differnce_OperationBnA[i])+"/"+str(setA[i])+",", end=' ')
    return differnce_OperationAnB,differnce_OperationBnA


# Compliment
def complimentOperation(memA,memB):
    for i in range(size):
        # print(1-memA[i])
        compliment_OperationA.append(1-memA[i])
        compliment_OperationB.append((1-memB[i]))
    print("\nOrignal member values/ corresponding set A value:")
    for i in range(size):
        print(str(memA[i])+"/"+str(setA[i])+",", end=' ')
    print("\nOrignal member values/ corresponding set B value:")
    for i in range(size):
        print(str(memB[i])+"/"+str(setB[i])+",", end=' ')
    print("\nAfter compliment operation on set A (-A):")
    for i in range(size):
        print(str(compliment_OperationA[i])+"/"+str(setA[i])+",", end=' ')
    print("\nAfter compliment operation on Set B (-B):")
    for i in range(size):
        print(str(compliment_OperationB[i])+"/"+str(setA[i])+",", end=' ')
    return compliment_OperationA,compliment_OperationB


# Taking user choice
choice = input("Enter the choice: \n1. Union on input sets \n2. Intersection on input sets \n3. difference on input sets \n4. Compliment on input sets \n")
if choice == '1':
    unionOperation(memA,memB)
elif choice == '2':
    intersectionOperation(memA,memB)
elif choice == '3':
    differnceOperation(memA,memB)
elif choice == '4':
    complimentOperation(memA,memB)
else:
    print("Invalid choice")


# Displaying Result
x = np.arange(2000)
mfx = fuzz.trimf(x, [500,1000, 1500])
print(x,mfx)
plt.plot(x,mfx,label = "Triangluar member function")
mfxtrapmf = fuzz.trapmf(x, [1,500,1500,2000])
plt.plot(x,mfxtrapmf,label = "Trapozidal member function")
mfxsigmod = fuzz.sigmf(x,750,0.05)
print(mfxsigmod)
plt.plot(x,mfxsigmod,label = "Sigmodal member function")
plt.xlabel('Set element Values')
plt.ylabel('Member function values')
plt.legend()
plt.show()
