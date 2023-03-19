import fractions

f1 = fractions.Fraction(1, 3)
f2 = fractions.Fraction(3, 5)

print(f"{f1} + {f2} = {f1+f2}")
print(f"{f1} * {f2} = {f1*f2}")


num1 = 1
den1 = 3
num2 = 3
den2 = 5


def multiply_fractions(num1, den1, num2, den2):
    num = num1 * num2
    den = den1 * den2
    common_factor = gcd(num, den)
    num //= common_factor
    den //= common_factor
    return (num, den)

def add(num1, num2, num3, num4):
    x = num1 * num4 + num2 * num3
    y = num2 * num4
    z = gcd(x, y)
    return (x//z, y//z)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

product_num, product_den = add(num1, den1, num2, den2)
print(f"Сумма: {product_num}/{product_den}")
product_num, product_den = multiply_fractions(num1, den1, num2, den2)
print(f"Произведение: {product_num}/{product_den}")


