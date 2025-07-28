string= input("enter a word  ")
char= input("enter a character  ")
i=0
count=0
while(i<len(string)):
    if(string[i] == char):
        count+=1
    i+=1
print(f"The total number of times {char} has occured in {string} is {count}")

