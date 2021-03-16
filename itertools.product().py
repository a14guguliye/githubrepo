A = list(map(int, input().split()))
B = list(map(int, input().split()))


outputlist=[]

k=0
for i in range(len(A)):
    for j in range(len(B)):
        outputlist.append((int(A[i]),int(B[j]),))
        k=k+1

print(*outputlist)
