# -*- coding: utf-8 -*-
import os
import pygame

import random
from pygame.sprite import Sprite


class Alien_a(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen, direction):
        """初始化外星人并设置其起始位置"""
        super(Alien_a, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.dir_name = os.path.dirname(os.path.abspath(__file__))
        path = pygame.image.load(os.path.join(self.dir_name, "image", "alien.bmp"))
        self.image = pygame.transform.scale(path, (20, 20))
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 标记
        self.mark = ""
        self.direction = direction

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    # def update(self):
    #     """"向左或向右移动外星人"""
    #     self.x += (self.ai_settings.alien_speed_factor * self.ai_settings. \
    #                fleet_direction)
    #     self.dir_name = os.path.dirname(os.path.abspath(__file__))
    #
    #     # 加载外星人图像，并设置其rect属性
    #     self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕便边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def random_move(self):
        self.y += self.ai_settings.alien_speed_factor * 1
        self.x += self.direction * self.ai_settings.alien_speed_factor
        self.rect.x = self.x
        self.rect.y = self.y

    def random_move_down(self):
        self.y += self.ai_settings.alien_speed_factor * 1
        self.rect.y = self.y

    def random_move_left(self):
        self.y += self.ai_settings.alien_speed_factor * 1
        self.x -= 0.1
        self.rect.x = self.x
        self.rect.y = self.y

    def random_move_right(self):
        self.y += self.ai_settings.alien_speed_factor * 1
        self.x += 0.1
        self.rect.x = self.x
        self.rect.y = self.y

    def check_bottom(self):
        """检查是否有外星人到达底部"""
        if self.y >= self.ai_settings.screen_height:
            return True

    def initial_random_location(self):
        """生成随机位置的外星人"""
        initial_x = random.randint(0, self.ai_settings.screen_width - self.rect.width)
        initial_y = 0
        self.x = initial_x
        self.rect.x = self.x
        self.rect.y = initial_y
