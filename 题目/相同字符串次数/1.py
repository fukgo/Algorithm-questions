s = input().strip()
target = "helloworld"
count = 0
length = len(target)
n = len(s)
for i in range(n - length + 1):
    if s[i:i + length] == target:
        count += 1
print(count)


# 示例测试

print("字符串中 'helloworld' 单词出现的次数为:", count)