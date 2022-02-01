i=0
guess=8
while i<=10:
    user=int(input("enter a number"))
    if user<guess:
        print("small then guess number")
    elif user>guess:
        print("greater then guess number")
    else:
        print("you win")
        break
    i=i+1
