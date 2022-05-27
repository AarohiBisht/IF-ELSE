# Write a python program to input any character and check whether it is alphabet, digit or special character.

chr=input("enter the character")
if chr>="A" and chr<="Z" or chr>="a" and chr<="z":
    print("alphabet")
# elif chr>=0 and chr<=9:
#     print("it is digit")
elif chr=="#" or chr=="@" or chr=="$" or chr=="&":
    print("it is special character")
else:
    print("digit")