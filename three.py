def binarysearch(start,end,num,x):
    if start>=1:
     
       mid=(start+end)//2
       if x<num[mid] :
           return binarysearch(start,mid-1,num,x)
       elif x>num[mid]:
           return binarysearch(mid+1,end,num,x)
       elif x==num[mid]:
           return mid
       else:
           return -1 
       
num = input('Enter the sorted numbers: ')
num = num.split()
num = [int(y) for y in num]
x = int(input('The number to be found: '))
n=len(num)

pos = binarysearch(0,n,num,x)
if pos < 0:
    print("not found")
else:
    print("Found at",pos)