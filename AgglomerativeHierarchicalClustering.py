from math import sqrt
import heapq
from sys import maxsize

def print_table(dist_table):
    for i in dist_table.keys():
        print(i,dist_table[i])

def dist(p1, p2):
    res = 0
    for i in range(len(p1)):
        res += pow((p1[i]-p2[i]), 2)
    return sqrt(res)

def single_link(p1,p2,p3,pdist_table):
    return min(dist_table[p1][p3], dist_table[p2][p3])

def complete_link(p1,p2,p3,pdist_table):
    return max(dist_table[p1][p3], dist_table[p2][p3])

ch = int(input("1. Single Link\n2. Complete Link\nEnter choice..."))
n = int(input("Enter number of points: "))
points = {}
for i in range(n):
    points["p"+str(i+1)] = list(map(float, input().split()))

dist_table = {}
min_dist = []
heapq.heapify(min_dist)

for i in range(len(points)):
    dist_table["p"+str(i+1)] = {}
    m = [maxsize,()]
    for j in range(len(points)): 
        dist_table["p"+str(i+1)]["p"+str(j+1)] = (dist(points["p"+str(i+1)], points["p"+str(j+1)]))
        if j<i and m[0] > dist_table["p"+str(i+1)]["p"+str(j+1)]:
            m = [dist_table["p"+str(i+1)]["p"+str(j+1)], ("p"+str(i+1), "p"+str(j+1))]
    if len(m[1]) > 0:
        heapq.heappush(min_dist, m)

print(min_dist)

print()
print_table(dist_table)
print()

while len(dist_table) > 1:
    x = heapq.heappop(min_dist)

    while x[1][0] not in dist_table and x[1][1] not in dist_table and len(min_dist)>0:
        x = heapq.heappop(min_dist)

    print("Next option: ",x)
    m = [maxsize, ()]
    dist_table[x[1][0]+x[1][1]] = {}
    for i in dist_table.keys():
        if ch==1:
            dist_table[i][x[1][0]+x[1][1]] = single_link(x[1][0], x[1][1], i, dist_table)
        else:
            dist_table[i][x[1][0]+x[1][1]] = complete_link(x[1][0], x[1][1], i, dist_table)
        dist_table[x[1][0]+x[1][1]][i] = dist_table[i][x[1][0]+x[1][1]]

        if m[0] > dist_table[i][x[1][0]+x[1][1]] and dist_table[i][x[1][0]+x[1][1]]>0 and i!=x[1][0] and i!=x[1][1]:
            m = [dist_table[x[1][0]+x[1][1]][i], (i, x[1][0]+x[1][1])]
    del dist_table[x[1][0]]
    del dist_table[x[1][1]]
    heapq.heappush(min_dist, m)
    
    print()
    print_table(dist_table)
    print()
