List=[]
nums = int(input("enter the number of words:"))
for i in range(nums):
    word=input("enter the word:")
    List.append(word)
print(List)    
myList.sort()
print('List in Ascending Order: ', myList)

myList.sort(reverse=True)
print('List in Descending Order: ', myList)
