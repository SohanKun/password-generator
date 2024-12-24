print("     PASSWORD GENERATOR     ")
import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
symbols="!@#$%^&*()[]{}?\/;:.,"
all=upper+lower+digits+symbols
#taking input of length of passwor required from user
length=int(input("Enter the length of password required : "))
#taking input of no of passwords required
amount=int(input("Enter the no of passwords required : "))
for i in range(amount):
    password="".join(random.sample(all,length))
    print(password)  #pinting the final password as output
print("Thanks for using our password generator")
