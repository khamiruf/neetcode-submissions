class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        open_parens = set(paren_map.values())
        stack = []

        for p in s:
            if p in paren_map:
                if not stack: return False
                if stack[-1] == paren_map[p]:
                    stack.pop()
                else:
                    return False
            elif p in open_parens:
                stack.append(p)
        
        return len(stack) == 0

