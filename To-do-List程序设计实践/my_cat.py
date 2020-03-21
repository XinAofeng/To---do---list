import pygame

class Cat(pygame.sprite.Sprite):  #定义my_flower类，为用户自己的花朵初始化相关属性
    def __init__(self , cat_image , location):  #location表示不同标签所在位置
        pygame.sprite.Sprite.__init__(self)
        self.image = cat_image
        self.rect = self.image.get_rect()   #获取图像的限定矩形,即图片的位置
        #修改图片的位置
        self.rect.left , self.rect.top = location[0] , location[1]