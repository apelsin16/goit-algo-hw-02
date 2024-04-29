def check_symmetry(symbols):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for symbol in symbols:
        if symbol in pairs.values():
            stack.append(symbol)
        elif symbol in pairs.keys():
            if not stack or pairs[symbol] != stack.pop():
                return "Несиметрично"
    return "Симетрично" if not stack else "Несиметрично"

# Приклади використання програми
print(check_symmetry("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Симетрично
print(check_symmetry("( 23 ( 2 - 3);"))             # Несиметрично
print(check_symmetry("( 11 }"))                     # Несиметрично
