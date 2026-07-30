class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        for char in s:
            if char in pairs:
                if not stack:
                    return False
                if stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0