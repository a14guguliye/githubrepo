N=input()

firstset=(set(list((input().split()))))
N1=input()


secondset=(set(list((input().split()))))

firstsetoriginal=firstset.copy()



for val in firstset.intersection(secondset):
    firstset.discard(val)




for val in secondset.intersection(firstsetoriginal):
    secondset.discard(val)



outputlist=[]

for val in sorted(list(firstset.union(secondset))):
    outputlist.append(int(val))
    

for val in (sorted(outputlist)):
    print(val)
