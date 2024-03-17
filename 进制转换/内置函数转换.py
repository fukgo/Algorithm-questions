"""
十进制（Decimal）
二进制（Binary）
八进制（Octal）
十六进制（Hexadecimal）"""
n = 555
# 十进制转二进制： bin()
print(bin(n))
# 十进制转八进制： oct()
print(oct(n))
# 十进制转十六进制：hex()
print(hex(n))

# 任意进制转十进制：
m = 2, 8, 10
# int(n, m) n为任意数
#int('10', base=2)将字符串'10'解释为二进制数，并将其转换为十进制整数。在二进制中，数字10表示十进制中的数字2。因此，int('10', base=2)的结果为2。
"""其他任意进制转任意进制，先用int()转为十进制，
然后用bin()，oct()，hex()转为其他进制"""