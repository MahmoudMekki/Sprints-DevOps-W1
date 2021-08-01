def find(str,char):
    rslt = list()
    for i,v in enumerate(str):
        if v == char:
            rslt.append(i)
        else:
            continue
    return rslt

str = input("Enter the word :")
char = input("Enter The character:")
print(find(str,char))