# ball.py

import pygame
from Box2D import b2BodyDef, b2CircleShape, b2FixtureDef, b2_dynamicBody, b2Vec2
from settings import *

class Ball:
    """球类，用于创建和管理游戏中的球"""

    def __init__(self, world, game):
        """
        初始化球对象
        :param world: Box2D世界对象
        :param game: 游戏对象
        """
        self.world = world
        self.game = game
        self.create_ball()

    def create_ball(self):
        """创建球的物理体和形状"""
        # 创建刚体定义
        body_def = b2BodyDef()
        body_def.position = ((WIDTH / PPM) / 2, (HEIGHT / PPM) / 2)  # 设置初始位置为屏幕中心
        body_def.type = b2_dynamicBody  # 设置为动态体
        self.body = self.world.CreateBody(body_def)

        # 创建圆形形状
        circle = b2CircleShape(radius=BALL_RADIUS)
        
        # 创建夹具定义
        fixture_def = b2FixtureDef(
            shape=circle,
            density=1.0,  # 设置密度
            friction=BALL_FRICTION,  # 设置摩擦力
            restitution=1.0  # 设置弹性
        )
        
        # 将夹具添加到刚体
        self.body.CreateFixture(fixture_def)
        # 设置初始速度
        self.body.linearVelocity = (INITIAL_BALL_SPEED, 0)

    def update(self):
        """更新球的状态，检查是否有玩家得分"""
        position = self.body.position
        if position[0] < 0:
            # 球超出左边界，玩家2得分
            self.game.scores[2] += 1
            self.reset(-1)
        elif position[0] > WIDTH / PPM:
            # 球超出右边界，玩家1得分
            self.game.scores[1] += 1
            self.reset(1)

    def reset(self, direction):
        """
        重置球的位置和速度
        :param direction: 球的初始运动方向（1为向右，-1为向左）
        """
        self.body.position = ((WIDTH / PPM) / 2, (HEIGHT / PPM) / 2)  # 重置位置到屏幕中心
        self.body.linearVelocity = (INITIAL_BALL_SPEED * direction, 0)  # 设置初始速度

    def draw(self, screen):
        """
        在屏幕上绘制球
        :param screen: pygame屏幕对象
        """
        position = self.body.position
        pygame.draw.circle(
            screen,
            (255, 255, 255),  # 白色
            (int(position[0] * PPM), int(HEIGHT - position[1] * PPM)),  # 转换Box2D坐标到pygame坐标
            int(BALL_RADIUS * PPM)  # 转换半径到像素
        )

    def apply_hit_force(self, direction):
        """
        对球施加击打力
        :param direction: 力的方向
        """
        # 根据方向给球施加力
        force = b2Vec2(*direction) * HIT_FORCE
        self.body.ApplyForce(force, self.body.worldCenter, True)