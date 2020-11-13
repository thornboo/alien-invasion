# -*- coding: utf-8 -*-

class Settings():
    """一个储存游戏《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置￼
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230 , 230 , 230)
        
        #飞船设置
        self.ship_speed_factor = 0.5  #飞船速度
        
        #子弹设置
        self.bullet_speed_factor = 1  #子弹速度
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60 , 60 , 60 #子弹颜色
        self.bullets_allowed = 5  #子弹个数
        
        #外星人设置
        self.alien_speed_factor = 0.1 #外星人移动速度
        self.fleet_drop_speed = 10
        
        #fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1