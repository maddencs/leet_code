class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return s

        if len(s) == 1:
            return s

        if numRows == 1:
            return s

        converted = ''
        row = 0
        i = 0
        while row < numRows:
            converted += s[i]
            if row != 0 and row != numRows - 1:
                zig_idx = i + 2 * numRows - 2 - 2 * row
                if zig_idx < len(s):
                    converted += s[zig_idx]

            i += 2 * numRows - 2
            if i >= len(s):
                row += 1
                i = row

            if row >= len(s):
                break

        return converted
