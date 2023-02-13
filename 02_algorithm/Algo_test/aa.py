def bubble_sort(a, N):
    for n in range(N-1, -1, -1):
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

a = [5, 8, 7, 33, 1,2]
N = 6
print(bubble_sort(a, N))