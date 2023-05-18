from random import shuffle
from math import sqrt

kn = int(input("Enter value of k: "))
no_of_points = int(input("Enter number of points: "))

points = []
means = []

for i in range(no_of_points):
    points.append(list(map(int, input().split( ))))

x = list(range(len(points)))
shuffle(x)
x = x[:kn]
for i in range(kn):
    means.append(points[x.pop()])

clusters = [ [] for _ in range(kn) ]

print(points)
print(means)

step_counter = 1
while True:
    clusters_copy = [ [] for _ in range(kn) ]
    print("\nStep ",step_counter,":\n")
    for i in range(len(points)):
        min_dist = []
        for j in range(len(means)):
            dist = 0
            for k in range(len(points[i])):
                dist += (points[i][k] - means[j][k]) ** 2
            dist = sqrt(dist)
            if len(min_dist) == 0:
                min_dist = [j, dist]
            elif min_dist[1] > dist:
                min_dist = [j, dist]
        clusters_copy[min_dist[0]].append(i)
    
    if clusters_copy == clusters:
        clusters = clusters_copy
        print("Final Cluster: ", [[points[j] for j in i] for i in clusters], "\nFinal Means: ", means)
        break
    means_copy = []
    for i in clusters_copy:
        x = [0 for _ in range(len(means[0]))]
        for j in i:
            for k in range(len(x)):
                x[k]+=points[j][k]
        for j in range(len(x)):
            x[j]/=len(i)
        means_copy.append(x)
    
    if means_copy == means:
        means = means_copy
        print("Final Cluster: ", [[points[j] for j in i] for i in clusters], "\nFinal Means: ", means)
        break
    means = means_copy
    clusters = clusters_copy
    print("Updated Cluster: ", [[points[j] for j in i] for i in clusters], "\nUpdated Means: ", means)
    step_counter += 1
