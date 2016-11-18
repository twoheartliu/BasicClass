# 这里是两个字符串, 包含了大写字母和小写字母
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 字符串有一个 find 函数
# 可以返回 参数 在字符串中的首次出现的下标
# 例如
print(lower.find('e'))
# 4
print(lower.find('E'))
# -1 因为找不到


# 例子
# 返回字符串的小写形式
# 注意, 假设 s 字符串全是大写字母
def lowercase(s):
    # 初始化一个空字符串
    result = ''
    # 遍历字符串
    for c in s:
        # 对每一个字符串, 找到它在 upper 中的下标
        i = upper.find(c)
        # 然后把它加到 result 中
        # result = result + lower[i]
        # 下面的 += 相当于上面的语句, 是一个简便的写法
        result += lower[i]
    # 返回结果
    return result


# 1
# 定义一个函数
# 参数是一个字符串 s
# 返回大写后的字符串
# 注意, 假设 s 字符串全是小写字母
# def uppercase(s):


# 2
# 让 lowercase 能正确处理带 小写字母 的字符串


# 3
# 让 uppercase 能正确处理带 大写字母 的字符串


# 4
# 凯撒加密
# 对于一个字符串, 整体移位, 就是加密
# 假设移 1 位
# 原始信息 'afz' 会被加密为 'bga'
# 实现 encode, 把明文加密成密码并返回
# 移 1 位
# def encode(s)


# 5
# 实现 decode, 把密码解密为明文并返回
# 移 1 位
# def decode(s)


# 6
# 实现新的 encode
# 多了一个参数 shift 表示移的位数
# def encode(s, shift)


# 7
# 实现新的 decode
# 多了一个参数 shift 表示移的位数
# def decode(s, shift)

# 8
# 实现新的 encode
# 多了一个参数 shift 表示移的位数
# 如果 s 中包含了不是字母的字符, 比如空格或者其他符号, 则不做任何处理保留原样
# def encode(s, shift)


# 9
# 实现新的 decode
# 多了一个参数 shift 表示移的位数
# 如果 s 中包含了不是字母的字符, 比如空格或者其他符号, 则不做任何处理保留原样
# def decode(s, shift)


# 10
# 知乎有一个求助题, 破译密码的
# 当然了, 根据普通人定律, 小孩子喜欢用这种方式表白...
# 链接在此
# https://www.zhihu.com/question/28324597
# 另, 这一看就是凯撒加密...
# 如果没思路, 可看本文件最后的提示
# 我把密码放在下面, 请解出原文
s = 'VRPHWLPHV L ZDQW WR FKDW ZLWK BRX,EXW L KDYH QR UHDVRQ WR FKDW ZLWK BRX'

# 请在做出这道题后, 观摩知乎链接中的各个答案, 好好地吸取大神们的营养















# 10 题提示
# 没有给出 shift 信息, 怎么办?
#
# 强行试出来
