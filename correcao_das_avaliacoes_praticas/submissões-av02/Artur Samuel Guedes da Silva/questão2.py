nums = input().split()
if(len(nums) > 1):
    for i in range (len(nums)):
        nums[i] = float(nums[i])
else:
    nums[0] = float(nums[0])
print(sum(nums))
print(sum(nums)/len(nums))
if(len(nums)%2 != 0):
    print(f'{nums[len(nums)//2]:.1f}')
else:
    print(f'{(nums[len(nums)//2]+nums[((len(nums))//2)+1])/2:.1f}')