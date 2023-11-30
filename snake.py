import curses
import random

screen = curses.initscr()
curses.curs_set(0)
screen_height, screen_width = screen.getmaxyx()
#creat a new window take a whole old window start from (0,0)
window = curses.newwin(screen_height, screen_width, 0, 0)
#to allwow window receive input from the keybord
window.keypad(True)
window.timeout(100)

# define the snake head
snk_x = screen_width // 4
snk_y = screen_height // 2
#define the intial position of snake's body
snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]
Food = [screen_height // 2, screen_width // 2]
# define the food
window.addch(Food[0], Food[1], curses.ACS_BULLET)
key = curses.KEY_RIGHT
while True:
  next_key = window.getch()
  key = key if next_key == -1 else next_key
  # if snake collided with twalls or itself
  if snake[0][0] in [0, screen_height] or snake[0][1] in [
      0, screen_width
  ] or snake[0] in snake[1:]:
    curses.endwin()
    quit()
  new_head = [snake[0][0], snake[0][1]]
  if key == curses.KEY_DOWN:
    new_head[0] += 1
  if key == curses.KEY_UP:
    new_head[0] -= 1
  if key == curses.KEY_RIGHT:
    new_head[1] += 1
  if key == curses.KEY_LEFT:
    new_head[1] -= 1
  #insert the new head to the first of snake list
  snake.insert(0, new_head)
  #if snake ate the food
  if snake[0] == Food:
    Food = None
    while Food is None:
      new_food = [
          random.randint(1, screen_height - 1),
          random.randint(1, screen_width - 1)
      ]
      Food = new_food if new_food not in snake else None
    window.addch(Food[0], Food[1], curses.ACS_BULLET)
  else:
    #otherwise remove the last segmant of snake body
    tail = snake.pop()
    window.addch(tail[0], tail[1], ' ')
    # put the snake in window
  window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
