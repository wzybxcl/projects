def MID(str, y, z):
    startpos = y
    result = str[startpos:startpos + z]
    return result

def LENGTH(str):
    return len(str)

def IterativeVowels(Str):
    Total = 0
    LengthString = len(Str)
    for i in range(0, LengthString-1):
        FirstCharacter = MID(Str, 0, 1)
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter =='i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            Total += 1
        Str - MID(Str, 1, len(Str)-1)

    return Total

IterativeVowels('house')
    