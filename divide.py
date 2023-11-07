def divide(x,y):
    result=0
    while (x>=y):
        x-=y
        result+=1
        
    return result
divident=int(input("enter a divident:"))
divisor=int(input("enter a divisor:"))
result= divide(divident,divisor)
print(divident,"divided by",divisor,"is",result)