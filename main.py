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

snake = [
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
    if (
            snake[0][0] in [0, Height - 1] or
            snake[0][1] in [0, Width - 1] or
            snake[0] in snake[1:]
    ):
        curses.endwin()
        quit()
    new_Head = [snake[0][0],snake[0][1]]

    if Key == curses.KEY_DOWN:
        new_Head[0] += 1
    if Key == curses.KEY_UP:
        new_Head[0] -= 1
    if Key == curses.KEY_RIGHT:
        new_Head[1] += 1
    if Key == curses.KEY_LEFT:
        new_Head[1] -= 1

    snake.insert(0, new_Head)
    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, Height - 1),
                random.randint(1, Width - 1),
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)






