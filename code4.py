i = 0
while(i<5):
    j = 0
    while(j<5): #loop2
        if (j > 3): 
            break 
        else:
            print("*",end=" "), 
        j = j + 1
    print('')
    i = i + 1