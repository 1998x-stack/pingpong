"""Regression tests for the image-background/paddle rendering contract.

The physics and audio dependencies are stubbed because these tests exercise
Game.draw(), not the Box2D simulation or an active display.
"""
import importlib.util
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import patch


class RecordingScreen:
    def __init__(self):
        self.drawn = []
        self.fills = []

    def blit(self, image, position):
        self.drawn.append((image, position))

    def fill(self, color):
        self.fills.append(color)
        self.drawn.clear()  # Model how a full-screen fill hides earlier pixels.


class ScoreText:
    def __init__(self, text):
        self.text = text

    def get_width(self):
        return 40


class ScoreFont:
    def render(self, text, antialias, color):
        return ScoreText(text)


class Drawable:
    def __init__(self, label):
        self.label = label

    def draw(self, screen):
        screen.blit(self.label, (0, 0))


class BackgroundRenderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Import the actual game.py with lightweight dependency stubs.
        box2d = types.ModuleType("Box2D")
        for symbol in ("b2World", "b2PolygonShape", "b2Vec2"):
            setattr(box2d, symbol, object())
        player = types.ModuleType("player")
        player.Player = object
        ball = types.ModuleType("ball")
        ball.Ball = object
        settings = types.ModuleType("settings")
        settings.WIDTH = 800
        settings.HEIGHT = 600
        settings.BG_COLOR = (0, 0, 0)
        deps = {
            "pygame": types.ModuleType("pygame"), "Box2D": box2d,
            "player": player, "ball": ball, "settings": settings,
        }
        path = Path(__file__).resolve().parents[1] / "game.py"
        spec = importlib.util.spec_from_file_location("pingpong_game_render_test", path)
        module = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, deps):
            spec.loader.exec_module(module)
        cls.Game = module.Game

    def new_game(self):
        game = self.Game.__new__(self.Game)  # Avoid physics initialization.
        game.players = [Drawable("paddle1"), Drawable("paddle2")]
        game.ball = Drawable("ball")
        game.font = ScoreFont()
        game.scores = {1: 3, 2: 7}
        return game

    def test_previously_blitted_background_is_not_erased(self):
        screen = RecordingScreen()
        background = object()
        screen.blit(background, (0, 0))  # main.py's existing draw order.
        self.new_game().draw(screen)
        self.assertEqual(screen.fills, [], "Game.draw must not erase main.py's background")
        self.assertIs(screen.drawn[0][0], background)

    def test_paddles_ball_and_score_remain_visible_in_order(self):
        screen = RecordingScreen()
        screen.blit("background", (0, 0))
        self.new_game().draw(screen)
        self.assertEqual([item[0] for item in screen.drawn[:4]],
                         ["background", "paddle1", "paddle2", "ball"])
        score, position = screen.drawn[4]
        self.assertEqual(score.text, "3 : 7")
        self.assertEqual(position, (380, 20))


if __name__ == "__main__":
    unittest.main()
