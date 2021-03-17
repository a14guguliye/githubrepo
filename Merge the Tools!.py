def merge_the_tools(string,k):
    resultlist=[]

    step=(int(len(string)/k))

    resultdictionary={}

    for i in range(0,len(string),k):
        resultedset=string[i:i+k]

        for j in resultedset:
            resultdictionary[j]='b'

        outputresult=''
        for key, value in resultdictionary.items():
            outputresult+=key

        print(outputresult)
        resultdictionary={}

        
        



merge_the_tools('AABCAAADA',3)
