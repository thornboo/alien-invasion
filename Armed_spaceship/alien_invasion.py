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
    #初始化pygame,设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width ,  ai_settings.\
                                      screen_height ))
    pygame.display.set_caption( "Alien Invasion" )
    
    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship( ai_settings, screen )
    bullets = Group()
    aliens = Group()
    
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
        
    #创建一个用于存储子弹的编组
    bullets = Group()
    
    #创建一行外星人
    alien = Aliens.Alien_a(ai_settings , screen)
    
    #开始游戏主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings , screen , ship , bullets )
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings , screen , ship , aliens , bullets )

run_game()
        