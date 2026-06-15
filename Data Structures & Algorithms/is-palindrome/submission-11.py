class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)

        forward = 0
        backward = length-1

        while forward < backward:
            while s[forward].isalnum() == False and forward < backward: 
                forward = forward + 1
            
            while s[backward].isalnum() == False and forward < backward: 
                backward = backward -1
            
            if s[forward].lower() != s[backward].lower(): 
                return False

            forward = forward + 1
            backward = backward -1 

        return True


        