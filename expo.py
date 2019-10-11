def ex(a, e, m):
    if e == 0:
        return 1
    if e%2 ==1:
        return ex(a, (e-1)/2, m)*a%m
    aux = ex(a, e/2, m)
    return(aux*aux)%m

results = []
for i in [3, 5, 7]:
    for j in range(1,5):
        results.append(ex(j, i, i))
print(results)

