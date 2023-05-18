ni = input("Enter input column names: ").split(',')
no = input("Enter output column names: ").split(',')
inp_table = { i : [] for i in ni+no }
n = int(input("Enter number of entries: "))
cols = list(inp_table.keys())
for __ in range(n):
    i = input().split(',')
    for j in range(len(i)):
        inp_table[cols[j]].append(i[j])
check_table = dict.fromkeys(ni)
output_classes = dict.fromkeys(no)
input_classes = dict.fromkeys(ni)
for i in no:
    output_classes[i] = list(set(inp_table[i]))

for i in ni: 
    x = list(set(inp_table[i]))
    input_classes[i] = x
    check_table[i] = dict.fromkeys(x)
    for j in x:
        check_table[i][j] = dict.fromkeys(no)
        for k in no:
            check_table[i][j][k] = {"count": dict.fromkeys(output_classes[k]), "probability":dict.fromkeys(output_classes[k])}
            for l in output_classes[k]:
                c=0
                for m in range(n):
                    if inp_table[k][m] == l and inp_table[i][m] == j:
                        c+=1
                check_table[i][j][k]['count'][l] = c
                check_table[i][j][k]['probability'][l] = c/inp_table[k].count(l)

probabilities = dict.fromkeys(no)
for i in no:
    probabilities[i] = dict.fromkeys(output_classes[i])
    for j in output_classes[i]:
        probabilities[i][j] = inp_table[i].count(j)/n
print("\nOutput table: ",check_table)

test_inp = dict.fromkeys(ni)
x = input("\nEnter test case: ").split(',')
for i in range(len(x)):
    test_inp[ni[i]] = x[i]
print("Testcase:",test_inp)

for i in no:
    probabilities2 = dict.fromkeys(output_classes[i])
    likelihood = dict.fromkeys(output_classes[i])
    lsum = 0
    for j in output_classes[i]:
        probabilities2[j] = 1
        for k in ni:
            probabilities2[j]*=check_table[k][test_inp[k]][i]['probability'][j]
        likelihood[j] = probabilities[i][j]*probabilities2[j]
        lsum += likelihood[j]
    print("\nProbabilities for "+i+": ",probabilities2, "\nLikelihoods for "+i+": ",likelihood, "\nSum of likelihoods for "+i+": ",lsum)
    final_probabilities = dict.fromkeys(output_classes[i])
    for j in output_classes[i]:
        final_probabilities[j] = probabilities2[j]/lsum
    print("Final probabilities: ", final_probabilities)

    print("As probability of " + max(final_probabilities, key=final_probabilities.get) + " is highest, the given record can be classified as: "+ max(final_probabilities, key=final_probabilities.get))

