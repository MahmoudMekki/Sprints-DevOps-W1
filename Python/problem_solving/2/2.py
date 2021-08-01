def word(str):
    vowels = ('a','e','i','o','u')
    for i,v in enumerate(str):
        if v.lower() in vowels:
            str = str.replace(v,"")
        else:
            continue
    return str


str = input("Enter your Word : ")
print(word(str))