
nums=[1,2,3,4,5]
pre_pr=[]
def product(nums):
    
    for num in nums:
        if pre_pr:
            pre_pr.append(pre_pr[-1]*num)
            print("hello")
        else:
            pre_pr.append(num)  
            print("hello") 

for x in pre_pr:
   print(x)

