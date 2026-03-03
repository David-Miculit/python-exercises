nr_1 = int(input("First number: "))
nr_2 = int(input("Second number: "))
operation = input("Choose an operation: ")

expression = f"{nr_1} {operation} {nr_2}"
print("Expression: ", expression)

try:
    result = eval(expression)
    print("Result: ", result)
except SyntaxError:
    print("Invalid expression")