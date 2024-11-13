# find the nearest greater than b
from itertools import permutations
a,b = map(int,input("Enter two numbers : ").split())
def nearLarge(a,b):
  x = 0
  number = str(a)
  per = permutations(number)
  perlist = [int(''.join(p)) for p in per]
  perlist.sort()
  print(perlist)
  for i in perlist:
    if i > b:
      x = i
      break
  if x !=0:
    print(x)
  else:
    print(-1)

nearLarge(a,b)