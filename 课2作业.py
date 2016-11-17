# 作业 2 作业
#
#
import turtle

# 这是套路
t = turtle.Turtle()

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
colored_square(0, 0, 100, '#ff0000')




# 作业开始

# 1
# 实现一个矩形函数
# x y 是矩形左上角坐标
# w h 是宽高
# color 是矩形的颜色
# def rect(x, y, w, h, color)

# 2
# 实现一个矩形函数
# x y 是矩形中心的坐标
# w h 是宽高
# color 是矩形的颜色
# def center_rect(x, y, w, h, color)

# 3
# 实现一个圆形函数
# x y 是圆心坐标
# r 是半径
# color 是填充色
# def circle(x, y, r, color)
#
# 提示, 我们以正 36 形为圆

# 4
# 实现一个五角星函数
# x y 是五角星横边左边坐标
# length 是一条线的长度
# color 是填充色
# def wujcxy(x, y, length, color)

# 5
# 实现一个函数画日本国旗
# 调用 2 个函数画日本国旗
# 一个画背景的白色矩形
# 一个画中间的红色圆
# def japan()
#
# 注意, 你可以添加 x y w h 参数让国旗画在任意地方, 任意尺寸
# 注意, 以下所有国旗同理

# 6
# 实现一个函数画中国国旗(以下国旗题目都是如此 不重复了)
# 调用 2 个函数画中国国旗
# 一个画红色背景
# 另一个画五角星（调用 5 次，不要求角度朝向，只要5个五角星即可）
# def china()

# 7
# 实现一个函数画法国国旗
# def france()

# 8
# 画德国国旗
# def germany()

# 9
# 画 冈比亚国旗
# def gambia()

# 10
# 画 瑞士国旗
# def switzerland()

# 11
# 画朝鲜国旗
# 分别是 圆 矩形 五角星
# 提示, 使用之前定义的函数
# def northkorea()

# 12
# 画出美国国旗
# 美国国旗是 13 条横杠 加上 50 颗星星
#
# 这题做不出拉倒


# 画完后一定要加上这一句
# 这句在整个文件的最后面
turtle.done()
