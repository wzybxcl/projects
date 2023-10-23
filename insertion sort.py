arr = ["Nahida","Ayato","Neuvillette","Furina","Chlorinde","Wriothesly","Ayaka","Fu Xuan","Blade"]

for i in range(1, len(arr)):
    temp = arr[i]
    j = i - 1
    while j >= 0 and temp < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = temp

print("Sorted array:", arr)