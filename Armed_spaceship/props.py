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
        self.image = pygame.transform.scale(path, (10, 10))  # 道具图片的尺寸
        self.rect = self.image.get_rect()

        # 初始化道具位置,在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update_props(self):
        """随机出现一个道具并向下移动道具"""
        self.rect.x += random.randint(0, 900)
        self.rect.y += 0.1

    def enlarge_bullet(self, ship, bullets):
        """如果飞船吃到道具就把子弹放大一倍"""
        if self.rect.y >= self.ai_settings.screen_height:
            if self.rect.x == ship.rect.centerx:
                bullets.radius = bullets.radius * 2
