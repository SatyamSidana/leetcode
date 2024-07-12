class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a=0
        for i in word:
            a+=1
            if i==ch:
                break
        b=word[:a]
        if a==len(word) and word[-1]!=ch:
            return word
        return b[::-1]+word[a:len(word)]
            
