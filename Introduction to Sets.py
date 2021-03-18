def average(array):
    #N=int(input())

    inputset=array
    outputset=set()
    i=0
    for val in inputset:
        outputset.add(float(val))
        i=i+1

    return (round(sum((outputset))/len(outputset),3))



if __name__ == '__main__':
