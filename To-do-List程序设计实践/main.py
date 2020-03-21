import pygame
import sys
import traceback
from pygame.locals import *
import my_flower
import labels
import my_cat
pygame.init()   #pygame初始化
pygame.mixer.init()     #混音器初始化

#进行背景和标题的设置
bg_size = width , height = 900 , 675   #根据图片尺寸设置背景尺寸
screen = pygame.display.set_mode(bg_size)   
pygame.display.set_caption("To-do-list")    #设置标题
background = pygame.image.load("images/桌面.jpg")

#载入所有游戏背景音乐及音效音效
pygame.mixer.music.load("sounds/birds_background.mp3")
pygame.mixer.music.set_volume(0.2)

#加载所有花的图片
flower1_image = "images/花1.png"
flower2_image = "images/小房子.png"  #假设是第二朵花
flower2_copy =  pygame.image.load("images/小房子.png")
flower2_copy_rect = flower2_copy.get_rect() #选择主页面展示的花朵的界面里的花 
flower2_copy_rect.left , flower2_copy_rect.top = 150 ,150


#加载其他图片
#游戏图片
game_bg = pygame.image.load("images/rural.png").convert_alpha() #游戏界面的背景
#mouse_2 ="images/mouse_2.png" #光标样式
game_nor = pygame.image.load("images/游戏_默认.png").convert_alpha()
game = game_nor #初始化
game_click = pygame.image.load("images/游戏_点击.png").convert_alpha()
#计划图片
plan_nor = pygame.image.load("images/计划_默认.png").convert_alpha()
plan = plan_nor #初始化
plan_click = pygame.image.load("images/计划_点击.png").convert_alpha()
#商店图片
shop_nor = pygame.image.load("images/商店_默认.png").convert_alpha()
shop = shop_nor #初始化
shop_click = pygame.image.load("images/商店_点击.png").convert_alpha()
#仓库图片
stor_nor = pygame.image.load("images/仓库_默认.png").convert_alpha()
stor = stor_nor #初始化
stor_click = pygame.image.load("images/仓库_点击.png").convert_alpha()

#猫的图片
cat_image=[]    #1猫默认图标
for i in range(4):
    url = 'images/'+'cat_1'+str(i)+'.png'
    img=pygame.image.load(url).convert_alpha()
    cat_image.append(img)
cat_show = cat_image[0] #默认的猫的surfer对象
cat1_stand=[]   #1猫点击图标
for i in range(2):
    url = 'images/'+'cat1_stand_'+str(i)+'.png'
    img=pygame.image.load(url).convert_alpha()
    cat1_stand.append(img)

#其他图片
back = pygame.image.load("images/饲料.png").convert_alpha()
back_rect = back.get_rect()
back = pygame.image.load("images/饲料.png").convert_alpha()
back_rect = back.get_rect()
money = pygame.image.load("images/金币.png").convert_alpha()
water = pygame.image.load("images/水滴.png").convert_alpha()
sun = pygame.image.load("images/阳光.png").convert_alpha()
toy = pygame.image.load("images/玩具.png").convert_alpha()
fertilizer = pygame.image.load("images/肥料.png").convert_alpha()
ticket = pygame.image.load("images/入场券.png").convert_alpha()


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
location_game = game_left , game_top = 670 ,272
location_shop = plan_left , plan_top = 20 , 50
location_stor = stor_left , stor_top = 720 , 460

#设置猫的位置
location_cat = cat_left , cat_top = 400 , 395

#加载猫对象
cat = my_cat.Cat(cat_show , location_cat)

#加载标签对象
label_game = labels.Lable(game_nor ,location_game)
label_shop = labels.Lable(shop_nor ,location_shop)
label_stor = labels.Lable(stor_nor ,location_stor)
def main():
    location_plan = plan_left , plan_top = 800 ,460#因为之后要修改，所以放在main里定义
    choice = 0  #标志位，标识现在用户选择的是哪朵花
    background_control = 0  #默认为主屏幕 
    pygame.mixer.music.play(-1) #-1表示无限循环播放，此处为背景音乐
    tip=0   #设置猫的动图播放
    clock = pygame.time.Clock() 
    cat_act = False #判断是否执行动图 
    running = True
    while running:
        label_plan = labels.Lable(plan_nor ,location_plan)#因为涉及到坐标修改，所以放在后面定义
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
            elif event.type == MOUSEMOTION:
                if label_game.label_rect.collidepoint(event.pos):
                    game = game_click
                else:
                    game = game_nor
                if label_plan.label_rect.collidepoint(event.pos):
                    plan = plan_click
                    location_plan = plan_left , plan_top = 800 ,470
                else:
                    plan = plan_nor
                    location_plan = plan_left , plan_top = 800 ,460
                if label_shop.label_rect.collidepoint(event.pos):
                    shop = shop_click
                else:
                    shop = shop_nor
                if label_stor.label_rect.collidepoint(event.pos):
                    stor = stor_click
                else:
                    stor = stor_nor
                if cat.rect.collidepoint(event.pos):
                    cat_act = True
                else:
                   cat_act = False

            #让猫动起来
        while cat_act:
            tip=0
            for i in range(0,2):
                cat_show = cat1_stand[tip]
                screen.blit(cat_show, cat.rect)
                tip=(tip+1)%2
                time_passed = clock.tick(5)  
                pygame.display.flip()
                clock.tick(60)#设定帧率
                if i == 1:
                    i = 0
                if not cat_act:
                    break
            at_show = cat_image[0]
            break
        if not cat_act:
             cat_show = cat_image[0]
        
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
            screen.blit(game,label_game.label_rect)    #绘制游戏标签
            screen.blit(plan,label_plan.label_rect)    #绘制计划标签
            screen.blit(shop,label_shop.label_rect)    #绘制商店标签
            screen.blit(stor,label_stor.label_rect)    #绘制仓库标签
            screen.blit(money , (630 , 20))   #绘制金币显示 
            screen.blit(water , (530 , 20))   #绘制水滴显示 
            screen.blit(sun , (430 , 20))   #绘制阳光显示
            screen.blit(fertilizer , (330 , 20))   #绘制阳光显示
            screen.blit(cat_show, cat.rect)
            screen.blit(toy , (230 , 20))   #绘制玩具显示
            screen.blit(ticket , (130 , 20))   #绘制玩具显示
        if background_control == 1:
            screen.blit(game_bg , (0 , 0))
            screen.blit(back , (10 , 20))
            screen.blit(flower2.image , (150 , 150))
        pygame.display.flip()   #刷新画面，将内存画布反转到屏幕上
        
        clock.tick(240)#设定帧率
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()

