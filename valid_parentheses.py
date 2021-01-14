class Solution:
    close_to_open_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if c in '({[':
                stack.append(c)
            elif c in ')}]':
                open_bracket = self.close_to_open_map[c]
                if not stack or stack.pop() != open_bracket:
                    return False

        return not stack
