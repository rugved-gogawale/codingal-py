dictionaryfortesting= {"codingal": 2, "is" : 2, "best":2, "for":1, "coding": 4}
print("The original dictionary : " + str(dictionaryfortesting))
k = 2 
res=0
for key in dictionaryfortesting:
    if dictionaryfortesting[key]==k:
        res+=1
print("Frequency of k is : "+ str(res))