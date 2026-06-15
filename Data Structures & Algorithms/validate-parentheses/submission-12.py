class Solution:
    def isValid(self, s: str) -> bool:
        
        list = [s[0]]

        for x in s[1:]: 
            if (x == '(' or x == '{' or x == '['):
                list.append(x)
            else: 
                if (x == ')'):
                    reverse = '('
                elif (x == '}'):
                    reverse = '{'
                else:
                    reverse = '['

                if len(list) < 1:
                    return False

                last = list.pop()
            
                if (last != reverse):
                    return False


        return len(list) == 0