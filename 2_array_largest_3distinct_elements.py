def getlargest3elements(arr):
  if len(arr)<3:
    print("Invalid Response")
    return 

  first=second=third=float('-inf')
  for i in range(len(arr)):
    if arr[i]>first:
      third=second
      second=first
      first=arr[i]
    elif arr[i]>second and arr[i]!=first:
      third=second
      second=first
    elif arr[i]>third and arr[i]!=second and arr[i]!=first:
      third=arr[i]
  print("Largest 3 elements are: ",first,second,third)
  return

arr = [12, 13, 1, 10, 34, 11, 34]
getlargest3elements(arr)