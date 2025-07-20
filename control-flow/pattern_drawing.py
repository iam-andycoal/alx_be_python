number = int(input("Enter the size of the pattern: "))

row = 0
while row < number:
  for i in range(number):
    print("*", end="")
    print()
    row += 1
