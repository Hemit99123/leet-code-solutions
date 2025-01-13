divide = True
n = int(input("Convert:"))
binary = []

while (divide):
  quotient = n // 2
  remainder = n % 2

  if (quotient == 0):
    divide = False
  else:
    binary.append(remainder)
    n = quotient

binary.reverse()
