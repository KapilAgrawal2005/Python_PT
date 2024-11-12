# moves zeros to the end
a = [0,1,0,3,12]
def move(a):
  for i in range(len(a)):
    if a[i] == 0:
      a.remove(a[i])
      a.append(0)
  print(a)
move(a)