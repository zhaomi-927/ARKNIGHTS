# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
auto_setup(__file__)
#全自动搓玉
def panduanguoguan():#判断过关
    while not exists(Template(r"tpl1643114966021.png", record_pos=(-0.334, 0.208), resolution=(1440, 810))):#判断过关
        sleep(4.0)#没有成功通过就等4秒，然后继续循环找成功通过
    else:
        sleep(4.0)#找到了之后，为了防止在字从画面左边飞到画面内的瞬间识别到并立刻进行点击而设置的一个等待时间。（因为计算机执行）
    touch(Template(r"tpl1643114966021.png", record_pos=(-0.334, 0.208), resolution=(1440, 810)))#识别到了点击一下
    sleep(2.0)
    kaishixingdong()
        
def kaishi():#开始
    touch((1100,200))#在主界面开始
    sleep(2.0)
    touch((250,740))
    sleep(1.0)
    touch((250,200))
    sleep(1.0)
    touch((250,200))
    sleep(1.0)
    touch((400,400))
    sleep(1.0)
    panduanguanqia()
    
def panduanguanqia():#判断关卡
    sleep(2.0)
    
    while not exists(Template(r"tpl1642525359824.png", record_pos=(-0.012, -0.11), resolution=(1440, 810))):#判断有没有这个图片
        swipe((670,500),vector=[-0.1,0])#判断没有，就自右往左滑动屏幕，移到右边，移完回去继续判断图片
    else:
        sleep(1.0)
        touch(Template(r"tpl1642525017627.png", record_pos=(-0.009, -0.112), resolution=(1440, 810)))#判断到了就点它
        sleep(1.0)
        kaishixingdong()
    
def kaishixingdong():#开始行动
    while not exists(Template(r"tpl1643114312762.png", record_pos=(0.393, 0.182), resolution=(1440, 810))):#判断有没有这个图片
        touch(Template(r"tpl1642516830543.png", record_pos=(0.417, 0.229), resolution=(1440, 810)))
        sleep(2.0)
        tilipanduan()
    else:
        sleep(1.0)
        touch(Template(r"tpl1643114346374.png", record_pos=(0.392, 0.181), resolution=(1440, 810)))
        touch(Template(r"tpl1642516830543.png", record_pos=(0.417, 0.229), resolution=(1440, 810)))
        sleep(2.0)
        tilipanduan()

def tilipanduan():#体力判断
    while not exists(Template(r"tpl1642517328915.png", record_pos=(0.362, 0.114), resolution=(1440, 810))):#判断有没有这个图片
        touch(Template(r"tpl1642520686454.png", record_pos=(0.11, 0.169), resolution=(1440, 810)))#判断没有，就关掉弹窗
        sleep(1.0)
        jijian()#基建
    else:
        touch(Template(r"tpl1642517328915.png", record_pos=(0.362, 0.114), resolution=(1440, 810)))#再点一次开始
        sleep(15.0)
        panduanguoguan()#判断过关
        
def jijian():#基建
        touch(Template(r"tpl1642591510628.png", record_pos=(-0.292, -0.251), resolution=(1440, 810)))
        sleep(1.0)
        touch(Template(r"tpl1642591571242.png", record_pos=(0.033, -0.218), resolution=(1440, 810)))
        sleep(10.0)
        shoucaipanduan()
        
def shoucaipanduan():#收菜判断
        while not exists(Template(r"tpl1642591865312.png", record_pos=(0.442, -0.209), resolution=(1440, 810))):#判断有没有这个图片
            sleep(1.0)
            fanhui()#返回
        else:
            touch(Template(r"tpl1642591865312.png", record_pos=(0.442, -0.209), resolution=(1440, 810)))#收菜
            sleep(1.5)
            shoucai()
            
def shoucai():#收菜
    touch((250,790))
    sleep(1.0)
    touch((250,790))
    sleep(1.0)
    touch((250,790))
    sleep(1.0)
    touch((250,790))
    sleep(1.0)
    while not exists(Template(r"tpl1642677481067.png", record_pos=(-0.319, 0.26), resolution=(1440, 810))):#判断有没有这个图片
            sleep(1.0)
            fanhui()#返回
    else:
        touch((200,650))
        sleep(1.0)
        touch(Template(r"tpl1642677845949.png", record_pos=(-0.371, -0.035), resolution=(1440, 810)))
        sleep(1.5)
        touch(Template(r"tpl1642677899425.png", record_pos=(-0.098, 0.208), resolution=(1440, 810)))
        zhandianpanduan1()
        
def fanhui2():#点2次返回
    sleep(1.0)
    touch(Template(r"tpl1642591968805.png", record_pos=(-0.464, -0.254), resolution=(1440, 810)))
    sleep(2.0)
    touch(Template(r"tpl1642591968805.png", record_pos=(-0.464, -0.254), resolution=(1440, 810)))
    sleep(2.0)
        
def zhandianpanduan1():#站点判断1
    while not exists(Template(r"tpl1642678269046.png", record_pos=(-0.168, 0.253), resolution=(1440, 810))):#判断有没有这个图片
        sleep(1.0)
        zhandianpanduan2()
    else:
        huanren()
        zhandianpanduan2()
        

def zhandianpanduan2():#站点判断2
    touch(Template(r"tpl1642678329288.png", record_pos=(-0.471, -0.053), resolution=(1440, 810)))
    sleep(1.0)
    while not exists(Template(r"tpl1642678269046.png", record_pos=(-0.168, 0.253), resolution=(1440, 810))):#判断有没有这个图片
        sleep(1.0)
        zhandianpanduan31()
    else:
        huanren()
        zhandianpanduan31()
def zhandianpanduan31():#站点判断3.1
    while not exists(Template(r"tpl1642679198875.png", record_pos=(-0.472, 0.011), resolution=(1440, 810))):#判断有没有这个图片
        fanhui2()
        zhizaozhan()
    else:
        touch(Template(r"tpl1642679198875.png", record_pos=(-0.472, 0.011), resolution=(1440, 810)))
        while not exists(Template(r"tpl1642678269046.png", record_pos=(-0.168, 0.253), resolution=(1440, 810))):#判断有没有这个图片
            fanhui2()
            zhizaozhan()
        else:
            huanren()
            fanhui2()
            zhizaozhan()
def zhandianpanduan12():#站点判断1.2
    while not exists(Template(r"tpl1642678269046.png", record_pos=(-0.168, 0.253), resolution=(1440, 810))):#判断有没有这个图片
        sleep(1.0)
        zhandianpanduan22()
    else:
        huanren()
        zhandianpanduan22()
        

def zhandianpanduan22():#站点判断2.2
    touch(Template(r"tpl1642678329288.png", record_pos=(-0.471, -0.053), resolution=(1440, 810)))
    sleep(1.0)
    while not exists(Template(r"tpl1642678269046.png", record_pos=(-0.168, 0.253), resolution=(1440, 810))):#判断有没有这个图片
        sleep(1.0)
        zhandianpanduan32()
    else:
        huanren()
        zhandianpanduan32()
def zhandianpanduan32():#站点判断3.2
    while not exists(Template(r"tpl1642679198875.png", record_pos=(-0.472, 0.011), resolution=(1440, 810))):#判断有没有这个图片
        fanhui2()
        fanhui()
    else:
        touch(Template(r"tpl1642679198875.png", record_pos=(-0.472, 0.011), resolution=(1440, 810)))
        while not exists(Template(r"tpl1642678269046.png", record_pos=(-0.168, 0.253), resolution=(1440, 810))):#判断有没有这个图片
            zhandianpanduan42()
        else:
            huanren()
            zhandianpanduan42()
            
def zhandianpanduan42():#站点判断4.2
    while not exists(Template(r"tpl1642736950402.png", record_pos=(-0.473, 0.075), resolution=(1440, 810))):#判断有没有这个图片
        fanhui2()
        fanhui()
    else:
        touch(Template(r"tpl1642736950402.png", record_pos=(-0.473, 0.075), resolution=(1440, 810)))
        while not exists(Template(r"tpl1642678269046.png", record_pos=(-0.168, 0.253), resolution=(1440, 810))):#判断有没有这个图片
            fanhui2()
            fanhui()
        else:
            huanren()
            fanhui2()
            fanhui()
def zhizaozhan():#制造站
            touch(Template(r"tpl1642679918187.png", record_pos=(-0.328, -0.049), resolution=(1440, 810)))
            sleep(1.5)
            touch(Template(r"tpl1642679962332.png", record_pos=(-0.123, 0.209), resolution=(1440, 810)))
            sleep(1.0)
            zhandianpanduan12()
            fanhui()

def huanren():#换人
            touch((400,700))
            sleep(1.5)
            touch(Template(r"tpl1642678805104.png", record_pos=(-0.106, 0.248), resolution=(1440, 810)))
            sleep(0.5)
            touch((700,500))
            sleep(0.5)
            touch((850,500))
            sleep(0.5)
            touch((850,250))
            sleep(0.5)
            touch(Template(r"tpl1642679079982.png", record_pos=(0.421, 0.247), resolution=(1440, 810)))
            

            
def fanhui():#返回
            touch(Template(r"tpl1642591968805.png", record_pos=(-0.464, -0.254), resolution=(1440, 810)))#若没有则返回主菜单
            sleep(1.0)
            touch(Template(r"tpl1642591989843.png", record_pos=(0.156, 0.105), resolution=(1440, 810)))
            sleep(5.0)
            jijianfangwen()
            sleep(5.0)
            kaishi()
def jijianfangwen():#基建访问
    touch(Template(r"tpl1643031147259.png", record_pos=(-0.222, 0.167), resolution=(1440, 810)))
    sleep(2.0)
    touch(Template(r"tpl1643031173088.png", record_pos=(-0.41, -0.11), resolution=(1440, 810)))
    sleep(2.0)
    touch(Template(r"tpl1643031430047.png", record_pos=(0.281, -0.156), resolution=(1440, 810)))
    sleep(5.0)
    touch((1350,700))#1
    sleep(5.0)
    touch((1350,700))#2
    sleep(5.0)
    touch((1350,700))#3
    sleep(5.0)
    touch((1350,700))#4
    sleep(5.0)
    touch((1350,700))#5
    sleep(5.0)
    touch((1350,700))#6
    sleep(5.0)
    touch((1350,700))#7
    sleep(5.0)
    touch((1350,700))#8
    sleep(5.0)
    touch((1350,700))#9
    sleep(5.0)
    touch((1350,700))#10
    sleep(5.0)
    touch(Template(r"tpl1643032254607.png", record_pos=(-0.293, -0.253), resolution=(1440, 810)))
    sleep(2.0)
    touch(Template(r"tpl1643032288004.png", record_pos=(-0.426, -0.076), resolution=(1440, 810)))


kaishi()#脚本从这里开始运行
