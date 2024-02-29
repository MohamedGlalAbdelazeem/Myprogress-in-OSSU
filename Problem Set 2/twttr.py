






def remove_vowels(user_input):
    result = ''
    for char in user_input:
       if char not in 'aeiouAEIOU':
          result += char
    return result

def main():
    user_input = input("input: ")
    transofrom_input  = remove_vowels(user_input)
    print(transofrom_input)

main()