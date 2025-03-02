import re

operators = {'+', '-', '*', '/'}
AE = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

def check_operator(item):
    stack = []
    i = 0
    while i < len(item):
        char = item[i]
        
        if char == '(':
            stack.append(char)
            i += 1
        
        elif char == ')':
            # buat ngecek kurung e ada pasangannya ato gak
            if not stack or stack[-1] != '(':
                return False 
            stack.pop() #pop kalo udah ngematch sama yang depan
            i += 1

    #case char: operator   
        elif char in operators:
            #memastikan operator gak jadi belakang ato epan
            if(char != "-"):
                if i == 0 or i == len(item) - 1:
                    return False  
            
            elif (char == "-"):
                if i == len(item) - 1:
                    return False 
            
            #assign untuk check prev char dan setelahnya
            prev_char = item[i - 1]
            next_char = item[i + 1]
            
            # kalo prev charnya dia itu operator atau (, invalid
            if prev_char in operators or prev_char == '(':
                return False 
            
            # kalo after charnya dia itu operator atau (, invalid
            if next_char in operators or next_char == ')':
                return False
            
            i += 1
        
    #case char: number
        else:
            #kalo char minus, skip dan proses angkanya aja
            if char == '-':
                if i + 1 < len(item) and item[i + 1] in AE:
                    i += 1  
                else:
                    return False
            
            #cek char char selanjutnya
            while i < len(item) and (item[i] in AE or item[i] == '.'):
                i += 1
    
    # cek kurung tutup kurung buka balance apa gak
    if stack:
        return False 
    
    return True


def delete_parentheses_recursively(expression):
    #base case
    if '(' not in expression and ')' not in expression:
        return expression
    

    expression_inside = re.findall(r"\([^()]*\)", expression)
    print(expression_inside)

    #for item in expression_inside
    #check using re, if the pattern inside () is as following
    #1. a digit number (can be negative or positive)
    #2. If x and y are a digit number, then so are
    # (i) x + y (if the first symbol in y is not -)
    # (ii) x - y (if the first symbol in y is not -)
    # (iii)) x * y
    # (iv) x / y
    # (v) x**y (our notation for exponentiation)
    # basically it has to be number followed by operator, it cannot be operator that is precedented by another operator or  nothing 
    # exammple of wrong one -> (**4) (3+-4)

    for item in expression_inside:
        if check_operator(item) == False:
            return "False"
            
   
    #if valid, express the inner side as 1 
        # else:
    new_expression = re.sub(r"\([^()]*\)", "1", expression)            
    
    # kalo gak keganti, kan artinya dah habis () nya
    if new_expression == expression:
        return expression
    
    return delete_parentheses_recursively(new_expression)

# tes
expression = input()
result = delete_parentheses_recursively(expression)
print("Operasi awal:", expression)
print("Operasi setelah kena rekursif:", result)

#Last step:
#recheck if there is any unclosed bracket using for loop
#if there is then it is unbalanced
#print check 
if result not in ["False", "True"]:
    if check_operator(result) == True: 
        print("Valid")
    else: 
        print("Invalid")
else: 
    print("Invalid")