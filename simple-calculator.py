##THE GREAT CALCULATOR MY GLORIOUS KING OF PRACTICE PROGRAMMSS
##Once again ik how to document but no I can't expose it this soon in the first code
##Uhh I guess the logics are fine if you find any flaws please mention

##getting inputs and using while case because I know how to

while True:
    try:
        #getting inputs
        x = float(input("Enter The Number:"))
        print(f"{x}")
        y = float(input("Enter The Number:"))
        print(f"{y}")
        #setting up operations
        opp = input("Choose the operation: + - x /: ")
        if opp not in ["+", "-", "x", "/"]:
            print("Don't be dumb pwease")
            continue
        if x < 0 or y < 0:
            print("ik you're negative but please don't show it here -_-")
            continue
        if opp == "/" and y == 0:
            print("0 for divider ehhh comeon lil one that's dumb -_-")
            continue
        break
    except ValueError:
        print("THAT AINT EVEN A NUMBER MF ;)")


#printing according to desired opted one

if opp == "+":
    add = x + y
    print(f"The sum is: {add}")

elif opp == "-":
    sub = x - y
    print(f"The difference is: {sub}")

elif opp == "x":
    mult = x*y
    print(f"The product is: {mult}")

else:
    div = x/y
    print(f"The quotient is: {div}")