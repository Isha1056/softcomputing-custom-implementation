# Isha Gupta
# C022
# Implementation of logic gate (XOR) using Mc-Culloch Pitts (MCP) model.

from functools import reduce
from random import randint

get_bin = lambda x, n: format(x, 'b').zfill(n)

def generate_table(type):
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
        elif type==5:
            x.append(int(not(reduce(lambda x, y: x | y, x))))
        elif type==6:
            x.append(reduce(lambda x, y: x ^ y, x))        
        truth_table.append(x)
    return truth_table, inps, weights

ch=int(input("6. XOR\nEnter choice..."))
truth_table,inps,weights=generate_table(ch)
print("Truth Table: "+ str(truth_table))
if ch==6:
    weights = [1,-1]
    weights1 = [1,1]
    for i in truth_table:
        x = i[0]*weights[0] + i[1]*weights[1]
        y = i[1]*weights[0] + i[0]*weights[1]
        if x<1:
            x=0
        else:
            x=1
        if y<1:
            y=0
        else:
            y=1
        res=x*weights1[0]+y*weights1[1]
        print("\nCase "+str(i[:-1])+":")
        print("Truth table value: "+str(i[-1]))
        if res>0:
            print("Calculated value: 1")
        else:
            print("Calculated value: 0")