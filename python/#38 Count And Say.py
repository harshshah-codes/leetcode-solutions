class Solution:
    def countAndSay(self, n):
        def helper(s, n): 
            # `s` is the string of the RLE of the previous iteration
            # `n` is the number of times, the RLE has happened
            if n == 1: return s # Base case

            cnt = 0
            res = ''

            for i in range(len(s)): 
                cnt += 1 # Increase the count of current digit
                if (i + 1 < len(s)) and (s[i] == s[i+1]):
                    continue
                if (i + 1 < len(s)) and (s[i] != s[i+1]):
                    res += f"{cnt}{s[i]}"
                    cnt = 0
                else:
                    res += f"{cnt}{s[i]}"

            return helper(res, n-1)

        return helper('1', n) 