# For loop examples
from datatypes import naughty_list

for i in range(10, 20):
    print(i)


for name in naughty_list:
    print(name)

# While loop examples
count = 0
while count < 10:
    print(count)
    count += 1


while True:
    user_input = input("Enter a number: ")
    if user_input == '0':
        print("Goodbye! See you later!")
        break
