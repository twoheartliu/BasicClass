# 作业 1
# 以后每次的作业出来后 我会放到群公告
# 
# 这表示引入了一个别人写好的东西(术语模块, 很快会讲)
import turtle

# 这样可以得到一个变量 t, 可以对它进行很多操作
# 很快会讲, 现在先用
t = turtle.Turtle()
t.speed(0)
color = '#55C2DD'
t.pencolor(color)


# 例子 1
# 
# 实现函数, 用于画一个边长 100 的正方形
# 参数 x, y 是正方形左上角坐标
def square(x, y):
    # 这三行的意思是 移动到 x y 处
    # 但是不露痕迹 (参考资料)
    t.penup()
    t.goto(x, y)
    t.pendown()
    # 设置朝向, 确保箭头朝向 右边
    # 如果是用 t.goto 来画的话, 就不用关心朝向
    t.setheading(0)
    # 循环画正方形
    # 当然, 你可以用 t.goto 来画
    # 只需要计算一下四个顶点的坐标 (这很简单)
    for i in range(4):
        t.forward(100)
        t.right(90)


# 1
# 实现函数, 用于画一个正方形, 边长由参数提供
# 参数 x, y 是正方形左上角坐标
# 参数 l 是正方行边长
# 函数声明如下
# def square(x, y, l)

# 直接参考例子
def square(x, y, l):
    # 这三行的意思是 移动到 x y 处
    # 但是不露痕迹 (参考资料)
    t.penup()
    t.goto(x, y)
    t.pendown()
    # 设置朝向, 确保箭头朝向 右边
    # 如果是用 t.goto 来画的话, 就不用关心朝向
    t.setheading(0)
    # 循环画正方形
    # 当然, 你可以用 t.goto 来画
    # 只需要计算一下四个顶点的坐标 (这很简单)
    for i in range(l):
        t.forward(100)
        t.right(90)


# 我们发现我们会一直使用“不露痕迹的把画笔移动到某处”这个功能那么可以把这个功能写成函数

def setpen(x, y):
    # 这三行的意思是 移动到 x y 处
    # 但是不露痕迹 (参考资料)
    t.penup()
    t.goto(x, y)
    t.pendown()
    # 设定朝向
    t.setheading(0)


# 这时，我们第一题可以写成这样

def square(x, y, l):
    setpen(x, y)
    for i in range(l):
        t.forward(100)
        t.right(90)


# 作业资料中提到 goto 可以直接走到某个坐标
# 如果我们用 goto 来画的话

def square(x, y, l):
    setpen(x, y)
    t.goto(x + l, y)
    t.goto(x + l, y - l)
    t.goto(x, y - l)
    t.goto(x, y)


# 可以看出 goto 只适用于已知坐标点的情况，明显，用循环来做更为便捷
# 试着调用函数检验自己画出的图形是否正确
# square(10,20,80)

# 2
# 实现函数, 用于画一个矩形, 长宽由参数提供
# 参数 x, y 是左上角坐标
# 参数 w, h 是 宽高
# 函数声明如下
# def rect(x, y, w, h)
def rect(x, y, w, h):
    setpen(x, y)
    for i in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)


# rect(10,20,40,60)
# 使用 control + / 快速注释某一行

# 3
# 画一排正方形, 一共 5 个
# 从 0 0 点开始, 边长为 30, 正方形之间间隔为 0
# 函数声明如下
# def square5()
# 提示 根据资料中的循环例子, 计算每个正方形的坐标

# 写程序的时候，重点考虑做什么，不要考虑怎么做
# 要有大局观
# 要想 what 不要想 how
def square5():
    for i in range(5):
        square(x, y, 30)


# 上面这个函数显然是不完全的，但是我们已经把框架写好了
# square x,y 的坐标我们需要确定
# 观察 i 与 x , y 之间存在什么关系
# 根据给出的资料中的循环的解释
# i 的值是 0  1  2  3  4
# x 的值是 0 30 60 90 120
# y 的值是 0

def square5():
    for i in range(5):
        x = 30 * i
        y = 0
        square(x, y, 30)


# square5()

# 4
# 画一排正方形, 一共 5 个
# 从 0 0 点开始, 边长为 30, 正方形之间间隔为 10 像素
# 函数声明如下
# def square5()
def square5():
    l = 30
    space = 10
    for i in range(5):
        # 同上，观察 x 与 i 的关系
        # i 是 0 1 2 3 4 5
        # x 是 0 30+10 60+20 90+30 120+40
        x = i * (l + space)
        y = 0
        square(x, y, l)


# 可以先在纸上画出来，总结出规律
# 编程最重要的不是代码量的多少，而是理清思路

# 5
# 实现函数, 画一排正方形, 有如下参数
# x, y 是第一个正方形左上角坐标
# n 是正方形的个数
# space 是两个正方形之间的间距
# l 是正方形的边长
# def square_line(x, y, n, space, l)
def square_line(x, y, n, space, l):
    setpen(x, y)
    for i in range(n):
        # x 起点可在任意位置，且 inner_x 不应被 x 覆盖
        inner_x = x + i * (l + space)
        inner_y = y
        square(inner_x, inner_y, l)


# square_line(-200,-10,5,10,20)

# 6
# 实现函数, 用上题的函数来画一个正方形方阵, 参数如下
# x, y 是第一个正方形左上角坐标
# space 是两个正方形之间的间距
# l 是正方形的边长
# n 是横向正方形的个数
# m 是纵向正方形的个数
# def square_square(x, y, space, l, n, m)
def square_square(x, y, space, l, n, m):
    setpen(x, y)
    for i in range(m):
        line_x = x
        line_y = y - (l + space) * i
        square_line(line_x, line_y, n, space, l)


# 把一排矩形抽象为一个，只考虑纵行的 m 次 循环


# 7
# 实现函数, 画一排矩形, 有如下参数
# x, y 是第一个矩形左上角坐标
# w, h 是矩形宽高
# n 是矩形的个数
# space 是两个矩形之间的间距
# def rect_line(x, y, w, h, space, n)

# 跟上面是同样的理念，首先观察我们可以复用哪些函数
# 把框架敲定，再来实现细节
def rect_line(x, y, w, h, space, n):
    setpen(x, y)
    for i in range(n):
        # x 起点可在任意位置，且 inner_x 不应被 x 覆盖
        rect_x = x + i * (w + space)
        rect_y = y
        rect(rect_x, rect_y, w, h)


# rect_line(-100, -200, 80, 50, 20, 5)



# 8
# 实现函数, 画一个矩形方阵, 参数如下
# x, y 是第一个矩形左上角坐标
# space 是两个矩形之间的间距(横向和纵向)
# w, h 是矩形的长宽
# n 是横向矩形的个数
# m 是纵向矩形的个数
# def rect_square(x, y, space, w, h, n, m)
def rect_square(x, y, space, w, h, n, m):
    setpen(x, y)
    for i in range(m):
        line_x = x
        line_y = y - (h + space) * i
        rect_line(line_x, line_y, w, h, space, n)


# rect_square(-100, 200, 20, 50, 80, 5, 6)

# 9
# 实现函数, 画一个正多边形, 参数如下
# x y 是起点, 设起点为多边形的顶部边的左顶点
# n 是多边形的边数
# l 是边长
# def polygon(x, y, n, l)
def polygon(x, y, n, l):
    setpen(x, y)
    angle = 360 / n
    for i in range(n):
        t.forward(l)
        t.right(angle)


# polygon(-10, -20, 6, 50)


# 10
# 实现函数, 画一个正多边形, 参数如下
# x y 是中心点
# n 是多边形的边数
# l 是边长
# def polygon(x, y, n, l)
# 
# 提示, 有中心点, 就能算出顶部边的起点
# 使用角度 / 转向 / t.setheading 实现这个函数
def polygon(x, y, n, l):
    setpen(x, y)
    t.left(90)
    angle = 360 / n / 2
    # c = 2 * pi * r
    c = l * n
    pi = 3.1415926535
    r = c / (2 * pi)
    t.forward(r)
    t.setheading(0)
    a = 360 / n
    for i in range(n):
        t.forward(l)
        t.right(a)


# polygon(0, 0, 8, 50)
# 这里选择用圆来近似，三角函数什么的太难啦~

# 11
# 实现函数, 画圆
# 参数如下
# x, y, r 分别是 圆心坐标 和 半径
# def circle(x, y, r)
# 
# 思路
# 假设圆为正 36 边形(无所谓 你可以提高 我觉得 36 就好了)
# 那么周长 c 是 2 * PI * r
# PI 就设为 3.14 好了
# 所以就可以算出 边长
# 有了边长 就能算出第一步的坐标
# 然后就可以画一个 正36边形 了
# 记得用 资料中的函数来辅助
# 当然 你可以直接使用上题的函数
def circle(x, y, r):
    n = 36
    pi = 3.1415926535
    c = 2 * pi * r
    l = c / n
    polygon(x, y, n, l)

circle(0,-10,50)


# 画完后一定要加上这一句
turtle.done()
