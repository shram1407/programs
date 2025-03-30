def s(N):

    sap = 0
    i = 0

    while (sap < N):
        sap = sap + i
        i = i + 1

    if (N == sap):
        return 1
    
    return 0

print(s(3))