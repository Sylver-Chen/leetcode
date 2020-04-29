##  1.一行输入
# 输入一个数/字符串
s = input()
print(s)
# abcd
# abcd

# 输入一个数组
s = input()
s = [i for i in s.splits()]
print(s)
# 1 2 3 4
# ['1', '2', '3', '4']

## 2.两行输入
# 两行输入要在第一行读取的基础上再进行一些操作。
# 假设第一行输入数组长度，第二行输入数组
while True:
    s = input()
    if s != "":
        length = int(s)
        nums = [int(i) for i in input().split()]
        print(length, nums)
        break
    else:
        break

## 3.多行输入
## 每行输入一个数/字符串
while True:
    s = input()
    if s != "":
        print(s)
    else:
        break

# 每行读取不同的内容
# 比如，第一行输入操作个数，第二行输入数组
data = []
length = int(input())
n = 0
while n < length:
    s = input()
    if s ！= "":
        tmp = [i for i in s.splits()]
        data.append(tmp)
        n += 1
    else:
        break
print(data)
