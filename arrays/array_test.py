#a = 5
#print(a)

#b = [5,7,56,-3,0,29]
#print(b)

#for i in b:
#    print(i*i)

c = [*range(2, 100)]
# c.remove(1999998)
# print (c)

# length

# test = 10
# while (test > 0):
# if (test > 0):
#    test = test - 2
#    print(test)

result = []
while (len(c) > 0):
#    if (c[0] > 49000 and c[0] < 50000):
    result.append(c[0])

    composites = []
    for i in c:
        if (i % c[0] == 0):
            composites.append(i)

    for i in composites:
        c.remove(i)

print(result)
print(c)

a = [3,4,5,77]

# print(a[4])

# index = 0
# for i in a:
#     print(a[index])
#     index = index + 1

def contains(element, arr):
    for i in arr:
        if (i == element):
            return True
    
    return False


twins = []
not_twins = []
index = 0
for i in result:
    if (index < len(result)-1 and result[index + 1] - result[index] == 2):
        if (contains(result[index], twins) == False):
            twins.append(result[index])
        if (contains(result[index + 1], twins) == False):
            twins.append(result[index + 1])

    index = index + 1

for x in result:
    if (contains(x, twins) == False):
        not_twins.append(x)

print(twins)
print(not_twins)