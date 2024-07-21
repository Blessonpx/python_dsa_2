def method1_first_repeating_element(arr, n):
  for i in range(n):
    for j in range(i + 1, n):
      if arr[i] == arr[j]:
        return arr[i]

def method2_first_repeating_element(arr, n):
  myset = dict()
  min=-1
  for i in range(n-1,-1,-1):
    if arr[i] in myset:
      min = arr[i]
    else:
      myset[arr[i]]=1
  return min
    


arr = [10, 5, 3, 4, 3, 5, 6]
n = len(arr)
print("First Repeating Element:", method1_first_repeating_element(arr, n))
print("First Repeating Element:", method2_first_repeating_element(arr, n))
