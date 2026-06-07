#program to provide multiplication tables of a provided number

print("welcome to multiplication tables kindly enter the number of the multiplication table you need!")
num = int(input("Enter the number:"))

for i in range (1,16):
    
    print(f" {num} x {i} = {num * i}")
