import pygame
import time
import sys
pygame.init()
clock = pygame.time.Clock() 
window = pygame.display.set_mode([1000, 1000])
# 设置窗口标题
pygame.display.set_caption("猫咪咪")
imglst=[]
for i in range(4):
    img=pygame.image.load('images/'+'xixi'+str(i)+'.png').convert_alpha()
    imglst.append(img)
while True:
    tip=0
    for i in range(0,4):
        window.blit(imglst[tip], (0, 0))
        tip=(tip+1)%4
        time_passed = clock.tick(5)  
        pygame.display.update()
        for event in pygame.event.get():   # 遍历所有事件
            if event.type==pygame.QUIT:   # 如果单继关闭窗口，则退出
                sys.exit()
pygame.exit()