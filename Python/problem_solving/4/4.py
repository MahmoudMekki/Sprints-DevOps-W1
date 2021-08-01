def dublicatedr_removal(lst):
    dict ={}
    for v in lst:
        dict[v]=v
    return dict

lst_str = input("Enter your numbers:").split()
lst_num =[]
for i in range(len(lst_str)):
    lst_num.append(int(lst_str[i]))

rslt = dublicatedr_removal(lst_num)
print(rslt.values())