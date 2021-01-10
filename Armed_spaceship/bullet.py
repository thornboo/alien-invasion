# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship, radius=5):
        """在飞船位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen
        # 在（0，0）创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.radius = radius
        self.radius_max = self.radius * 2

        # 存储用小数表示的子弹位置
        self.x = int(self.rect.x)
        self.y = int(self.rect.y)
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹的位置的小数值
        self.y -= self.speed_factor
        # self.x -= self.speed_factor   #子弹斜飞
        # 更新表示子弹rect位置
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self, ai_settings, screen):
        """在屏幕上绘制子弹"""
        if self.radius >= self.radius_max:
            self.radius = self.radius_max
        pygame.draw.circle(screen, ai_settings.bullet_color, [self.x, self.y], self.radius, 0)
