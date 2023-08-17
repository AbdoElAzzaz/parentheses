def generate_parentheses(n):
    result = []
    backtrack(n, n, '', result)
    return result

def backtrack(left, right, current, result):
    if left == 0 and right == 0:
        result.append(current)
        return

    if left > 0:
        backtrack(left - 1, right, current + '(', result)
    if right > left:
        backtrack(left, right - 1, current + ')', result)

n = int(input("Enter the number of parentheses pairs: "))

result = generate_parentheses(n)
print(result)