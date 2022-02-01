from ctypes import c_int16


i=1
s=0
c=0
while i<10:
    c=c+1
    s=s+i
    avg=s/c
    i=i+1
print(avg)
