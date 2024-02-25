def score_of_parentheses(s):
    stack = []
    current_score = 0

    for char in s:
        if char == '(':
            stack.append(current_score)
            current_score = 0
        else:  # char == ')'
            prev_score = stack.pop()
            completed_score = current_score   

            # Custom weighting logic
            if completed_score == 0:  # Base case "()"
                weight = 3       
            else:                # Nested case "(...)"
                weight = 5      

            current_score = prev_score + weight 

    return current_score


print(score_of_parentheses('(())'))