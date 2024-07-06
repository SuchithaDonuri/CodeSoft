import random
print("Welcome to password generator: ")
letter=int(input("How many letters would you like to have in your password?\n"))
symbol=int(input("How many symbols would you like?\n"))
number=int(input("How many numbers would you like?\n"))
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','^','&','*']
numbers=['0','1','2','3','4','5','6','7','8','9']
password=""
for i in range(letter):
    password+=random.choice(letters)
#print(password)
for i in range(symbol):
    password+=random.choice(symbols)
#print(password)
for i in range(number):
    password+=random.choice(numbers)
#print(password)
li=list(password)
random.shuffle(li)
ps=""
for i in li:
    ps+=i
print(ps)