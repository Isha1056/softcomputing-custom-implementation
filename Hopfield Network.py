from random import shuffle
n = int(input("Enter number of input patterns: "))
x = []
for i in range(n):
    x.append(list(map(int, input().split())))

w = [[0 for _ in range(len(x[-1]))] for __ in range(len(x[-1]))]

for i in x:
    for j in range(len(i)):
        for k in range(len(i)):
            w[j][k] += (i[j]*i[k])
            if j == k:
                w[j][k] = 0

print("Final calculated weights: ", w)
ntest = int(input("Enter number of test cases: "))
for i in range(ntest):
    test = list(map(int, input("\n\nEnter test sequence: ").split()))
    order = list(range(len(test)))
    shuffle(order)
    it = 1
    while True:
        test_copy = test.copy()
        print("\nIteration: ", it)
        for i in order:
            print("\nConsider Y =", i+1)
            yin = test[i]
            for j in range(len(test)):
                yin += (test[j] * w[j][i])
            print("Value of Yin:",yin)
            
            if yin > 0:
                yin = 1
            else:
                yin = -1
            print("Yin after applying activation function:",yin)
            test[i] = yin
            print("Therefore, Y =",test)
            
            if test in x:
                print("Y", test, "converges with input vector", x.index(test), ": ", test)
                break
            else:
                print("No convergence")
        if test in x or test == test_copy :
            break
        it+=1
