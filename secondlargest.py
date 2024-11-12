# find the second largest element in the list
a = [3,8,1,10,5]
def secondLargest(a):
  for i in range(len(a)):
    for j in range(len(a)):
      if a[i] > a[j]:
        a[j],a[i] = a[i],a[j]
  print(a[1])

secondLargest(a)