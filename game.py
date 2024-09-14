# game.py

import pygame  # 导入pygame库，用于游戏开发
from Box2D import b2World, b2PolygonShape, b2Vec2  # 从Box2D导入物理引擎相关类
from player import Player  # 导入Player类
from ball import Ball  # 导入Ball类
from settings import *  # 导入所有设置

class Game:
    """游戏主类，管理游戏逻辑和对象"""

    def __init__(self):
        """
        初始化游戏
        """
        self.world = b2World(gravity=(0, 0), doSleep=True)  # 创建物理世界，无重力
        self.players = [Player(self.world, 1), Player(self.world, 2)]  # 创建两个玩家
        self.ball = Ball(self.world, self)  # 创建球
        self.create_walls()  # 创建墙壁

        self.scores = {1: 0, 2: 0}  # 初始化得分
        self.font = pygame.font.SysFont(None, 36)  # 创建字体对象

    def create_walls(self):
        """创建游戏边界墙"""
        upper_wall = b2PolygonShape()  # 创建上边界形状
        lower_wall = b2PolygonShape()  # 创建下边界形状

        # 使用SetAsBox创建墙体
        upper_wall.SetAsBox(WIDTH / PPM / 2, 0.1, b2Vec2(WIDTH / PPM / 2, 0.1), 0)
        lower_wall.SetAsBox(WIDTH / PPM / 2, 0.1, b2Vec2(WIDTH / PPM / 2, (HEIGHT / PPM) - 0.1), 0)

        # 创建静态的墙体物体
        self.world.CreateStaticBody(shapes=[upper_wall, lower_wall])

    def handle_collision(self, contact):
        """
        处理碰撞
        :param contact: 碰撞对象
        """
        body_a = contact.fixtureA.body  # 获取碰撞物体A
        body_b = contact.fixtureB.body  # 获取碰撞物体B
        
        if (body_a == self.ball.body and body_b in [player.body for player in self.players]) or \
        (body_b == self.ball.body and body_a in [player.body for player in self.players]):
            # 球拍与球碰撞时施加力
            direction = (1.0, 0.0)  # 示例方向，可以根据需要动态调整
            self.ball.apply_hit_force(direction)
        
        return True  # 返回True表示碰撞处理完成
        
    def update(self, dt):
        """
        更新游戏状态
        :param dt: 时间步长
        """
        keys = pygame.key.get_pressed()  # 获取按键状态
        for player in self.players:
            player.update(keys)  # 更新玩家状态

        self.world.Step(TIME_STEP, 10, 10)  # 更新物理世界
        self.ball.update()  # 更新球的状态

    def draw(self, screen):
        """绘制游戏画面"""
        screen.fill(BG_COLOR)  # 填充背景色
        for player in self.players:
            player.draw(screen)  # 绘制玩家
        self.ball.draw(screen)  # 绘制球
        # 显示得分
        score_text = self.font.render(f"{self.scores[1]} : {self.scores[2]}", True, (255, 255, 255))
        screen.blit(score_text, (WIDTH / 2 - score_text.get_width() / 2, 20))