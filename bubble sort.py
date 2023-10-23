arr = [8,2,4,6,1,3,10,9,5,7]
n = len(arr)
for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    if not swapped:
        break

print("Sorted list:", arr)


ARR <- [8,2,4,6,1,3,10,9,5,7]
N <- Length of ARR
FOR I <- 0 TO N - 1
    SWAPPED <- FALSE
    FOR J <- 0 TO N - I - 2
        IF ARR[J] > ARR[J + 1] THEN
            SWAP ARR[J] AND ARR[J + 1]
            SWAPPED <- TRUE
        END IF
    END FOR
    IF NOT SWAPPED THEN
        EXIT LOOP 
    END IF
END FOR
