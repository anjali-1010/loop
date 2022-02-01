n=int(input("enter a  number"))
s=0
i=1
while i<n:
    if n%i==0:
        s=s+i
    i=i+1
if n==s:
    print(n,"number is perfect number")
else:
    print(n,"number is not perfect number")