n=float(input("Enter the first number: "))
m=float(input("Enter the second number: "))
r=input("Enter the operation: ")
if  r=="+":
    result=n+m
elif r=="-":
    result=n-m
elif r=="*":
    result=n*m
elif r=="/":
    if m==0:
        print("Zero division error")
    else:
     result=n/m
else:
    print("Please enter valid data")
print(n ,r, m,"=",result)
