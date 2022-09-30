num1 = int(input('ingresa el num1\n'))
num2 = int(input('ingresa el num2\n'))

total = 0

while (num1 >= 1):
    if (num1 % 2 != 0):
        total = total + num2
    print(str(num1) + "\t" +  str(num2))
  
      
    num1 = num1 / 2
    num1 = int(num1)
    num2 = num2 * 2
    num2 = int(num2)

print("\nTotal: " + str(total))