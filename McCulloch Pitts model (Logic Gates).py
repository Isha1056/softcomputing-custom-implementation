# Isha Gupta
# C022
# Implementation of logic gate (AND, OR, NOT, NAND, NOR ) using Mc-Culloch Pitts (MCP) model.

from functools import reduce
from random import randint

get_bin = lambda x, n: format(x, 'b').zfill(n) # Function to convert decimal to binary number of fixed length

def generate_table(type):   # Function to generate Truth tables
    if type == 3:
        return [[0,1],[1,0]],1,[randint(1,10)] 
    truth_table=[] 
    inps=int(input("Enter number of inputs: "))
    weights = [randint(1,10) for _ in range(inps)]
    for i in range(pow(2,inps)):
        x = list(map(int, list(get_bin(i,inps))))
        if type==1:
            x.append(reduce(lambda x, y: x & y, x))
        elif type==2:
            x.append(reduce(lambda x, y: x | y, x))
        elif type==4:
            x.append(int(not(reduce(lambda x, y: x & y, x))))
        else:
            x.append(int(not(reduce(lambda x, y: x | y, x))))          
        truth_table.append(x)
    return truth_table, inps, weights

ch=int(input("1. AND\n2. OR\n3. NOT\n4. NAND\n5. NOR\nEnter choice...")) # Choice based user iterface
truth_table,inps,weights=generate_table(ch)
print("Truth Table: "+ str(truth_table))
print("Weights: "+str(weights))
if ch==1:   # AND
    threshold = sum(weights)
    print("Threshold: return 0 if theta < "+str(threshold)+", else 1")
    for i in truth_table:
        x=0
        for j in range(len(weights)):
            x+=(i[j]*weights[j])
        print("\nCase "+str(i[:-1])+":")
        print("Truth table value: "+str(i[-1]))
        if x<threshold:
            print("Calculated value: 0")
        else:
            print("Calculated value: 1")

elif ch==2: # OR
    print("Threshold: return 1 if theta > "+str(0)+", else 0")
    for i in truth_table:
        x=0
        for j in range(len(weights)):
            x+=(i[j]*weights[j])
        print("\nCase "+str(i[:-1])+":")
        print("Truth table value: "+str(i[-1]))
        if x>0:
            print("Calculated value: 1")
        else:
            print("Calculated value: 0")
elif ch==3: # NOT
    threshold = sum(weights)
    print("Threshold: return 1 if theta < "+str(threshold)+", else 0")
    for i in truth_table:
        x=0
        for j in range(len(weights)):
            x+=(i[j]*weights[j])
        print("\nCase "+str(i[:-1])+":")
        print("Truth table value: "+str(i[-1]))
        if x<threshold:
            print("Calculated value: 1")
        else:
            print("Calculated value: 0")
elif ch==4: # NAND
    threshold = sum(weights)
    print("Threshold: return 1 if theta < "+str(threshold)+", else 0")
    for i in truth_table:
        x=0
        for j in range(len(weights)):
            x+=(i[j]*weights[j])
        print("\nCase "+str(i[:-1])+":")
        print("Truth table value: "+str(i[-1]))
        if x<threshold:
            print("Calculated value: 1")
        else:
            print("Calculated value: 0")
elif ch==5: # NOR
    print("Threshold: return 0 if theta > "+str(0)+", else 1")
    for i in truth_table:
        x=0
        for j in range(len(weights)):
            x+=(i[j]*weights[j])
        print("\nCase "+str(i[:-1])+":")
        print("Truth table value: "+str(i[-1]))
        if x>0:
            print("Calculated value: 0")
        else:
            print("Calculated value: 1")
