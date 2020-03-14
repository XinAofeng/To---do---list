import pygame

class Flower(pygame.sprite.Sprite):  #定义my_flower类，为用户自己的花朵初始化相关属性
    sun = 100
    water = 100
    fertilizer = 100
    def __init__(self , flower_image , bg_size , speed):    #speed指代花朵各项属性减少速度 
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load(flower_image).convert_alpha()
        self.rect = self.image.get_rect()   #获取图像的限定矩形,即图片的位置
        #修改图片的位置
        self.rect.left , self.rect.top = (bg_size[0] - self.rect.width)//2 , bg_size[1] - self.rect.height - 40
        self.sun_speed = speed[0]
        self.water_speed = speed[1]
        self.fertilizer_speed = speed[2]
        
        #初始化各个属性的初值
        self.sun = Flower.sun
        self.water = Flower.water
        self.fertilizer = Flower.fertilizer
        
        #初始化各个属性剩余的百分比
        self.sun_remain = 1
        self.water_remain = 1
        self.fertilizer_remain = 1
        self.health_remain = 1
    def life(self): #计算四个属性条，健康，阳光，水分，肥料
        #if 浇水or施肥or...
        #else：
        self.sun -= 1*self.sun_speed    #此处的数字均应为记录的时间，即记录每过1h，减少多少
        self.water -= 2*self.water_speed
        self.fertilizer -= 3*self.fertilizer_speed

       



    #def click_flower():   #点击花朵，则弹出列表，显示所有花朵种类