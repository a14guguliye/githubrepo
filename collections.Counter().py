
numberofShoes=int(input())

shoes=[int(s) for s in (input().split())]


numShoes=int(input())

inputforshoes=[]
keys=[]
values=[]

for i in range(numShoes):
    inputforshoes.append(tuple(int(s) for s in (input().split())))


for i in inputforshoes:
    keys.append(i[0])
    values.append(i[1])


S=0


for k in range(0,len(keys)):
    if(keys[k] in shoes):
        S+=values[k]
        shoes.remove(keys[k])

print(S)

