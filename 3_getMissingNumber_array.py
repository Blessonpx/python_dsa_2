def method_1_getMissingNumber(n,arr):
    sum=n*(n+1)/2
    sum_2=0
    for i in range(len(arr)):
        sum_2=sum_2+arr[i]
    return sum-sum_2

def method_2_getMissingNumber(n,arr):
    hash=[0]*(n+1)
    for i in range(len(arr)):
        hash[i]=+1
    for i in range(len(hash)):
        if hash[i]==0:
            return i
    return -1

def method_3_getMissingNumber(n,arr):
    xor1 = 0
    xor2 = 0
    # XOR all array elements
    for num in arr:
        xor2 ^= num
    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor1 ^= i
    # Missing number is the XOR of xor1 and xor2
    return xor1 ^ xor2

# First find XOR all numbers in the range [1, N]
# Then XOR all elements of the array with the XOR(1, N).
# The result will be the missing number.

arr = [1,2,3,5]
n=5
print(method_1_getMissingNumber(n,arr))
print(method_2_getMissingNumber(n,arr))
print(method_3_getMissingNumber(n,arr))
