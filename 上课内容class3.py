# 16/07/12
#
# 此为第三课的上课内容
#
# 今天上课的内容是
# 作业 2 讲解
# debug(调试/除错) 的标准应对流程
# list 和 str
#
# 预习内容是
#
# 内置数据结构 list(列表)
# 字符串和常用字符串操作
#
# 看不懂, 很正常
# 完全看不懂, 有小问题


# list 可以干嘛?
# list 可以存储很多元素, 每个元素的值、类型都不用相同
# 具体看下面的例子
#
# list(列表) 常用操作
# 创建列表
# 使用 [] 符号, 每个元素用逗号分隔
a = [1, 3, 4, 5]
# 现在 a 是一个 list，拥有 4 个元素


# 可以用 len 函数返回 list 的长度
print('求 list 长度', len(a))
# 使用 len() 函数可以求出列表的长度(列表中元素的个数)
# 值可以用变量接住
length = len(a)
print(length)

# 访问元素
# 对于列表中的每个元素, 可以通过下标（就是元素在列表中的序号，从 0 开始）访问
# 下标访问语法是 [] 中括号
print('用下标访问 list 中的元素')
print(a[0])
print(a[1])
print(a[2])
print(a[3])
# 因为一共只有 4 个元素, 所以访问不存在的下标会出错
# print(a[4])


# 手动访问元素当然是低效的
# 可以用循环来访问元素, 这个过程叫 遍历列表
print('循环访问 list 所有元素')
length = len(a)
for i in range(length):
    print('循环遍历', a[i])

# 不用下标取数据
# 直接遍历得到元素
# element 是一个变量名， 可以是任意合法变量名
for element in a:
    print('直接遍历元素', element)

# 向已经存在的 list 中添加新元素
# 可以用列表的 append 函数往列表末尾插入一个元素
# 并且, 这个新元素可以是任意类型, 这里是一个字符串
a.append('新元素')
print(a)
# [1, 3, 4, 5, '新元素']
a.append(0)
print(a)
# [1, 3, 4, 5, '新元素', 0]
# 多添加几个元素
a.append(12)
a.append(23)
a.append(34)
print(a)

# 下面用一个新列表进行下面的讲解
# 注意 a 已经是新列表了
a = [1, 3, 2, 3, 4, 5, 3]
# 删除一个特定的元素, 该元素必须出现在列表中, 否则会出错
a.remove(4)
print(a)
# [1, 3, 2, 3, 5, 3]
# 删除不存在的元素会出错
# 自己试试下面这句
# a.remove(100)
# 可以发现, 列表中有多个相同的元素 3
# 试试删除它会怎样
a.remove(3)
print(a)
# [1, 2, 3, 5, 3]
a.remove(3)
print(a)


# [1, 2, 5, 3]
# 结论是 remove 函数只会删除从头到尾出现的第一个该元素
# 多尝试, 很多事情试试看就知道了

# 例子，得到列表中最大的元素

def max_element(l):
    m = l[0]
    for e in l:
        if m < e:
            m = e
    return m


# print('Max', max_element([1, 2, 3, 5, 4]))


# 题目, 给定一个只包含数字的 list
# 题目，得到列表中最小的元素
# 题目，得到列表中所有数字的合
# 题目，得到列表中所有数字的平均数
# 提示，len 函数可以求 list 长度（也就是数字个数），上文有写







# 字符串
# ——字符串操作——
#
# 字符串可以判断相等、判断是否包含、相加、取子字符串
#
# 例子：
# 判断相等或者包含
print('good' == 'good')
print('good' == 'bad')
print('good' != 'bad')
print('possible' in 'impossible')
print('lie' in 'believe')

# 拼接得到一个新字符串
print('very' + 'good')
print('very ' + 'good')
# 得到一个你想要的字符串有多种方式
# 但是现在有现代的方式, 字符串的 format 函数
# 注意, 书上如果和我不一样, 以我为准
# 用法如下
name = 'fanfouer'
a = '{}, 你好'.format(name)
print(a)
a = '{}, {}'.format('fanfouer', 'evening')
print(a)
# 简单说来, 就是 花括号会被 format 函数的参数替换行成新字符串


# 字符串相当于一个一定长度的 list，可以用数字下标访问
# 看例子，看结果
# s 的长度为7，但是下标是从 0 开始的，所以最大下标是6
s = 'iamgood'
print(s[0])
print(s[1])
print(s[2])
# ...
print(s[6])
#
# 当然也就可以和 list 一样用循环遍历了
# 自己试试
for i in s:
    print('循环遍历 str', i)
# 字符串可以切片, 当然, list 也可以这样切片
# 语法如下
# s[开始下标:结束下标]
s[0:3]  # 'iam'
s[1:3]  # 'am'

# 省略下标参数意思是取到底
s[:3]  # 'iam'
s[2:]  # 'mgood'

# 下标是负数代表反着来（看看就好，不必记忆）
s[:-1]  # 'iamgoo'
s[:-2]  # 'iamgo'

# tuple 元组
# tuple 和 list 一模一样
# 只是你不能往里面添加新元素，也不能删除
# 总之就是不能修改
# 其他和 list 是一样的
# tuple 用括号表示
t = (1,2,3)
print('tuple',t)