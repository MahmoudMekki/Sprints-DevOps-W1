def divide(str):
    div1 =""
    div2 =""
    if len(str)%2 ==0:
        mid = int(len(str)/2)
        div1 = str[:mid]
        div2 = str[mid:]
        return div1,div2
    else:
        mid =int((len(str)/2))+1
        div1 = str[:mid]
        div2 = str[mid:]
        return div1,div2

word = input("Enter your Word: \n")
div1,div2 = divide(word)
print(div1,div2)

