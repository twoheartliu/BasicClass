# 此为第三课的作业 2
#

# 例 1
# 返回两个参数中较小的一个
def min(a, b):
    if a < b:
        return a
    else:
        return b

# print(min(1, 2))
# print(min(3, 2))


# 作业 1
# 实现 max 函数
# 接受两个参数
# 返回较大的那一个值
# def max(a, b)


# 作业 2
# 实现 max 函数
# 接受一个参数, 类型为 list
# 返回 list 中最大的元素
# list 中只包含数字
# def max(l)


# 作业 3
# 实现 min 函数
# 接受一个参数, 类型为 list
# 返回 list 中最小的元素
# list 中只包含数字
# def min(l)


# 作业 4
# 实现 sum 函数
# 接受一个参数, 类型为 list
# 返回 list 中所有元素的和
# list 中只包含数字
# def sum(l)


# 作业 5
# 实现 average 函数
# 接受一个参数, 类型为 list
# 返回 list 中所有元素的平均数
# list 中只包含数字
# def average(l)


# 作业 6
# 实现 sum1 函数
# 接受一个参数 n
# 返回 1 - 2 + 3 - 4 + ... n 的值
# def sum1(n)


# 作业 7
# 实现 sum2 函数
# 接受一个参数 n
# 返回 1 + 2 - 3 + 4 - ... n 的值
# def sum2(n)


# 作业 8
# 实现 fac 函数
# 接受一个参数 n
# 返回 n 的阶乘, 1 * 2 * 3 * ... * n
# def fac(n)


# 作业 9
# 实现 fib 函数
# 接受一个参数 n
# 返回第 n 个斐波那契数
# 斐波那契数列如下, 规律自寻或搜索
# 1 1 2 3 5 8 13 21
# def fib(n)


# 作业 10
# 实现 fib_list 函数
# 接受一个参数 n
# 返回前 n 个斐波那契数组成的 list
# 斐波那契数列如下, 规律自寻或搜索
# 1 1 2 3 5 8 13 21
# def fib_list(n)


# 注意 下面几题中的参数 op 是 operator(操作符) 的缩写
#
# 作业 11
# 实现 apply 函数
# 参数如下
# op 是 '+' '-' '*' '/' 其中之一
# a b 分别是 2 个数字
# 根据 op 对 a b 运算并返回结果(加减乘除)
# def apply(op, a, b)


# 作业 12
# 实现 apply_list 函数
# op 是 '+' '-' '*' '/' 其中之一
# oprands 是一个只包含数字的 list
# 根据 op 对 oprands 中的元素进行运算并返回结果
# def apply(op, oprands)
# 例如, 下面的调用返回 -4
# apply('-', [3, 4, 2, 1])


# 作业 13
# 实现 apply_compare 函数
# 参数如下
# expression 是一个 list, 包含了 3 个元素
# 第一个元素是 op, 值是 '>' '<' '==' 其中之一
# 剩下两个元素分别是 2 个数字
# 根据 op 对数字运算并返回结果(结果是 True 或者 False)
# def apply_compare(expression)


# 注意
# 下面两题做不出来没关系
#
# 作业 14
# 实现 apply_if 函数
# 参数如下
# expression 是一个 list, 包含了 4 个元素
# 第一个元素是 'if' (也就是 op)
# 第二个元素是 'True' 或者 'False'
#
# 如果第二个元素的结果是 True 则返回第三个元素
# 否则返回第四个元素
# def apply_if(expression)


# 作业 15
# 实现 apply_all 函数
# 参数如下
# expression 是一个 list
# expression 中第一个元素是上面几题的 op, 剩下的元素是和 op 对应的值
# 根据 expression 运算并返回结果
# def apply_all(expression)


# 注意
# 下次作业起, 会用更标准简练的方式来表示参数类型和说明
