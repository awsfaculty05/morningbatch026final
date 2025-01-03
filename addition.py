def add(a,b):
    mysum=a+b
    print (mysum)
    return mysum

if __name__=="__main__":
    x = input('Enter first number: ')
    y = input('Enter second number: ')
    print(type(x))
    z = add(x, y)
    print ('Sum of x&y is:',z)
