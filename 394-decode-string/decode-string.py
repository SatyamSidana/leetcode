class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i!="]":
                stack.append(i)
            else:
                curr_s=""
                while stack[-1]!="[":
                    curr_s=stack.pop()+curr_s
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                curr_s=(int(num))*curr_s
                stack.append(curr_s)
        return "".join(stack)