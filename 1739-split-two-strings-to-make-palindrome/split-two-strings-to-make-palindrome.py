class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        def makes_palindrome(prefix: str, suffix: str) -> bool:
            """Determine if prefix or suffix
            # when do we know if we used the full length? len(prefix[:l] + suffix[r:]) == len(res)
            # an l==0 means we did not include prefix. an r == len(suffix) - 1 means we did not include suffix.
            """
            l, r = 0, len(suffix) - 1
            # keep going until inequality or intersection
            # r >= l intersection: we want l and r to be at first idx of inequality for next steps
            while r >= l and prefix[l] == suffix[r]:
                l += 1
                r -= 1
            # try proceed suffix until length and return true if palindrome
            if is_palindrome(prefix[:l] + suffix[l:]):
                return True
            # try proceed prefix until length and return true if palindrome
            if is_palindrome(prefix[:r+1] + suffix[r+1:]):
                return True
            return False

        return makes_palindrome(a,b) or makes_palindrome(b,a)
        