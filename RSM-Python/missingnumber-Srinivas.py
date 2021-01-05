nums = list(map(int, input().split())) #Input array
nums.sort() #Sort array

for i in range(0,len(nums)-1):
    if((nums[i+1]-nums[i])!=1):
        print(nums[i]+1)
