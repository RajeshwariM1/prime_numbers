n=int(input("enter a number : "))

if n>0:
    if n%2==0:
        print(n," is even and positive number ")
    else:
        print(n,"is positive and odd number ")
else:
    if n%2==0:
        print(n,"is non-positive even number ")
    else:
        print(n,"is non-positive odd number ")


