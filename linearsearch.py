from random import shuffle
Items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
MaxIndex =len(Items)
SearchValue = input("Please enter the value you are searching for")
SearchVal = int(SearchValue)
Index = 0
Found = False

while Found is not True or Index <= MaxIndex:
    if Items[Index] == SearchVal:
        Found = True
        print(f'{SearchVal} is found at position {Index+1}')
        break
    else:
         Index = Index + 1
    if Index > MaxIndex:
        print("Value is not in the list")
        

ARR <- [64, 34, 25, 12, 22, 11, 90]
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