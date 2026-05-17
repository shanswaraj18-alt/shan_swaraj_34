class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.diameter = None
one = node(1)
two = node(2)
three = node(3)
four = node(4)
five = node(5)
six = node(6)
eight = node(8)
nine =node(9)
ten = node(10)
three.left = two
three. right = nine
eight.left = one
eight.right = six
four.left = eight
four.right= ten
five.left=three
five.right=four
"""#preorder traversal
def pre_order_traversal(node):
    if node== None:
        return
    print(node.value,end='')
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
pre_order_traversal(five)
#inorder traversal
def pre_order_traversal(node):
    if node== None:
        return
    pre_order_traversal(node.left)
    print(node.value,end=' ')
    pre_order_traversal(node.right)
pre_order_traversal(five)
#postorder traversal
def pre_order_traversal(node):
    if node== None:
        return
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    print(node.value,end=' ')
    
pre_order_traversal(five)
#level_order_traversal
from collections import deque
def level_order(node):
       result = []
       queue =deque([])
       queue.append(node)
       while len(queue)!=0:
           e = queue.popleft()
           result.append(e.value)
           if e.left is not None:
              queue.append(e.left)
           if e.right is not None:
              queue.append(e.right)
       return result 
print(level_order(five))
#height of binartree in recursive
def solve(node):
    if node == None:
        return 0
    node_left = solve(node.left)
    node_right = solve(node.right)
    return 1+max(node_left,node_right)
print(solve(five))   
#height of binarytree in iterative
def level_order(node):
    queue = deque([])
    result = []
    height =0 
    queue.append(node)
    while len(queue)!=0:
        level_size =len(queue)
        height+=1
        for _ in range(level_size):
            e =queue.popleft()
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
    return height
print(level_order(five))    
#diameter in binary tree
diameter = 0
def solve(node):
    global diameter
    if node == None:
        return 0
    height_left = solve(node.left)
    height_right = solve(node.right)
    diameter = max(diameter,height_left+height_right)
    return 1+max(height_left,height_right)
solve(five)
print(diameter)
#balancing of binary tree
def solve(node):
    if node == None:
        return 0
    height_left = solve(node.left)
    if height_left ==-1:
        return -1
    height_right = solve(node.right)
    if height_right==-1:
        return -1
    if abs(height_left-height_right)>1:
        return -1
    return 1+max(height_left,height_right)
x=solve(five)
if x==-1:
    print("not balanced binary tree")
print(" balanced")    """

#max path sum
maxi = float('-inf')
def solve(node):
    global maxi
    if node ==None:
        return 0
    sum_left = solve(node.left)
    if sum_left <0:
        sum_left=0
    sum_right = solve(node.right)
    if sum_right<0:
        sum_right=0
    maxi = max(maxi,sum_left+sum_right+node.value)    
    return node.value + max(sum_left,sum_right)
print(solve(five))
#top view in a binary tree
from collections import deque
def topview(node):
    if not node :
        return None
    ans =[]
    queu = deque()
    result = {}
    queu.append((node,0))
    while queu :
        e,line = queu.popleft()
        if line not in result:
            result[line]=e.value
        if e.left:
            queu.append((e.left,line-1))
        if e.right:
            queu.append((e.right,line+1))
    for value in sorted(result.items()):
        ans.append(value[1]) 
    return ans           
print(topview(five))

#bottom view in a binary tree
from collections import deque
def topview(node):
    if not node :
        return None
    ans =[]
    queu = deque()
    result = {}
    queu.append((node,0))
    while queu :
        e,line = queu.popleft()
        result[line]=e.value
        if e.left:
            queu.append((e.left,line-1))
        if e.right:
            queu.append((e.right,line+1))
    for value in sorted(result.items()):
        ans.append(value[1]) 
    return ans           
print(topview(five))

#right view of a binary tree
from collections import deque
def rightview(node):
    if node==None:
        return
    queue = deque()
    result=[]
    queue.append(node)
    while len(queue)!=0:
        level_size=len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i==level_size-1:
                result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
print(rightview(five))                

            


    
            

