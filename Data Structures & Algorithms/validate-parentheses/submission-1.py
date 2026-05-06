class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            match char:
                case '(':
                    stack.append('(')
                case ')':
                    if not stack or stack.pop() != '(':
                        return False
                case '{':
                    stack.append('{')
                case '}':
                    if not stack or stack.pop() != '{':
                        return False
                case '[':
                    stack.append('[')
                case ']':
                    if not stack or stack.pop() != '[':
                        return False
                case default:
                    raise Exception("unknown character")
        return len(stack) == 0