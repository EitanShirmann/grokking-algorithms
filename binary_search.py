import random

length =1000000000
arr = range(length)
num = random.randint(0,length-1)

def search(arr, num):
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = (high+low)//2
        guess = arr[mid]
    
        if guess==num:
            return guess

        elif guess<num:
            low = mid+1
               
        else:
            high = mid-1


print("The number predicted", search(arr, num))
print("The true number was ", search(arr, num))