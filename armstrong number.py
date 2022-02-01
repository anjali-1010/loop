n=int(input("enter a number"))
i=n
s=0
while i>0:
    d=i%10
    s=s+d**3
    i=i//10
if n==s:
    print("number is armstrong")
else:
    print("not armstrong number")
    
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
