class Solution:
    def isValid(self, s: str) -> bool:
        tmp_bool = False
        if s == "":
            return True
        if len(s)== 1:
            return tmp_bool    
        tmp_stack = []
        match_parantheses = {")":"(", "}":"{","]":"["} # dict to match closing bracket to opening bracket
        for char in s:
            if char in match_parantheses.values(): # if it is opening bracket push it, easier than to do with IFs
                tmp_stack.append(char)
            else:
                if len(tmp_stack) == 0: #check if we have only closing bracket, stack empty, not valid
                    return False
                if tmp_stack[-1] != match_parantheses[char]: # check if top of stack has matching closing bracket
                    return False    
                tmp_stack.pop()    
        if len(tmp_stack) == 0:
            return True
        return tmp_bool   
 