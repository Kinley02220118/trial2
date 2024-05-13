def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

word = input('Enter any word you like: ')
print('Reversed string:', reverse_string(word))