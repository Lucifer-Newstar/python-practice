#get acc no and assign amount
acc_no = input("Enter your account number:")
if len(acc_no)<15 or len(acc_no)>15:
    print ("Account number is wrong")
    acc_no = input("Enter your account number:")
initial_amount = 500
#assign actions
act = input("Welcome to the bank choose your action: 1. Withdrawal, 2. Check Balance, 3. Exit:")

#using while function where exit isn't chosen. code logic is shit ik bear with it I'm js a kid ``uwu``
while not act == "3":
    if act == "2":
        print(f"The balance amount in your account XXXX-XXXX-{acc_no[-4:]} is : $ {initial_amount} ")
        print("Thank you for using our bank!")
        act = input("Welcome to the bank choose your action: 1. Withdrawal, 2. Check Balance, 3. Exit:")
    elif act == "1":
        wamt = int(input("Enter the amount to be withdrawn:"))
        if wamt > initial_amount:
            print(f"Insufficient bank balance! Remaining balance: {initial_amount}")
            act = input("Welcome to the bank choose your action: 1. Withdrawal, 2. Check Balance, 3. Exit:")
        else:
            ramt = initial_amount - wamt
            initial_amount = ramt
            print(f"The amount {wamt} is withdrawn. The remaining balance is : {initial_amount}")
            act = input("Do you wish to continue? Choose your action: 1. Withdrawal, 2. Check Balance, 3. Exit:")
    else:
        print("Choose from the actions")
        act = input("Welcome to the bank choose your action: 1. Withdrawal, 2. Check Balance, 3. Exit:")


print ("Thank you!")