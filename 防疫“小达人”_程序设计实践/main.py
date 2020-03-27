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
Screen = pygame.display.set_mode(bg_size , 0 , 32)  
pygame.display.set_caption("To-do-list")    #设置标题
background = pygame.image.load("images/桌面.jpg")
game_bg = pygame.image.load("images/rural.png").convert_alpha() #第二个游戏界面的背景

#载入所有游戏背景音乐及音效音效
pygame.mixer.music.load("sounds/birds_background.mp3")
pygame.mixer.music.set_volume(0.2)

#加载所有花的图片
flower1 = pygame.image.load("images/花1.png").convert_alpha()
flower2 = pygame.image.load("images/小房子.png").convert_alpha()
flower2_copy =  pygame.image.load("images/小房子.png").convert_alpha()
flower2_copy_rect = flower2_copy.get_rect() #选择主页面展示的花朵的界面里的花 
flower2_copy_rect.left , flower2_copy_rect.top = 150 ,150


#游戏图片
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
cat1_stand=[]   #1猫点击图标
for i in range(4):
    url = 'images/'+'cat1_stand_'+str(i)+'.png'
    img=pygame.image.load(url).convert_alpha()
    cat1_stand.append(img)

#返回图标
back_nor = pygame.image.load("images/返回_默认.png").convert_alpha()
back = back_nor
back_click = pygame.image.load("images/返回_点击.png").convert_alpha()
back_rect = back_nor.get_rect()
back_rect.left , back_rect.top = 10 , 20
#“疫情速览”
words_nor = pygame.image.load("images/疫情速览_默认.png").convert_alpha()
words = words_nor
words_click = pygame.image.load("images/疫情速览_点击.png").convert_alpha()
words_rect = words_nor.get_rect()
words_rect.left , words_rect.top = 140 , 250
board = pygame.image.load("images/木板.png").convert_alpha()
#主界面右上角的属性图标
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

#加载需要花的对象
my_gardan = []  #存放所有花的对象
Flower1 = my_flower.Flower(flower1 , bg_size)
Flower2 = my_flower.Flower(flower2 , bg_size)
my_gardan.append(Flower1)
my_gardan.append(Flower2)

#设置标签位置
location_game = game_left , game_top = 670 ,272
location_shop = plan_left , plan_top = 20 , 50
location_stor = stor_left , stor_top = 720 , 460


#加载标签对象
label_game = labels.Lable(game_nor ,location_game)
label_shop = labels.Lable(shop_nor ,location_shop)
label_stor = labels.Lable(stor_nor ,location_stor)
def main(): 
    screen = Screen 
    location_plan = plan_left , plan_top = 800 ,460#因为之后要修改，所以放在main里定义
    location_cat = cat_left , cat_top = 400 , 395 #设置猫的位置,因为之后要修改，所以放在main里定义
    choice = 0  #标志位，标识现在用户选择的是哪朵花
    background_control = 0  #默认为主屏幕 
    pygame.mixer.music.play(-1) #-1表示无限循环播放，此处为背景音乐
    clock = pygame.time.Clock() 
    cat_act = False #判断是否执行动图 
    running = True
    fullscreen=False    #控制是否全屏
    while running:
        label_plan = labels.Lable(plan_nor ,location_plan)#因为涉及到坐标修改，所以放在后面定义
        cat = my_cat.Cat(cat_image[0] , location_cat)#加载猫对象,因为涉及到坐标修改，所以放在后面定义
        for event in pygame.event.get():
            if event.type == QUIT:  #用户点击差差推出程序
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    fullscreen=not fullscreen
                    if fullscreen:
                        screen=pygame.display.set_mode(bg_size , FULLSCREEN , 32)
                    else:
                        screen=pygame.display.set_mode(bg_size,0,32)
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
                if back_rect.collidepoint(event.pos):
                    back = back_click
                else:
                    back = back_nor
                if words_rect.collidepoint(event.pos):
                    words = words_click
                else:
                    words = words_nor
            #让猫动起来
            
    
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
            screen.blit(toy , (230 , 20))   #绘制玩具显示
            screen.blit(ticket , (130 , 20))   #绘制玩具显示
            screen.blit(board , (70 , 80))   #绘制公告栏显示
            screen.blit(words , (135 , 245))#加载文字
            if not cat_act:
                screen.blit(cat_image[0], (400 , 435))
        if background_control == 1:
            screen.blit(game_bg , (0 , 0))
            screen.blit(back , (10 , 20))
            screen.blit(flower2_copy , (150 , 150))


        pygame.display.flip()   #刷新画面，将内存画布反转到屏幕上
        clock.tick(240)#设定帧率
        if cat_act:
            tip=0   #设置猫的动图播放 
            for i in range(0,4):
                screen.blit(cat1_stand[tip], (400 , 386))
                pygame.display.update()
                tip=(tip+1)%4
                time_passed = clock.tick(3) 
        
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()

