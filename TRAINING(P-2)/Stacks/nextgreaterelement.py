
def nextLargerElement(arr, n):
    stack = []
    l = [-1] * n
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            l[i] = stack[-1]
        stack.append(arr[i])
    return l
arr=[10,20,30,10,50]
n=len(arr)
print(nextLargerElement(arr,n))