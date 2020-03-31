import pygame

class User(pygame.sprite.Sprite):  #定义my_flower类，为用户自己的花朵初始化相关属性
    def __init__(self):  #location表示不同标签所在位置
        pygame.sprite.Sprite.__init__(self)
        #self.image = user_image    用户的图片
        #self.rect = self.image.get_rect()   #获取图像的限定矩形,即图片的位置
        #修改图片的位置
        #self.rect.left , self.rect.top = location[0] , location[1]
        self.rank = 0   #默认初始为0级
        self.level = [500 , 800 , 1200]  #三个等级
        self.title = ['防疫小白' , '防疫学徒' , '防疫大师']
        self.exp = 310 #默认初始经验值为0
        self.exp_scale = (self.exp/self.level[self.rank])*100    #绘制经验值的比例
        self.title_show = self.title[self.rank] #选择当前的称号