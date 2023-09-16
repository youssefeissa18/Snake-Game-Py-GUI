import random
import curses

screenWindow = curses.initscr()

curses.curs_set(0)

Height, Width = screenWindow.getmaxyx()


window = curses.newwin(Height, Width,0, 0)

window.keypad(1)

window.timeout(100)

snake_X = Width // 4
snake_Y = Height // 4

snakeBody = [
    [snake_Y, snake_X],
    [snake_Y, snake_X - 1],
    [snake_Y, snake_X - 2],
]


food = [
    Height // 2,
    Width // 2
]


window.addch(food[0], food[1], curses.ACS_PI)

Key = curses.KEY_RIGHT

while True:
    next_Key = window.getch()
    # Key = Key if next_Key == -1 else next_Key
    if next_Key == -1:
        Key = Key
    else:
        Key = next_Key
    if snakeBody[0][0] in [0, Height] or snakeBody[0][1] in [0, Width] or snakeBody[0] in [1:]:
        curses.endwin()
        quit()
