# -*- coding: utf-8 -*-
import os
import random

import pygame
from pygame.sprite import Sprite


class Props(Sprite):
    prop_num = 0

    def __init__(self, ai_settings, screen):
        super(Props, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.dir_name = os.path.dirname(os.path.abspath(__file__))

        # 飞船图像并获取其外接矩形
        path = pygame.image.load(os.path.join(self.dir_name, "images", "G.png"))
        self.image = pygame.transform.scale(path, (20, 20))  # 飞船图片的尺寸
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = random.randint(0, ai_settings.screen_width)
        self.rect.y = 0
        self.y = float(self.rect.y)

        # 在飞船的属性center中储存小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        # self.moving_right = False
        # self.moving_left = False

    def update(self):
        """根据移动标志调整位置"""
        # 更新飞船的center值，而不是rect
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        #     self.center += self.ai_settings.ship_speed_factor
        # if self.moving_left and self.rect.left > 0:
        #     self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.y += 0.1
        self.rect.y = self.y
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """屏幕上居中"""
        self.center = self.screen_rect.centerx
