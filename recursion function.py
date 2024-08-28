#recursion functon for printing a number
def print1(x,n):
    if(x>n):
        return 
    else:
        print(x)
        return print1(x+1,n)

#recursion function for factorial
def fact(n):
    if(n<2):
        return 1
    else:
        return n*fact(n-1)

# recursion for finding power of a number
def pow(n,p):
    if p<1:
        return 1
    else:
        return n*pow(n,p-1)

x=1
n=int(input("Enter a number: "))
print1(x,n)
print(fact(n))
print(pow(3,4))
