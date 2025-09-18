'''n=int(input())
for i in range (1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''
n=int(input())
isprime=True
for i in range (2,int(n/2)+1):
    if(n%i==0):
       isprime=False 
    
if isprime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")