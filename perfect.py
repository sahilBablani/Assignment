def Perfect(n):
    sum=1
    i=2
    while i*i<=n:
        if n%i==0:
            sum=sum + i + n/i
        i +=1
        return(True if sum==n and n!=1 else False)
print("Below are all perfect numbers")
n=2
for n in range(1000):
    if Perfect(n):
        print(n)
        
            