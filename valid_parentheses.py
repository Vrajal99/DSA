# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


def isValid( s: str) -> bool:
    map_={"{":"}","(":")","[":"]"}
    stack=[]
    
    for i in s:
        if i in map_:
            stack.append(i)
        else:  
            if not stack:  # Stack is empty
                return False
            if map_[stack[-1]] != i: 
                return False
            stack.pop()
    return len(stack)==0

s = "()[]{}" #True
# s = "(]" #False
print(isValid(s))

