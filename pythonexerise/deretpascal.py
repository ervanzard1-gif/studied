n=5
baris=[1]
for i in range(n):
    print(' '*(n-i),*baris)
    barisbaru=[1]
    for j in range(len(baris)-1):
        barisbaru.append(baris[j]+baris[j+1])

    barisbaru.append(1)
    baris=barisbaru