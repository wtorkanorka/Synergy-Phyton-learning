# 2 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
class Turtle(object):
    turtle_x = 0
    turtle_y = 0
    step = 0

    def __init__(self, t_x, t_y, s):
        self.turtle_x = t_x
        self.turtle_y = t_y
        self.step = s

    def go_up(self):
        self.turtle_y += self.step

    def go_down(self):
        self.turtle_y -= self.step

    def go_left(self):
        self.turtle_x -= self.step

    def go_right(self):
        self.turtle_x += self.step

    def evolve(self):
        self.step += 1

    def degrade(self):
        if self.step < 1:
            print("Шаг станет меньше нуля")
        else:
            self.step -= 1

    def count_moves(self, x_2, y_2):
        x_moves = abs((x_2 - self.turtle_x) // self.step)  # Количество шагов по оси х
        y_moves = abs((y_2 - self.turtle_y) // self.step)  # Количество шагов по оси у
        remainder_x = abs(x_2 - self.turtle_x) % self.step
        remainder_y = (
            abs(y_2 - self.turtle_y) % self.step
        )  # Проверка на остаток от деления
        if remainder_x > 0:
            x_moves += 1
        if remainder_y > 0:
            y_moves += 1
        return max(x_moves, y_moves)


turtle = Turtle(1, 1, 1)
print(turtle.count_moves(5, 5))
