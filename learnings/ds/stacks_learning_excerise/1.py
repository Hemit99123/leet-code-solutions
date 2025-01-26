def reverse_string(text):
    stack = []

    reverse = ""

    for char in text:
        stack.push(char)
        
    for _ in range(stack.size()):
        new_char = stack.pop()
        reverse += new_char
        
    return reverse


print(reverse_string("We will conquere COVID-19"))
# 91-DIVOC ereuqnoc lliw eW
