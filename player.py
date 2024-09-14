# player.py

import pygame
from Box2D import b2BodyDef, b2PolygonShape, b2FixtureDef, b2_kinematicBody
from settings import *

class Player:
    """玩家类，用于创建和管理游戏中的球拍"""

    def __init__(self, world, player_number):
        """
        初始化玩家对象
        :param world: Box2D世界对象
        :param player_number: 玩家编号（1或2）
        """
        self.world = world  # 存储Box2D世界对象
        self.player_number = player_number  # 存储玩家编号
        self.create_paddle()  # 创建球拍

    def create_paddle(self):
        """创建球拍的物理体和形状"""
        body_def = b2BodyDef()  # 创建刚体定义
        body_def.position = (PADDLE_START_X[self.player_number], (HEIGHT / PPM) / 2)  # 设置球拍初始位置
        body_def.type = b2_kinematicBody  # 设置为运动学刚体
        self.body = self.world.CreateBody(body_def)  # 在物理世界中创建刚体
        
        box = b2PolygonShape(box=(PADDLE_WIDTH / 2, PADDLE_HEIGHT / 2))  # 创建矩形形状
        
        fixture_def = b2FixtureDef(  # 创建夹具定义
            shape=box,
            density=1.0,  # 设置密度
            friction=PADDLE_FRICTION,  # 设置摩擦力
            restitution=1.0  # 设置弹性
        )
        
        self.body.CreateFixture(fixture_def)  # 将夹具添加到刚体

    def update(self, keys):
        """
        更新球拍位置
        :param keys: 按键状态
        """
        velocity = 0  # 初始化速度为0
        if self.player_number == 1:  # 玩家1的控制
            if keys[pygame.K_w]:  # 如果按下W键
                velocity = PADDLE_SPEED  # 向上移动
            elif keys[pygame.K_s]:  # 如果按下S键
                velocity = -PADDLE_SPEED  # 向下移动
        elif self.player_number == 2:  # 玩家2的控制
            if keys[pygame.K_UP]:  # 如果按下上箭头键
                velocity = PADDLE_SPEED  # 向上移动
            elif keys[pygame.K_DOWN]:  # 如果按下下箭头键
                velocity = -PADDLE_SPEED  # 向下移动
        self.body.linearVelocity = (0, velocity)  # 设置球拍的线性速度

    def draw(self, screen):
        """
        在屏幕上绘制球拍
        :param screen: Pygame屏幕对象
        """
        # 获取球拍的顶点并转换为屏幕坐标
        vertices = [(self.body.transform * v) * PPM for v in self.body.fixtures[0].shape.vertices]
        vertices = [(v[0], HEIGHT - v[1]) for v in vertices]  # 处理Y轴方向（Pygame坐标系与Box2D不同）

        pygame.draw.polygon(screen, (255, 255, 255), vertices)  # 绘制白色多边形表示球拍