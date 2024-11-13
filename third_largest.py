# find the third largest element in the list
a = [5,9,2,7,3,8,6]
def secondLargest(a):
  for i in range(len(a)):
    for j in range(len(a)):
      if a[i] > a[j]:
        a[j],a[i] = a[i],a[j]
  print(a[2])

secondLargest(a)