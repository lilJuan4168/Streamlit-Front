import streamlit as st
import streamlit.components.v1 as components


st.sidebar.image("img/bocanblack.webp")

st.write("In development... play a game in the meanwhile")
if st.button("Play Snake Game", use_container_width=True):
   components.html("""

<!DOCTYPE html>
<html>
<head>
    <title>Juego de la Serpiente</title>
    <style>
        body {
            background-color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        canvas {
            border: 2px solid #FFF;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="400" height="400"></canvas>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');

        const SNAKE_SIZE = 20;
        const FOOD_SIZE = 20;
        let snake = [{ x: 10, y: 10 }];
        let food = { x: 5, y: 5 };
        let dx = 1;
        let dy = 0;
        let score = 0;
        let gameStarted = false;

        function drawSnake() {
            snake.forEach(segment => {
                ctx.fillStyle = '#00FF00';
                ctx.fillRect(segment.x * SNAKE_SIZE, segment.y * SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE);
            });
        }

        function drawFood() {
            ctx.fillStyle = '#FF0000';
            ctx.fillRect(food.x * SNAKE_SIZE, food.y * SNAKE_SIZE, FOOD_SIZE, FOOD_SIZE);
        }

        function update() {
            const newHead = { x: snake[0].x + dx, y: snake[0].y + dy };
            snake.unshift(newHead);

            if (newHead.x === food.x && newHead.y === food.y) {
                score += 10;
                document.getElementById('score').innerHTML = score;
                generateFood();
            } else {
                snake.pop();
            }
        }

        function generateFood() {
            food = {
                x: Math.floor(Math.random() * (canvas.width / SNAKE_SIZE)),
                y: Math.floor(Math.random() * (canvas.height / SNAKE_SIZE))
            };
        }

        function checkCollision() {
            if (
                snake[0].x < 0 ||
                snake[0].x >= canvas.width / SNAKE_SIZE ||
                snake[0].y < 0 ||
                snake[0].y >= canvas.height / SNAKE_SIZE
            ) {
                clearInterval(gameInterval);
                alert('Game Over! Your Score: ' + score);
            }

            for (let i = 1; i < snake.length; i++) {
                if (snake[i].x === snake[0].x && snake[i].y === snake[0].y) {
                    clearInterval(gameInterval);
                    alert('Game Over! Your Score: ' + score);
                }
            }
        }

        function gameLoop() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            if (gameStarted) {
                update();
                checkCollision();
            }

            drawSnake();
            drawFood();
        }

        document.addEventListener('keydown', event => {
            if (!gameStarted && event.key !== 'ArrowUp' && event.key !== 'ArrowDown' && event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') {
                return;
            }

            if (!gameStarted) {
                gameStarted = true;
            }

            switch (event.key) {
                case 'ArrowUp':
                    if (dy !== 1) {
                        dx = 0;
                        dy = -1;
                    }
                    break;
                case 'ArrowDown':
                    if (dy !== -1) {
                        dx = 0;
                        dy = 1;
                    }
                    break;
                case 'ArrowLeft':
                    if (dx !== 1) {
                        dx = -1;
                        dy = 0;
                    }
                    break;
                case 'ArrowRight':
                    if (dx !== -1) {
                        dx = 1;
                        dy = 0;
                    }
                    break;
            }
        });

        generateFood();
        setTimeout(() => {
            const gameInterval = setInterval(gameLoop, 100);
        }, 3000);
    </script>
    <div>Score: <span id="score">0</span></div>
</body>
</html>

   """, width=500, height=500)
if st.button("Restart", use_container_width=True):
    st.rerun()