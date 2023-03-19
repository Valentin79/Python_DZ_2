MOD = 16
d = int(input("Input number: "))
print(hex(d))

digits = '0123456789abcdefghijklmnopqrstuvwxyz'
string = ""
while d > 0:
    string = digits[d % MOD] + string
    d //= MOD
print (string)
