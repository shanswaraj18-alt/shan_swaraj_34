def convert2decimal(x:str):
    decimal_num = 0
    power =0 
    index = len(x)-1
    while index>=0:
        num = int(x[index])*(2**power)
        decimal_num += num
        index -= 1
        power += 1
    return decimal_num
#print(convert2decimal("10101")) 
#def convert2binary(x:int):
    result = " "
    while x >0 :
        if x%2==1:
            result+="1"
        else :
            result+="0"
        x = x//2
    result = result[::-1]
    return result
start = 7
goal = 9
result1 = start^goal
count =0
for i in range(0,32):
    if result1 & (1<<i) != 0:
        count+=1
#print("number to be flip to convert start into goal:",count) 

arr = [1,2,3,3,2,4,1]
result = 0
for i in arr:
    result = result^i
print("single no. prsnt in array:",result)        