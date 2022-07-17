"""
Remove duplicate elements in a string
"""


def removeDuplicatesInString( str_vals : str, k : int ) -> str:
    stack_chars = []
    
    for c in str_vals:
        if len(stack_chars) > 0 and stack_chars[-1][0] == c:
            val = stack_chars[-1][1]
            stack_chars[-1] = (c, val + 1)
        else:
            stack_chars.append((c, 1))

        if stack_chars[-1][1] == k:
            stack_chars.pop()
    
    result_string = ""
    for c, count in stack_chars:
        result_string += (c * count)

    return result_string