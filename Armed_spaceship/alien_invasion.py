# -*- coding: utf-8 -*-

import random
import sys

sys.path.append("..")
import Create_alien.alien as Aliens
import game_functions as gf
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from props import Props


def run_game():
    # 初始化pygame,设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings. \
                                      screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于储存游戏的统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()
    props = Props(screen, ai_settings)

    # 创建外星人群
    # gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        # 创建一个外星人
        if len(aliens) <= 10:
            direction = random.choice([-1, 0, 1])  # 代表左，直， 右
            alien = Aliens.Alien_a(ai_settings, screen, direction)  # 初始化的时候随机给一个方向
            alien.initial_random_location()
            aliens.add(alien)

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # if stats.game_active:
        ship.update()
        gf.enlarge_bullet(props, bullets, ai_settings, ship)
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        props.update_props()
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, props)

        # 第一种子弹击中外星人函数
        # gf.Collision_detection(aliens, bullets)


run_game()
