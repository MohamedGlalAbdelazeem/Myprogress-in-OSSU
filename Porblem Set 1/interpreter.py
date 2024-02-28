def calculate(expression):
    # Split the expression into its components val oper val
    x, op, z = expression.split()
    # Convert operands to integers
    x = float(x)
    z = float(z)
    # Perform the arithmetic operation based on the operator
    if op == '+':
        result = x + z
    elif op == '-':
        result = x - z
    elif op == '*':
        result = x * z
    elif op == '/':
        result = x / z

    return round(result, 1)  # Round the result to one decimal place


def main():
    expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")
    try:
        result = calculate(expression)
        print("Result:", result)
    except ValueError:
        print("Invalid expression format. Please enter an expression in the format ' 1 + 1 '.")

main()
