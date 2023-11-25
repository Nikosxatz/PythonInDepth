def minmax(*nums):
    mn=mx=nums[0]
    for i in nums:
        if i>mx:
            mx=i
        elif i<mn:
            mn=i
    return mn,mx

print(minmax(4,2,8,4,5))
print(minmax(3))
print(minmax(3,5,10,6,15,20,12))

        
