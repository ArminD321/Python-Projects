import tkinter as tk
from tkinter import messagebox
import random

# Constants
WINDOW_SIZE = 600
GRID_SIZE = 20
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
SNAKE_SPEED = 100  # Lower is faster
DIRECTIONS = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}

# Game Variables
snake = [(GRID_SIZE // 2, GRID_SIZE // 2)]
direction = "Right"
food_position = None
score = 0
game_over = False


def reset_game():
    """Resets the game to the initial state."""
    global snake, direction, food_position, score, game_over
    snake = [(GRID_SIZE // 2, GRID_SIZE // 2)]
    direction = "Right"
    score = 0
    game_over = False
    update_score()
    place_food()
    canvas.delete("all")
    draw_background()
    draw_snake()
    draw_food()
    game_loop()


def draw_background():
    """Draws the alternating green background."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = "lightgreen" if (row + col) % 2 == 0 else "green"
            canvas.create_rectangle(
                col * CELL_SIZE,
                row * CELL_SIZE,
                (col + 1) * CELL_SIZE,
                (row + 1) * CELL_SIZE,
                fill=color,
                outline="",  # No gridlines
            )


def draw_snake():
    """Draws the snake on the canvas."""
    for segment in snake:
        x, y = segment
        canvas.create_rectangle(
            x * CELL_SIZE,
            y * CELL_SIZE,
            (x + 1) * CELL_SIZE,
            (y + 1) * CELL_SIZE,
            fill="blue",
        )


def draw_food():
    """Draws the food on the canvas."""
    if food_position:
        x, y = food_position
        canvas.create_oval(
            x * CELL_SIZE,
            y * CELL_SIZE,
            (x + 1) * CELL_SIZE,
            (y + 1) * CELL_SIZE,
            fill="red",
        )


def place_food():
    """Places food at a random position not occupied by the snake."""
    global food_position
    while True:
        x = random.randint(0, GRID_SIZE - 5)
        y = random.randint(0, GRID_SIZE - 5)
        if (x, y) not in snake:
            food_position = (x, y)
            break


def update_score():
    """Updates the score label."""
    score_label.config(text=f"Score: {score}")


def move_snake():
    """Moves the snake in the current direction."""
    global snake, food_position, score, game_over

    # Calculate new head position
    head_x, head_y = snake[-1]
    delta_x, delta_y = DIRECTIONS[direction]
    new_head = (head_x + delta_x, head_y + delta_y)

    # Check collisions
    if (
        new_head in snake  # Snake collides with itself
        or new_head[0] < 0
        or new_head[1] < 0
        or new_head[0] >= GRID_SIZE
        or new_head[1] >= GRID_SIZE  # Snake hits the wall
    ):
        game_over = True
        messagebox.showerror("Game Over", f"You lost! Final score: {score}")
        return

    # Add the new head to the snake
    snake.append(new_head)

    # Check if the snake eats food
    if new_head == food_position:
        score += 1
        update_score()
        place_food()
        place_food()
        place_food()
        place_food()
        place_food()
        place_food()
        place_food()
        place_food()
    else:
        # Remove the tail if no food was eaten
        snake.pop(0)


def game_loop():
    """Main game loop."""
    global game_over
    if not game_over:
        move_snake()
        canvas.delete("all")
        draw_background()
        draw_snake()
        draw_food()
        root.after(SNAKE_SPEED, game_loop)


def change_direction(new_direction):
    """Changes the snake's direction."""
    global direction
    if (
        new_direction == "Up" and direction != "Down"
        or new_direction == "Down" and direction != "Up"
        or new_direction == "Left" and direction != "Right"
        or new_direction == "Right" and direction != "Left"
    ):
        direction = new_direction


# Main GUI setup
root = tk.Tk()
root.title("Snake Game")

# Create Menu
menu_bar = tk.Menu(root)
game_menu = tk.Menu(menu_bar, tearoff=0)
game_menu.add_command(label="New Game", command=reset_game)
game_menu.add_command(label="Quit", command=root.quit)
menu_bar.add_cascade(label="Game", menu=game_menu)
root.config(menu=menu_bar)

# Score Label
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 14))
score_label.pack()

# Create Canvas
canvas = tk.Canvas(root, width=WINDOW_SIZE, height=WINDOW_SIZE, bg="black")
canvas.pack()

# Bind Controls
root.bind("<Up>", lambda e: change_direction("Up"))
root.bind("<Down>", lambda e: change_direction("Down"))
root.bind("<Left>", lambda e: change_direction("Left"))
root.bind("<Right>", lambda e: change_direction("Right"))

# Start Game
reset_game()
root.mainloop()
