ex='z'
while ex!='x':
    num1=int(input("Enter the first number: "))
    con='y'
    while con=='y':
        op=input("+\n-\n*\n/\nPick an operation: ")
        num2=int(input("Enter next number: "))
        if op=='+':
            result=num1+num2
        elif op=='-':
            result=num1-num2
        elif op=='*':
            result=num1*num2
        elif op=='/':
            result=num1/num2
        else:
            print("Enter a valid operator")
            break
        print(result)
        con=input(f"Enter 'y' to continue calculation with {result} or 'n' to start new camculation or 'x' to exit: ")
        if con=='y':
            num1=result
        elif con=='x':
            ex='x'