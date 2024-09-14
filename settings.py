# settings.py

# 屏幕设置
WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)
TARGET_FPS = 60
TIME_STEP = 1.0 / TARGET_FPS

# 物理转换比例
PPM = 20.0  # 每米对应的像素数

# 球拍设置（单位：米）
PADDLE_WIDTH = 0.5
PADDLE_HEIGHT = 3.0
PADDLE_START_X = {
    1: 2.0,
    2: (WIDTH / PPM) - 2.0
}
PADDLE_SPEED = 15.0  # 米/秒

# 乒乓球设置（单位：米）
BALL_RADIUS = 0.3
INITIAL_BALL_SPEED = 15.0  # 米/秒

# settings.py

# 球拍的摩擦系数
PADDLE_FRICTION = 0.5

# 球的摩擦系数
BALL_FRICTION = 0.2

# 施加到球的额外力大小
HIT_FORCE = 50.0