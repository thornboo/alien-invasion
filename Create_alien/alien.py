# -*- coding: utf-8 -*-
import os
import pygame
from pygame.sprite import Sprite

class Alien_a(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien_a, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.dir_name = os.path.dirname(os.path.abspath(__file__))

        #加载外星人图像，并设置其rect属性
        path = pygame.image.load(os.path.join(self.dir_name, "image", "alien.b\
                                              mp"))
        self.image = pygame.transform.scale(path, (20, 20))
        self.rect = self.image.get_rect()
    
        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
        #储存外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image , self.rect)
