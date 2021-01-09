class Solution:
    def reverse(self, x: int) -> int:
        rev = str(x)[::-1]
        if rev[0] == '0' and rev != '0':
            rev = rev[1:]
        if rev[len(rev)-1] == '-':
            rev = '-' + rev[:len(rev)-1]
        if int(rev) >= 2**31-1 or int(rev) <= -2**31:
            return 0
        return int(rev)
            