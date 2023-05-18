# Isha Gupta
# C022
# Program to implement Winner Takes It All learning algorithm

from random import randint
from copy import deepcopy

# Defining container for set of points
set_size = int(input("Enter number of set points: "))
set_points = []
c_weights = []

# Input set of points
for i in range(set_size):
    t = []
    for j in input().split():
        t.append(int(j))
    set_points.append(t)

# Shortlisting range for selecting random cluster centers (weight columns) from given points
for i in range(len(set_points[0])):
    x = [set_points[_][i] for _ in range(len(set_points))]
    c_weights.append([min(x), max(x)])

# Defining network - input and output layer, weights and clusters
input_neurons = len(set_points[0])
output_neurons = int(input("Enter number of output neurons: "))
w = [ [ randint(c_weights[i][0], c_weights[i][1]) for j in range(output_neurons)] for i in range(input_neurons)]

epoch_counter = 1
cluster = []

print("Set Points: ", set_points)
print("Initial weights: ", w)

# Epoch loop
while True:
    print("\n\nEpoch: ",epoch_counter)
    w_copy = deepcopy(w)
    cluster = []

    # Calculating smallest distance from set of points to each cluster
    for i in set_points:
        D = []
        for j in range(output_neurons):
            s = 0
            for k in range(input_neurons):
                s += (w_copy[k][j] - i[k])**2
            if len(D) == 0:
                D = [j, s]
            elif s < D[1]:
                D[0] = j
                D[1] = s

        # Assigning point to closest cluster
        cluster.append([i, D[0]])

        # Updating weights (cluster center) based on newly assigned point
        for j in range(input_neurons):
            w_copy[j][D[0]] = w_copy[j][D[0]] + 0.5*(i[j] - w_copy[j][D[0]])
    
    # Check if clusters from current epoch match previous epoch to stop iteration
    if w_copy == w:
        w = w_copy
        print("Final Weights: ", w)
        break
    else:
        epoch_counter+=1
        w = w = w_copy
        print("Updated Weights: ", w)

# Output final clusters
for i in cluster:
    print("Point",i[0],"belongs to cluster",i[1])