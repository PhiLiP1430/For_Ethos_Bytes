# Given a string with duplicated characters, 
# write a function that will return a non-duplicated version of the string.

# Input str = "AAA BB CC"
# Output: "A BC"

# Input str = "abcabcabc"
# Output: "abc"

# Input str = "abababababacdef"
# Output: "abcdef"


def print_uniq(in_str):
    uniq_list = []
    input_list = list(in_str)
    
    for i in input_list:
        if i not in uniq_list:
            uniq_list.append(i)
    
    # I tried to use list comprehension, but I can't figure out how it will work
    # uniq_list = [uniq_list.append(i) for i in input_list if i not in uniq_list]

    result = "".join(uniq_list)
    return result


in_str = "AAA BB CC"
#in_str = "abcabcabc"
#in_str = "abababababacdef"

print(print_uniq(in_str))