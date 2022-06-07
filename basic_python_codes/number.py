a=int(input())
if(a&1==0):
    print(a," is even")
else:
    print(a," is odd")
flag=0
for i in range(2,int(a**0.5)+1):
    if(a%i==0):
        flag=1
        break
if(flag==1):
    print(a," is composite")
else:
    print(a," is prime")
if(a%5==0):
    print(a," is  divisible by 5")
else:
    print(a, " is not divisible by 5")
s=0
for i in range(a+1):
    s+=i
print("cumulative sum is:",s)
    
