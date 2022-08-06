def compare(string1: str, string2: str):
    while(len(string1) != 0 and len(string2) != 0):
        revStr1 = ""
        revStr2 = ""
        
        if (string1[0] < string2[0]):
            string1 = string1.removeprefix(string1[0])
        elif (string1[0] > string2[0]):
            string2 = string2.removeprefix(string2[0])
        else:
            string1 = string1.removeprefix(string1[0])
            string2 = string2.removeprefix(string2[0])

        if (len(string1) == 0 or len(string2) == 0):
            break

        for i in range(len(string1) - 1, -1, -1):
            revStr1 += string1[i]
        for i in range(len(string2) - 1, -1, -1):
            revStr2 += string2[i]

        string1 = revStr1
        string2 = revStr2

    if (len(string1) == 0 and
        len(string2) == 0):
        print("Both strings are empty!")
        return

    print(string1 if (len(string1) != 0) else string2)

compare("amin", "nima")
        

        