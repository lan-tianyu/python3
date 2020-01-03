import math

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# 1. 列表推导器，数据量比较大的情况下比较占内存
print([n for n in mylist if n >= 0])
print([n for n in mylist if n < 0])

# 2. 生成器表达式
pos = (n for n in mylist if n >= 0)
print(pos)
print(list(pos))

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


# 过滤的时候需要一些特殊的处理逻辑
def is_int(val):
    try:
        int(val)
        return True
    except Exception as e:
        print(e)
        return False


print(list(filter(is_int, values)))

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print([math.sqrt(x) for x in mylist if x >= 0])
print([n if n >= 0 else 0 for n in mylist])
