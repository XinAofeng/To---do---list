#2020.3.12 18：30-20：45    初始化程序，打印音效，背景，花朵，尝试修图  2020.3.13 18：21 -22：19  绘制标签 ，修改鼠标
#2020.3.14 8：41 -  9：20   10:20 - 11:13 花朵各种属性绘制以及动态减少实现

import pygame
import sys
import traceback
from pygame.locals import *
import my_flower
import labels


pygame.init()   #pygame初始化
pygame.mixer.init()     #混音器初始化

#进行背景和标题的设置
bg_size = width , height = 1080 , 608   #根据图片尺寸设置背景尺寸
screen = pygame.display.set_mode(bg_size)   
pygame.display.set_caption("To-do-list")    #设置标题
background = pygame.image.load("images/river.png")

#载入所有游戏背景音乐及音效音效
pygame.mixer.music.load("sounds/birds_background.mp3")
pygame.mixer.music.set_volume(0.2)

#加载所有花的图片
flower1_image = "images/flower_1.png"
flower2_image = "images/小房子.png"  #假设是第二朵花
flower2_copy =  pygame.image.load("images/小房子.png")
flower2_copy_rect = flower2_copy.get_rect() #选择主页面展示的花朵的界面里的花 

#加载其他图片
image_game = "images/game.png"  #主界面 游戏 标签
#mouse_2 ="images/mouse_2.png" #光标样式
game_image = pygame.image.load("images/rural.png")
back = pygame.image.load("images/饲料.png").convert_alpha()
back_rect = back.get_rect()
back = pygame.image.load("images/饲料.png").convert_alpha()
back_rect = back.get_rect()

#定义各种颜色
black = (0 , 0 , 0)
red = (255 , 0 ,0)
green = (0 , 255 , 0)
#设置不同花朵减少速度的属性值
all_speed = []  #用于存放所有花朵的三个减缓速度
speed1 =  [0.5 , 1.5 , 0.2]  #第一个花的阳光，水分，肥料的减缓速度 ， 健康值由这三项指标共同决定,减少速度均已小时计算
all_speed.append(speed1)

#加载需要花的对象
my_gardan = []  #存放所有花的对象
flower1 = my_flower.Flower(flower1_image , bg_size , all_speed[0])
flower2 = my_flower.Flower(flower2_image , bg_size , all_speed[0])
my_gardan.append(flower1)
my_gardan.append(flower2)
#设置标签位置
location_game = game_left , game_top = 30 ,50

#加载标签对象
label_game = labels.Lable(image_game ,location_game)

def main():
    choice = 0  #标志位，标识现在用户选择的是哪朵花
    background_control = 0  #默认为主屏幕   
    pygame.mixer.music.play(-1) #-1表示无限循环播放，此处为背景音乐
    clock = pygame.time.Clock() 
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:  #用户点击差差推出程序
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and label_game.label_rect.collidepoint(event.pos):
                    background_control = 1
                if event.button == 1 and back_rect.collidepoint(event.pos):
                    background_control = 0
                if event.button == 1 and flower2_copy_rect.collidepoint(event.pos):
                    choice = 1  #可以再补充确认键
        health_remain = my_gardan[choice].life()
        pygame.draw.line(screen , black , (my_gardan[choice].rect.left , my_gardan[choice].rect.top - 20),\
            (my_gardan[choice].rect.right , my_gardan[choice].rect.top - 20), 4)
        if health_remain > 0.2:   #健康值大于0.2，则为绿色
            health_color = green
        else:
            health_color = red
        pygame.draw.line(screen , health_color , (my_gardan[choice].rect.left , my_gardan[choice].rect.top - 20),\
            (my_gardan[choice].rect.left + my_gardan[choice].rect.width * health_remain, my_gardan[choice].rect.top - 20) , 4)
    
        if background_control == 0:
            screen.blit(background , (0 , 0))   #绘制背景，后画的会覆盖先画的
            screen.blit(my_gardan[choice].image , my_gardan[choice].rect) #绘制花朵
            screen.blit(label_game.label ,label_game.label_rect)    #绘制主界面标签
        if background_control == 1:
            screen.blit(game_image , (0 , 0))
            screen.blit(back , (10 , 20))
            screen.blit(flower2.image , (150 , 150))
        pygame.display.flip()   #刷新画面，将内存画布反转到屏幕上
        
        clock.tick(120)#设定帧率
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()

