class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
    
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32: 
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)


#Line 7 code explination
#Checking the ASCII values between two letters
#if they are the same letter but one is capitlized 
#then we subtract their values and check if they are equal to 32 
#which is the difference between same letters if one is captlized
#if the if statment is met we pop at stack[-1]


#Time Complexity: O(n)
#Space Complexity: O(n)