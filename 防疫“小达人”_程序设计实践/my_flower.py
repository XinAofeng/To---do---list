import pygame

class Flower(pygame.sprite.Sprite):  #定义my_flower类，为用户自己的花朵初始化相关属性
    def __init__(self , flower , bg_size ):    #speed指代花朵各项属性减少速度 
        pygame.sprite.Sprite.__init__(self)

        self.image = flower
        self.rect = self.image.get_rect()   #获取图像的限定矩形,即图片的位置
        #修改图片的位置
        self.rect.left , self.rect.top = 50 , 395
        