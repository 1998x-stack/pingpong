# main.py

import pygame  # 导入pygame库，用于游戏开发
from game import Game  # 从game模块导入Game类
from settings import WIDTH, HEIGHT, TARGET_FPS  # 从settings模块导入常量

def main():
    """主函数，游戏的入口点"""
    pygame.init()  # 初始化pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 创建游戏窗口
    pygame.display.set_caption("Double Ping Pong Game")  # 设置窗口标题

    # 加载背景图像
    background = pygame.image.load('assets/background.png').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # 加载音频
    pygame.mixer.music.load('assets/background.mp3')
    hit_sound = pygame.mixer.Sound('assets/hit.wav')
    restart_sound = pygame.mixer.Sound('assets/restart.wav')
    
    # 播放背景音乐（循环播放）
    pygame.mixer.music.play(-1)


    game = Game()  # 创建Game实例

    clock = pygame.time.Clock()  # 创建时钟对象，用于控制帧率
    running = True  # 游戏运行标志

    while running:  # 主游戏循环
        dt = clock.tick(TARGET_FPS) / 1000  # 计算帧时间（秒）
        for event in pygame.event.get():  # 处理事件
            if event.type == pygame.QUIT:  # 如果是退出事件
                running = False  # 结束游戏循环
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # 按R键重新开始游戏
                    restart_sound.play()
                    game = Game()

        game.update(dt)  # 更新游戏状态
        # 绘制背景
        screen.blit(background, (0, 0))
        game.draw(screen)  # 绘制游戏画面

        # 处理碰撞事件
        for contact in game.world.contacts:  # 遍历所有碰撞
            if game.handle_collision(contact):
                hit_sound.play()

        pygame.display.flip()  # 更新显示

    pygame.quit()  # 退出pygame

if __name__ == "__main__":
    main()  # 如果作为主程序运行，则调用main函数