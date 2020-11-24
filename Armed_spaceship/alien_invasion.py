# -*- coding: utf-8 -*-

import sys

sys.path.append("..")
import Create_alien.alien as Aliens

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame,设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings. \
                                      screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # 创建外星人群
    # gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        # 创建一个外星人
        if len(aliens) <= 10:
            alien = Aliens.Alien_a(ai_settings, screen)
            alien.initial_random_location()
            aliens.add(alien)

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # 第一种子弹击中外星人函数
        gf.collision_detection(aliens, bullets)


run_game()
