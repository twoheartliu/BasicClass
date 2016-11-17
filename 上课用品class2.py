# ———选择控制———
#
# if 可以根据情况选择性执行某些语句
# 例如
#
# 定义一个变量 grade 代表年级
grade = 3
# 如果 grade 小于 7
if grade < 7:
    # 这句 print 只在 grade 小于 7 这个条件满足的情况下会被执行
    print('小学生')

# 选择控制有多种不同的用法
# 只有if
if 1 > 2:
    print('条件成立')

# if 带 else
# if else 必定会执行一个语句
# 如果 1 大于 2
if 1 > 2:
    print('条件成立')
# 否则
else:
    print('条件不成立')

# 多个if else
grade = 8
if grade < 7:
    print('小学生')
# elif 是 else if 是的缩写
# 历史遗留问题，大家理解就好
elif grade < 10:
    print('初中生')
else:
    print('高中生')

# 例子
# 求绝对值
n = -1
if n < 0:
    n = -n

# 判断奇偶
n = 1
# 取余数的操作符是 %
# 比较运算是两个等号 ==
if n % 2 == 0:
    print('偶数')
else:
    print('奇数')

# ——比较运算和逻辑操作——
#
# if 判断的条件其实是一个值, 这种值叫 布尔值 (bool, Boolean)
# 因为纪念数学家 Boolean
# 这种值只有两种结果, 一个是 真, 一个是 假
# 在 Python 中, 这两种值分别是 True 和 False
#
# 1 > 2 实际上是一个值, False
# if 是根据这个值来决定执行的语句的
#
# 一共有 6 种比较运算
# 下面分别是
# 相等、不等、小于、大于、小于等于、大于等于
# ==
# !=
# <
# >
# <=
# >=

# 例子
# 1 == 1
# 1 == 2
# 1 != 1
# 1 != 2
# 1 < 2
# 1 > 2
# 1 <= 1
# 1 >= 1

# 除了比较运算, 还有三种逻辑操作
# 三种逻辑操作分别是 与、或、非
# 在 Python 中 分别如下
# and   表示所有条件都要成立，结果才是 True ，只要有一个不成立就是 False
# or    表示只要有一个条件成立就是 True， 全部条件都不成立就是 FALSE
# not   对结果取反， not True 就是 False， not False 就是 True
#
# 用到的地方很广, 比如你登录网站的时候, 服务器要做如下判断
# if 用户名存在 and 密码验证成功:
#     登录成功
# else:
#     登录失败

# 注意
# 比较运算和逻辑操作的结果都是 bool（布尔类型），结果是 True 和 False

# 例子
# 1 == 1 and 2 == 2   # True
# 1 == 1 and 1 == 2   # False
# 1 == 1 or 1 == 2    # True
# not 1 == 1          # False

# 实际中尽量不要使用 not 来 进行逻辑操作，毕竟不符合人类习惯

# 可以加括号来让代码直观一点
# ((1 == 1) and (2 == 2)) or (1 == 2)
print('测试结果', ((1 == 1) and (2 == 2)) or (1 == 2))


# 优先级这种事，不要刻意去背了，直接括号就很方便

# 函数返回值
#
# 函数不仅可以合并操作重复性的代码
# 还可以通过计算得到一个结果, 结果就是返回值
# 函数可以有「返回值」
# 返回值的意思是函数调用的结果是一个值，可以被赋值给变量
# 函数调用得到的结果 就是函数的返回值
# 函数如果没有 return， 那么会 return None
# None 代表什么也没有
# 例
# 定义一个函数 add
# 接受 a b 两个参数
def add(a, b):
    # 用 return 语句来得到一个返回值
    # 函数执行到 return 的时候 就结束了
    return a + b
    print('不会被执行的代码')


# 用法
print('add 函数的返回值', add(1, 2))
number = add(1, 3)
print('add 函数的返回值 number ', number)


def return_print():
    return print


# 函数名加括号是调用函数
# 单纯的函数名是表示函数
# 相当于调用 return_print 函数， 对返回值进行调用，并传递字符串参数
return_print()('这是返回的函数')
# 相当于下面两行
# 中文也是合法的变量名
打印函数 = return_print()
打印函数('用返回的函数打印数据')


# 注意看上面的语句，add(1, 3)被当做一个值赋值给了变量number
# 也就是说这个函数调用是一个数值，数值的值就是函数的返回值
# 例如，使用函数来求绝对值
def abs(n):
    if n < 0:
        n = -n
    return n


print(abs(0))
print(abs(-8))
print(abs(3))


# 函数执行遇到 return 就结束
def minus(a, b):
    return a - b
    print('这一句是不会被执行的, 因为 return 的时候函数就结束了')


# 例
# 使用函数检查一个数字是否是奇数（奇数对2取余数不等于0）
def isOdd(n):
    # 取余数的操作符是 %
    if n % 2 != 0:
        return True
    else:
        return False


print(isOdd(1))
print(isOdd(2))
print(isOdd(3))
print(isOdd(4))


# 练习，实现isEven函数，偶数返回True，奇数返回False
def isEven(n):
    return n % 2 == 0
def isOdd(n):
    return not n % 2 == 0
    # return n % 2 != 0

# 返回两个参数中较小的一个
def min(a, b):
    if a < b:
        return a
    else:
        return b


print(min(1, 2))
print(min(3, 2))


# 练习，实现max函数，接受两个参数，返回较大的那一个值



# 标准库
# 库 是一个编程术语, 意思是一系列函数的集合
# 比如 turtle 就是一个库, 用来画图
#
# 标准库 也是一个术语, 指的是语言自带的库
#
# Python 的官方文档有所有标准库的文档(当然, 不那么容易看懂)
# 我们可以用标准库实现很多功能
#
# 使用标准库就是简单地 import 即可
# 例如, 标准数学库可以这样用
import math

print('30度的正弦应该是 0.5', math.sin(30))
# 但是结果并不是这样
# 所以应该查看文档
# 文档说， sin 函数的参数应该是弧度制
# 我们要先把角度转成弧度再传递给 sin 函数
# 角度转弧度是有函数的
print('30角度转弧度的sin', math.sin(math.radians(30)))
# 30 角度转弧度的sin 0.49999999999999994
# 可以发现，结果并不是 0.5
# 这是因为计算机无法表示小数，只能表示小数的近似值
# 因为小数的值域是无限的
# 但是计算机表示数字的位数是有限的
# 所以只能表示近似值

# Python 有很多有用的标准库, 所以应该大致翻阅一下目录
# 但不是现在
# 这样遇到某件事/问题你就知道该用什么方法去解决了
# 除了官网文档, 还有一本书叫 <Python 标准库>
# 但是不建议买，现在完全用不着
