DECLARE array:ARRAY[1,10] OF INTEGER 
min <- 0
max <- LEN(array) - 1
target <- USERINPUT

WHILE (min <= max) DO
    mid <- (min + max) / 2

    IF array[mid] = target THEN
        OUTPUT mid
    ELSE IF array[mid] < target THEN
        min <- mid + 1
    ELSE
        max <- mid - 1
    END IF
END WHILE

OUTPUT -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min = 0
max = len(array) 
target = input("input number you want to search")

