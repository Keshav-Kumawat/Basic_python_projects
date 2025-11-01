# we are building the calculator in there 

def calculator():
    # addition of two numbers 
    while True:
        c=input("Choose the options(1,2,3,4):-\n 1.Addition\n 2.subtraction\n 3.multiplication\n 4.division\n")
        if c== '5':
           print("Exiting Calculator!!!!!") 
           break
        
        if c=='1':
            try:
                print("calculating addition------------")
                add1 = int(input(("enter an number:- ")))
                add2 = int(input(("enter an second number:- ")))
                print(add1 + add2)
            except ValueError as e :
                print("value is not correct! Please Enter an integer")  
            except :
                print("other Error occured-----")
        elif c == '2':
            try:
                print("calculating subtraction------------")
                sub1 = int(input(("enter an number")))
                sub2 = int(input(("enter an second number")))
                print(sub1 - sub2)
            except ValueError as e :
                print("value is not correct! Please Enter an integer")  
            except :
                print("other Error occured-----")        
        elif c == '3':
            try:
                print("calculating multiplication------------")
                mul1 = int(input(("enter an number")))
                mul2 = int(input(("enter an second number")))
                print(mul1 * mul2)
            except ValueError as e :
                print("value is not correct! Please Enter an integer")  
            except :
                print("other Error occured-----")

        elif c =='4':
            try:
                print("calculating subtraction------------")
                div1 = int(input(("enter an nominator")))
                div2 = int(input(("enter an denominator")))
                if div2 == 0:
                    print("enter an valid denominator")
                else:        
                 print(div1/div2)
            except ValueError as e :
                print("value is not correct! Please Enter an integer")  
            except :
                print("other Error occured-----")
        else:
            print("Please choose between Given options..............")   

calculator()             


        



