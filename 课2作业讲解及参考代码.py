# 作业 2 作业
#
#
import turtle

# 这是套路
t = turtle.Turtle()
t.speed(0)


# 特殊语法的 log 函数
# 不要管，套路，照抄就是
def log(*args):
    print('log', *args)
    return


# 无痕设置画笔位置的辅助函数
def setpen(x, y):
    # 这三行的意思是 移动到 x y 处
    # 但是不露痕迹 (参考资料)
    t.penup()
    t.goto(x, y)
    t.pendown()
    # 设置朝向, 确保箭头朝向 右边
    # 如果是用 t.goto 来画的话, 就不用关心朝向
    t.setheading(0)


# 背景资料
# 介绍一些额外的函数用来填充颜色
# 作业中会用到
# 关于颜色, 请参考作业 1 的资料

# 填充颜色的方法
# x y
# length 边长
# color 填充颜色
def colored_square(x, y, length, color):
    setpen(x, y)
    # 设置画笔颜色和填充色一致, 这样就不会有边框了
    t.pencolor(color)
    # 设置填充颜色
    t.fillcolor(color)
    # 开始填充
    t.begin_fill()
    for i in range(4):
        t.forward(length)
        t.right(90)
    # 结束填充
    # 在开始填充和结束填充之间的点会组成一个多边形并填色
    # 具体请自行尝试
    t.end_fill()


# 这个颜色为红色, 颜色代码请参考作业 1 的资料
# colored_square(0, 0, 100, '#ff0000')

def setcolor(color):
    t.pencolor(color)
    # 设置填充颜色
    t.fillcolor(color)


# 作业开始

# 1
# 实现一个矩形函数
# x y 是矩形左上角坐标
# w h 是宽高
# color 是矩形的颜色
# def rect(x, y, w, h, color)
def rect(x, y, w, h, color):
    setpen(x, y)
    angle = 90
    setcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.right(angle)
        t.forward(h)
        t.right(angle)
    t.end_fill()


# rect(-10, -100, 50, 20, 'blue')


# 2
# 实现一个矩形函数
# x y 是矩形中心的坐标
# w h 是宽高
# color 是矩形的颜色
# def center_rect(x, y, w, h, color)
def center_rect(x, y, w, h, color):
    center_x = x - w / 2
    center_y = y + h / 2
    rect(center_x, center_y, w, h, color)


# center_rect(-10, -200, 50, 80, 'green')

# 3
# 实现一个圆形函数
# x y 是圆心坐标
# r 是半径
# color 是填充色
# def circle(x, y, r, color)
#
# 提示, 我们以正 36 形为圆
def circle(x, y, r, color):
    n = 36
    angle = 360 / n
    pi = 3.1415926535
    c = 2 * pi * r
    l = c / n
    start_x = x - l / 2
    start_y = y + r
    setpen(start_x, start_y)
    setcolor(color)
    t.begin_fill()
    for i in range(n):
        t.forward(l)
        t.right(angle)
    t.end_fill()


# circle(-10, -100, 50, 'red')

# 4
# 实现一个五角星函数
# x y 是五角星横边左边坐标
# length 是一条线的长度
# color 是填充色
# def wujcxy(x, y, length, color)
def fivestar(x, y, length, color):
    setpen(x, y)
    angle = 144
    setcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(length)
        t.right(angle)
    t.end_fill()


# fivestar(-10, -10, 100, 'yellow')

# 5
# 实现一个函数画日本国旗
# 调用 2 个函数画日本国旗
# 一个画背景的白色矩形
# 一个画中间的红色圆
# def japan()
#
# 注意, 你可以添加 x y w h 参数让国旗画在任意地方, 任意尺寸
# 注意, 以下所有国旗同理
def japan():
    x, y, w, h = 0, 0, 300, 200
    center_rect(x, y, w, h, '#EEEEEE')
    circle(x, y, 50, 'red')


# 我们不关心国旗真正的比例如何计算只需要把它掏出来就好
# 注意是如何把代码如何拆分组合的

# japan()

# 6
# 实现一个函数画中国国旗(以下国旗题目都是如此 不重复了)
# 调用 2 个函数画中国国旗
# 一个画红色背景
# 另一个画五角星（调用 5 次，不要求角度朝向，只要5个五角星即可）
# def china()
def china():
    x, y, w, h = 0, 0, 300, 200
    center_rect(x, y, w, h, 'red')
    fivestar(-120, 60, 50, 'yellow')
    fivestar(-65, 80, 15, 'yellow')
    fivestar(-50, 60, 15, 'yellow')
    fivestar(-50, 40, 15, 'yellow')
    fivestar(-65, 20, 15, 'yellow')


# china()
# 同上，五角星差不多相似就行了…

# 7
# 实现一个函数画法国国旗
# def france()
def france():
    x, y, w, h = 0, 0, 300, 200
    width = w / 3
    x1 = x
    x2 = x + width
    x3 = x + 2 * width
    rect(x1, y, width, h, '#0000ff')
    rect(x2, y, width, h, '#ffffff')
    rect(x3, y, width, h, '#ff0000')


# france()

# 8
# 画德国国旗
# def germany()
def germany():
    x, y, w, h = 0, 0, 300, 200
    height = h / 3
    y1 = y
    y2 = y - height
    y3 = y - 2 * height
    rect(x, y1, w, height, 'black')
    rect(x, y2, w, height, 'red')
    rect(x, y3, w, height, 'yellow')


# germany()

# 9
# 画 冈比亚国旗
# def gambia()
def gambia():
    x, y, w, height = -100, 0, 300, 200
    h = height / 3
    y1 = y
    y2 = y - h
    y3 = y - h - h
    rect(x, y1, w, h, 'red')
    rect(x, y2, w, h, 'white')
    rect(x, y3, w, h, 'green')
    center_rect(x + w / 2, y - height / 2, w, height / 8, 'blue')


# gambia()
# 观察，先画出三个大的色块，再画中间的色块

# 10
# 画 瑞士国旗
# def switzerland()
def switzerland():
    x, y, w, h = 0, 0, 300, 200
    cross_w = h * 0.2
    cross_h = h * 0.6
    center_rect(x, y, w, h, 'red')
    center_rect(x, y, cross_w, cross_h, 'white')
    center_rect(x, y, cross_h, cross_w, 'white')


# switzerland()

# 11
# 画朝鲜国旗
# 分别是 圆 矩形 五角星
# 提示, 使用之前定义的函数
# def northkorea()
# 并无特殊之处，大家画一下就好了，这里就不给答案了

# 12
# 画出美国国旗
# 美国国旗是 13 条横杠 加上 50 颗星星
#
# 这题做不出拉倒

# 定义星条旗红白相间的颜色
def color_for_bar(i):
    if i % 2 == 0:
        color = 'red'
    else:
        color = 'white'
    log('color for bar', color, i)
    return color

# 画13条红白相间的条纹
def us_bars(x, y, w, h):
    log('us bars')
    h = h / 13
    for i in range(13):
        color = color_for_bar(i)
        start_y = y - h * i
        log('us bars, color, ', color)
        rect(x, start_y, w, h, color)

# 单独的一行星星
def star_line(x, y, w, h, n):
    length = w * 0.6
    for i in range(n):
        star_x = x + i * w
        fivestar(star_x, y, length, 'white')

# 成排的星星
def star_lines(x, y, w, h):
    height = h / 9
    w = w / 6.5
    for i in range(9):
        if i % 2 == 0:
            n = 6
            offset_x = x + 10
        else:
            n = 5
            offset_x = x + 20
        offset_y = y - i * height - 5
        star_line(offset_x, offset_y, w, h, n)

# 汇集成星条旗左上角的一块
def us_stars(x, y, w, h):
    w = w * 2 / 5
    h = h * 7 / 13
    rect(x, y, w, h, 'blue')
    #
    star_lines(x, y, w, h)

# 整个的美国国旗
def america():
    log('usa')
    x, y, w, h = 0, 0, 300, 200
    us_bars(x, y, w, h)
    us_stars(x, y, w, h)

# america()

# 美国国旗非常复杂，要理解到层层剥离把一个复杂的问题分解整合的编程思想

# 画完后一定要加上这一句
# 这句在整个文件的最后面
turtle.done()

# 遇到 bug 的标准应对流程
#
# 应对 1
# 遇到 bug 的第一反应是什么
# 不要慌

# 应对 2
# 看错误描述
# 1，看哪个文件出错
# 2，看错误的行数

# 应对 3
# 程序的流程无法得知
# 我们用 print 来追踪流程
# 用 print 来展现状态数据
#
# 不要用系统的 print 函数
# 用我们自己的包装，这样可以方便地改掉
# 我们在写代码的过程中，会多次使用 print 那么 debug 完成之后
# 每个 print 如果要手动删掉或者注释掉非常麻烦
# 用 log 的话，直接把 log 函数注释掉就可以了
