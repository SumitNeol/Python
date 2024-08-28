def rev(n):
    s=0
    r=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    return s
a=int(input("Enter a no: "))
v=rev(a)
if(v==a):
    print('pal')
else:
    print('not a Pal')

        
