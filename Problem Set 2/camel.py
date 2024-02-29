
# camelCase & snake_case

# take input from user the name camel case 
# output snake case
 
 
def camel_to_snake(camel_case):
    snake_case=""
    for char in camel_case:
        if char.isupper():
            snake_case+= "_" + char.lower()
        else:
            snake_case += char
    return snake_case
            
def main():
    camel_case = input("Enter name:")
    snake_case = camel_to_snake(camel_case)
    print(snake_case)

main()


 