# power of four
n = int(input("Enter the number :"))
def power(n):
  for i in range(0, n):
    if n != i**4:
      continue
    else:
      return True
    return False
power(n)