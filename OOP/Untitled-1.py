x = int(input("Enter number of times to be iterated:"))
for i in range (x):
    print (i * "hehe")

end = "meow"
if x == 10:
    print(end)

else:
    print(f"no {end}")

if end == "meow":
    print("\n woof")

while end == "meow":
    y = int(input("enter how many types you wanna iterate:"))
    for i in range (y):
        print("this is enough. ")
        end = "woof"