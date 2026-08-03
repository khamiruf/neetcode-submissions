class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ["+", "*", "-", "/"]

        for t in tokens:
            if t not in operator:
                stack.append(t)
            elif t in operator:
                if not stack:
                    return -1
                else:
                    match t:
                        case '+':
                            op2 = stack.pop()
                            op1 = stack.pop()
                            stack.append(int(op1) + int(op2))
                        case '-':
                            op2 = stack.pop()
                            op1 = stack.pop()
                            stack.append(int(op1) - int(op2))
                        case '*':
                            op2 = stack.pop()
                            op1 = stack.pop()
                            stack.append(int(op1) * int(op2))
                        case '/':
                            op2 = stack.pop()
                            op1 = stack.pop()
                            stack.append(int(op1) / int(op2))
        
        return int(stack[-1])
