def mx(*nums):
    mm=nums[0]
    for i in nums:
        if i>mm: mm=i
    return mm

print(mx(4,2,8,4,5))
print(mx(3))
print(mx(3,5,10,6,15,20,12))

        
