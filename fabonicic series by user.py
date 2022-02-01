from calendar import c


n=int(input("enter a number"))
first=0
second=1
while first<n:
    print(first)
    c=first
    first=second
    second=c+second