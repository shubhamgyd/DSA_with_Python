x = int(input("Enter the number: "))
sum = 0
while x > 0:
  x = x//10
  sum += 1
print("Count of Digits is ", sum)