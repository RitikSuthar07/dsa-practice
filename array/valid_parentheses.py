class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s :
            s = s.replace('()','')
            s = s.replace('{}','')
            s = s.replace('[]','')
        
        return s == ''
        
        # stack = []

        # for ch in s:
        #     if ch in '({[':
        #         stack.append(ch)
        #     else:
        #         if not stack:
        #             return False

        #         top = stack.pop()

        #         if (ch == ')' and top != '(') or \
        #            (ch == '}' and top != '{') or \
        #            (ch == ']' and top != '['):
        #             return False

        # return len(stack) == 0
        
