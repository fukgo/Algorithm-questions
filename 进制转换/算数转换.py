# 十进制转换为二进制：
def dec_to_bin(num):
    li = []
    if num<0:
        return '-' + dec_to_bin(abs(num))
    while True:
        num, reminder = divmod(num, 2)
        li.append(str(reminder))
        if num == 0:
            #','.join('abc')
            #将字符串abc中的每个成员以字符','分隔开再拼接成一个字符串
            return ''.join(li[::-1])


# 十进制转换为八进制：
def dec_to_oct(num):
    li = []
    if num<0:
        return '-' + dec_to_bin(abs(num))
    while True:
        num, reminder = divmod(num, 8)
        li.append(str(reminder))
        if num == 0:
            #','.join('abc')
            #将字符串abc中的每个成员以字符','分隔开再拼接成一个字符串
            return ''.join(li[::-1])
if __name__ == '__main__':
    print(dec_to_bin(159))
