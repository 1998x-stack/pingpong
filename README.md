

# Ping Pong Game

This is a simple two-player Ping Pong game built using `pygame` and `Box2D`. The game simulates a realistic table tennis experience with customizable physics, including ball friction, paddle movement, collision detection, sound effects, and background music.

## Features

- **Realistic Physics**: Powered by Box2D for dynamic collision handling and realistic movement.
- **Two-Player Mode**: Play locally with two players controlling paddles.
- **Customizable Gameplay**: Modify ball speed, paddle size, and friction settings for a tailored experience.
- **Sound Effects and Music**: Enjoy background music and sound effects when hitting the ball.
- **Collision-based Force**: Dynamic ball behavior upon collision, allowing for direction and speed change based on paddle interaction.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/pingpong-game.git
   cd pingpong-game
   ```

2. **Create a Conda Environment**

   Create and activate a new `conda` environment:
   
   ```bash
   conda create --name pong_game python=3.9
   conda activate pong_game
   ```

3. **Install Dependencies**

   Install the required libraries using `pip`:
   
   ```bash
   pip install -r requirements.txt
   ```

   **Requirements**:
   - `pygame`
   - `box2d-py` or `Box2D`
   
   You can also manually install the dependencies:
   
   ```bash
   pip install pygame box2d-py
   ```

## How to Play

1. **Run the Game**

   After installing the dependencies, you can start the game by running:

   ```bash
   python main.py
   ```

2. **Controls**

   - **Player 1**: Use `W` and `S` keys to move the left paddle up and down.
   - **Player 2**: Use `Up` and `Down` arrow keys to move the right paddle up and down.

3. **Objective**

   - The goal is to hit the ball past the opponent's paddle to score points. The first player to reach a predetermined score wins the game.

## Customization

You can customize various game settings by modifying the `settings.py` file:

- **Ball speed**: Adjust the ball's initial speed by modifying `INITIAL_BALL_SPEED`.
- **Paddle size**: Change the size of the paddles by modifying `PADDLE_WIDTH` and `PADDLE_HEIGHT`.
- **Friction**: Modify the paddle and ball friction by adjusting `PADDLE_FRICTION` and `BALL_FRICTION`.

## Sound and Music

The game features background music and sound effects when the ball is hit. You can replace the sound files with your own by modifying:

- `background_music.mp3` for the background track.
- `hit_sound.wav` for the sound effect when the ball hits the paddle.

## Future Improvements

- **AI Opponent**: Add an AI-controlled paddle for single-player mode.
- **Online Multiplayer**: Allow players to compete against each other over the network.
- **Power-ups**: Add power-ups to enhance gameplay dynamics.

## Contributing

Feel free to open issues or submit pull requests to improve the game. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## BUG FIX
```
pip uninstall Box2D
pip install box2d-py
brew install swig
pip install box2d-kengz
```