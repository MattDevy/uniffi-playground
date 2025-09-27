from mathlib.math import add, sub, div, equal, ArithmeticError

print(add(1, 2))
print(sub(2, 1))
print(div(4, 2))
print(equal(1, 2))

try:
    print(sub(0, 1))
except ArithmeticError as e:
    print(f"ArithmeticError: {e}")