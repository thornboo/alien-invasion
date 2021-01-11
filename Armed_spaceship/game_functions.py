# -*- coding: utf-8 -*-

import sys
import pygame
import random

sys.path.append("..")
import Create_alien.alien as Aliens
from bullet import Bullet
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就继续发射子弹"""
    # 创建新子弹,并将其加入到bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应按键松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, direction):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y,
                              direction)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, direction):
    """在玩家单击Play按钮时开始新游戏"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        # 重置游戏信息
        stats.reset_stats()
        stats.game_active = True

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens, direction)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, props, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets:
        bullet.draw_bullet(ai_settings, screen)
    ship.blitme()
    aliens.draw(screen)
    props.blitme()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    # 检查是否有子弹击中外星人
    # 如果有，就删除相应的子弹和外星人
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """第二种、响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def collision_detection(aliens, bullets):
    """第一种、检测子弹是否击中外星人，若击中则删除外星人和子弹"""
    for alien in aliens:
        for bullet in bullets:
            if alien.rect.x < bullet.x < alien.rect.x + alien.rect.width:
                if alien.rect.y < bullet.y < alien.rect.y + alien.rect.height:
                    aliens.remove(alien)
                    bullets.remove(bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可以容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可以容纳多少个外星人"""
    available_space_y = (ai_settings.screen_height - (2 * alien_height) - \
                         ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number, direction):
    """创建一个外星人并将其放在当前行"""
    alien = Aliens.Alien_a(ai_settings, screen, direction)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number  # 外星人垂直间距
    i = random.randint(0, 100)
    if i % 2 == 0:
        aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens, direction):
    """创建外星人群"""
    # 创建一个外星人，获得单个外星人的宽度和高度；并计算一行可以容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Aliens.Alien_a(ai_settings, screen, direction)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect. \
                                  height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number, direction)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变他们方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边缘，并更新所有外星人的位置"""

    for alien in aliens:
        if alien.check_edges():
            alien.direction *= -1
        alien.random_move()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 1:
        # 将ship_left(玩家生命值)减1
        stats.ships_left -= 1

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 清除子弹变大特效
        ai_settings.prop_switch = False

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        ship.center_ship()

        # 暂停一段时间
        sleep(0.5)

    else:
        stats.game_active = False


def enlarge_bullet(props, bullets, ai_settings, ship):
    """如果飞船吃到道具就把子弹放大一倍,且删除道具释放内存"""
    if pygame.sprite.collide_rect(ship, props):
        ai_settings.prop_switch = True
    if ai_settings.prop_switch:
        for bullet in bullets:
            bullet.radius = bullet.radius * 2
    if props.rect.y > ai_settings.screen_height:
        del props
