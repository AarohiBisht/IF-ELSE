# Write a python program to check whether a number is divisible by 5 and 11 or not.

n=int(input("enter the number "))
if n%5==0 and n%11==0:
    print("number is divisible by 5 and 11 both")
elif n%5==0:
    print("divisible by 5")
elif n%11==0:
    print("divisible by 11")
else:
    print("not divisible by both")
    