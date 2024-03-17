"""在 ISO 国际标准中定义了 A0 纸张的大小为 1189mm × 841mm，
将 A0 纸沿长边对折后为 A1 纸，大小为 841mm × 594mm，
在对折的过程中长度直接取下整（实际裁剪时可能有损耗）。
将 A1 纸沿长边对折后为 A2 纸，依此类推。
输入纸张的名称，请输出纸张的大小。"""
li = ['A0','A1','A2','A3','A4','A5','A6','A7','A8','A9']
li_num = [1189, 841]
x = input('').strip()
for i in range(len(li)-1):
    a = round(li_num[i]//2, 0)
    #print(a)
    li_num.append(a)
print(li_num[li.index(x)])
print(li_num[li.index(x)+1])