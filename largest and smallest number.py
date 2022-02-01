# from re import I


n=int(input("enter a number"))
i=0
largest=0
smallest=0
while i<n:
    n2=int(input("enter a number"))
    if largest == 0 or n >= largest: largest = n
    else: largest= largest
    if smallest == 0 or n <= smallest: smallest = n
    else: smallest= smallest

print("Maximum is", largest)
print("Minimum is", smallest)

#     if m>i:
#         m=n
#     elif s<i:j
#         s=i
#     i=i+1
#     print(m,s)
# largest = 0
# smallest = 0
# while True:
#     num = input("Enter a number: ")
#     if num =="done": break
#     try:
#         fnum = float(num)
#     except:
#         print("Invalid input")
#         continue

#     if largest == 0 or num >= largest: largest = num
#     else: largest= largest
#     if smallest == 0 or num <= smallest: smallest = num
#     else: smallest= smallest

# print("Maximum is", largest)
# print("Minimum is", smallest)
