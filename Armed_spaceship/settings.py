# -*- coding: utf-8 -*-

class Settings():
    """一个储存游戏《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置￼
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230 , 230 , 230)
        
        #飞船的设置
        self.ship_speed_factor = 0.5  #飞船速度
        
        #子弹设置
        self.bullet_speed_factor = 1  #子弹速度
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60 , 60 , 60
        self.bullets_allowed = 1