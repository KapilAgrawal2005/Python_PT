# find the number of digit that are occuring more than one time
a = str(input("Enter the data : "))
def counting(a):
  op = []
  for i in range (len(a)):
    for j in range(i+1,len(a)):
      if(a[i] == a[j]):
        op.append(a[i])
  print(len(op))
counting(a)