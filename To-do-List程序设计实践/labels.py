import pygame

class Lable(pygame.sprite.Sprite):  #定义my_flower类，为用户自己的花朵初始化相关属性
    def __init__(self , label_image , mouse_image , location):  #location表示不同标签所在位置
        pygame.sprite.Sprite.__init__(self)


        self.label = pygame.image.load(label_image).convert_alpha()
        self.label_rect = self.label.get_rect()   #获取图像的限定矩形,即图片的位置
        #修改图片的位置
        self.label_rect.left , self.label_rect.top = location[0] , location[1]

        self.mouse = pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect = self.mouse.get_rect()   #获取图像的限定矩形,即图片的位置
        self.mouse_rect.left , self.mouse_rect.top = self.label_rect.left , self.label_rect.top

    #屏幕的上下左右就是图片的上下左右，画布坐标系以电脑屏幕左上角为圆心
    def check_location(self):    #判断光标是否在当前标签内部，如果在，就修改鼠标样式，数字是根据图片尺寸进行的调整
        if self.mouse_rect.left > self.label_rect.left + 10 \
            and self.mouse_rect.left < self.label_rect.right - self.mouse_rect.width - 10\
            and self.mouse_rect.top > self.label_rect.top + 100\
            and self.mouse_rect.top < self.label_rect.bottom - self.mouse_rect.height - 100:
            return True
