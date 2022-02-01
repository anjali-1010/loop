user=int(input("enter a haow many student"))
i=1
s=0
c=0
while i<=user:
    user2=int(input("enter a student number"))
    s=s+user2
    c=c+1
    i=i+1
avg=s/c
print(avg)
if avg%5==0:
    print("divided")
else:
    print("not divided")
