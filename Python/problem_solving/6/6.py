def create_list(start,len):
    nums = []
    for i in range(len):
        nums.append(start+i)
    return nums


start,len = input("Enter your start and len:\n").split()

nums = create_list(int(start),int(len))
print (nums)