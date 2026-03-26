"""class solution():
    def isvalid(self,s : str):
       stack =[]
       for bracket in s:
           if bracket=="{"or bracket=="[" or bracket=="(":
               stack.append(bracket)
           else:
               if len(stack)==0:
                   return False
               ch = stack.pop()
               if((ch =="("and bracket==")")or
                   (ch=="{"and bracket=="}")or
                    (ch=="["and bracket=="]")):
                   continue
               else:
                   return False
       return len(stack)==0
paranthesis = solution()
print(paranthesis.isvalid("[({})]]") )"""

#get minimum in 0(1) using stack
"""class solution():
    def __init__(self):
        self.items =[]
    def push(self,value):
        if len(self.items)==0:
            self.items.append([value,value])
        else :
            mini = min(self.items[-1][1],value)
            self.items.append([value,mini])
    def get_min(self):
        if len(self.items)==0:
            return 0
        return self.items[-1][1]
    def top(self):
        if len(self.items)==0:
            return 0
        return self.items[-1][0]
    def pop(self):
        if len(self.items)==0:
            return 0
        self.items.pop(-1)
getmin =solution()
getmin.push(32)
getmin.push(45)
getmin.push(18)
print(getmin.get_min())
print(getmin.top()) """

class solution:
    def monotonicstack(self,nums :list):
        stack =[]
        ans=[-1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            while len(stack)!=0 and stack[-1]<=nums[i]:
                stack.pop()
            if len(stack)!=0:
                ans[i]= stack[-1]
            stack.append(nums[i])
        return ans
obj = solution()
print(obj.monotonicstack([2,5,4,8,7]))    

class solution:
    def monotonicstack(self,nums :list):
        stack =[]
        ans=[-1]*len(nums)
        for i in range(2*len(nums)-1,-1,-1):
            while len(stack)!=0 and stack[-1]<=nums[i%len(nums)]:
                stack.pop()
            if i <len(nums):    
               if len(stack)!=0:
                  ans[i]= stack[-1]
            stack.append(nums[i%len(nums)])
        return ans
obj = solution()
print(obj.monotonicstack([2,5,4,8,7]))

#asteroid colision
class solution:
    def asteroid(self,nums:list):
        stack =[]
        for i in range(0,len(nums)):
            if nums[i]>0:
                stack.append(nums[i])
            if nums[i]<0:  
                while len(stack)!=0 and abs(nums[i])<stack[-1]:
                    stack.pop()
                if len(stack)!=0 and abs(nums[i])==stack[-1]:
                    stack.pop()        
                elif len(stack)==0 or stack[-1]<0:
                    stack.append(nums[i])
        return stack  
obj = solution()
print(obj.asteroid([2,5,8,-6,9,-8,7]))              


               
                   