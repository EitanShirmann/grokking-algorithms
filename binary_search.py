arr = range(1000000000)
num = 656

def search(arr, num):
    low = 0
    high = len(arr)-1

    while low<=high:

        mid = (high+low)//2
        guess = arr[mid]
        print(guess)

        if guess==num:
            return guess

        elif guess<num:
            low = mid+1
               
        else:
            high = mid-1


print("The number was ", search(arr, num))