# Selection sort - Time complexity O(n^2)

arr = list(range(10))

def biggest(arr):
    big = arr[0]
    for i in arr:
        if i>big:
            big = i

    return big


def selection_sort(arr):
    newarr = []
    for i in range(len(arr)):
        newarr.append(biggest(arr))
        arr.pop()

    return newarr

print(selection_sort(arr))