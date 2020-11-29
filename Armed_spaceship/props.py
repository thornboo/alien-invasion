# -*- coding: utf-8 -*-

import os
import pygame
import random


class Props():

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.dir_name = os.path.dirname(os.path.abspath(__file__))

        # 获取道具图像
        path = pygame.image.load(os.path.join(self.dir_name, "images", "props.bmp"))
        self.image = pygame.transform.scale(path, (20, 20))  # 道具图片的尺寸
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 初始化道具位置,在屏幕左上角
        self.rect.y = self.rect.height
        self.rect.x = self.screen_rect.centerx  # random.randint(0, 900)

        # 储存道具的准确位置
        self.y = float(self.rect.y)

    def update_props(self):
        """随机出现一个道具并向下移动道具"""
        self.y += 0.5
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制道具"""
        self.screen.blit(self.image, self.rect)
